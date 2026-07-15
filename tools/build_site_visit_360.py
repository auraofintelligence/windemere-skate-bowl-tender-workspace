from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

from PIL import ExifTags, Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "assets" / "img" / "GoPro360-site-visit"
VIEWER_DIR = ROOT / "assets" / "img" / "site-360-viewer"
THUMB_DIR = ROOT / "assets" / "img" / "site-360-thumbs"
DATA_PATH = ROOT / "data" / "site-visit-360.json"
VIEWER_WIDTH = 3200
THUMB_SIZE = (640, 360)


def gps_to_decimal(value, ref: str) -> float:
    degrees, minutes, seconds = value
    decimal = float(degrees) + float(minutes) / 60 + float(seconds) / 3600
    return -decimal if ref in {"S", "W"} else decimal


def read_gps(image: Image.Image) -> tuple[float, float] | None:
    exif = image.getexif()
    if not exif:
        return None

    gps_key = next(
        (key for key in exif if ExifTags.TAGS.get(key) == "GPSInfo"),
        None,
    )
    if gps_key is None:
        return None

    gps_raw = exif.get_ifd(gps_key)
    gps = {ExifTags.GPSTAGS.get(key, key): value for key, value in gps_raw.items()}
    latitude = gps.get("GPSLatitude")
    latitude_ref = gps.get("GPSLatitudeRef")
    longitude = gps.get("GPSLongitude")
    longitude_ref = gps.get("GPSLongitudeRef")
    if not all((latitude, latitude_ref, longitude, longitude_ref)):
        return None

    return (
        gps_to_decimal(latitude, latitude_ref),
        gps_to_decimal(longitude, longitude_ref),
    )


def read_capture_time(image: Image.Image, source: Path) -> datetime:
    exif = image.getexif()
    for tag in (36867, 36868, 306):
        value = exif.get(tag)
        if not value:
            continue
        try:
            return datetime.strptime(str(value), "%Y:%m:%d %H:%M:%S")
        except ValueError:
            pass
    return datetime.fromtimestamp(source.stat().st_mtime)


def format_capture_time(value: datetime) -> str:
    hour = value.strftime("%I").lstrip("0") or "0"
    return (
        f"{value.day} {value.strftime('%B %Y')}, "
        f"{hour}:{value.strftime('%M:%S')} {value.strftime('%p').lower()}"
    )


def resize_to_width(image: Image.Image, width: int) -> Image.Image:
    if image.width <= width:
        return image.copy()
    height = round(image.height * width / image.width)
    return image.resize((width, height), Image.Resampling.LANCZOS)


def make_thumbnail(image: Image.Image) -> Image.Image:
    crop_width = image.width // 2
    crop_height = round(crop_width * THUMB_SIZE[1] / THUMB_SIZE[0])
    left = (image.width - crop_width) // 2
    top = max(0, (image.height - crop_height) // 2)
    crop = image.crop((left, top, left + crop_width, top + crop_height))
    return crop.resize(THUMB_SIZE, Image.Resampling.LANCZOS)


def save_webp(image: Image.Image, path: Path, quality: int) -> None:
    image.convert("RGB").save(path, "WEBP", quality=quality, method=6)


def main() -> None:
    sources = sorted(SOURCE_DIR.glob("GS__*.JPG"))
    if not sources:
        raise SystemExit(f"No GoPro JPG files found in {SOURCE_DIR}")

    VIEWER_DIR.mkdir(parents=True, exist_ok=True)
    THUMB_DIR.mkdir(parents=True, exist_ok=True)
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)

    for path in VIEWER_DIR.glob("windemere-site-360-*.webp"):
        path.unlink()
    for path in THUMB_DIR.glob("windemere-site-360-*-thumb.webp"):
        path.unlink()

    scanned = []
    for source in sources:
        with Image.open(source) as image:
            scanned.append(
                {
                    "source": source,
                    "capture": read_capture_time(image, source),
                    "gps": read_gps(image),
                    "width": image.width,
                    "height": image.height,
                }
            )

    scanned.sort(key=lambda item: (item["capture"], item["source"].name))
    records = []
    for sequence, item in enumerate(scanned, start=1):
        source = item["source"]
        slug = f"windemere-site-360-{sequence:02d}"
        viewer_path = VIEWER_DIR / f"{slug}.webp"
        thumb_path = THUMB_DIR / f"{slug}-thumb.webp"

        with Image.open(source) as image:
            save_webp(resize_to_width(image, VIEWER_WIDTH), viewer_path, quality=72)
            save_webp(make_thumbnail(image), thumb_path, quality=72)

        latitude, longitude = item["gps"] if item["gps"] else (None, None)
        records.append(
            {
                "id": slug,
                "sequence": sequence,
                "title": f"Windemere site view {sequence:02d}",
                "sourceFile": source.name,
                "captureTimeLocal": format_capture_time(item["capture"]),
                "latitude": round(latitude, 6) if latitude is not None else None,
                "longitude": round(longitude, 6) if longitude is not None else None,
                "gpsCaution": "Camera EXIF position, rounded and not survey-grade.",
                "originalWidth": item["width"],
                "originalHeight": item["height"],
                "viewer": f"../assets/img/site-360-viewer/{viewer_path.name}",
                "thumbnail": f"../assets/img/site-360-thumbs/{thumb_path.name}",
                "original": f"../assets/img/GoPro360-site-visit/{source.name}",
            }
        )

    DATA_PATH.write_text(json.dumps(records, indent=2) + "\n", encoding="utf-8")
    viewer_bytes = sum(path.stat().st_size for path in VIEWER_DIR.glob("*.webp"))
    original_bytes = sum(path.stat().st_size for path in sources)
    print(f"Wrote {len(records)} Windemere 360 records")
    print(f"Viewer payload: {viewer_bytes / 1024 / 1024:.1f} MB total")
    print(f"Original payload retained: {original_bytes / 1024 / 1024:.1f} MB total")


if __name__ == "__main__":
    main()
