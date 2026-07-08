from __future__ import annotations

import argparse
import io
import json
import urllib.request
from pathlib import Path

import fitz
from PIL import Image, ImageOps


ROOT = Path(__file__).resolve().parents[1]

VFG_SOURCES = [
    ("vfg-home-facility.jpg", "https://www.skateparkconstruction.com.au/userfiles/image/home-img.jpg", "VFG public website image - action sport facility context", "VFG public website home page"),
    ("vfg-black-head-01.jpg", "https://www.skateparkconstruction.com.au/userfiles/image/black-head-skatepark-01.jpg", "Black Head NSW 2025 - construction image from VFG public projects page", "VFG public projects page"),
    ("vfg-black-head-02.jpg", "https://www.skateparkconstruction.com.au/userfiles/image/black-head-skatepark-02.jpg", "Black Head NSW 2025 - construction image from VFG public projects page", "VFG public projects page"),
    ("vfg-boorowa-2021.jpg", "https://www.skateparkconstruction.com.au/userfiles/image/Resized_20211207_125335%202.jpeg", "Boorowa 2021 - construction image from VFG public projects page", "VFG public projects page"),
    ("vfg-barham-2019.jpg", "https://www.skateparkconstruction.com.au/userfiles/image/Barham.jpg", "Barham 2019 - consultation, conceptualisation, design and construction example", "VFG public projects page"),
    ("vfg-finley-2019.jpg", "https://www.skateparkconstruction.com.au/userfiles/image/Finley.jpg", "Finley 2019 - consultation, conceptualisation, design and construction example", "VFG public projects page"),
    ("vfg-howlong-2018.jpg", "https://www.skateparkconstruction.com.au/userfiles/image/Howlong.jpg", "Howlong 2018 - construction example", "VFG public projects page"),
    ("vfg-murwillumbah-2016.jpg", "https://www.skateparkconstruction.com.au/userfiles/image/Murwilumbah.jpg", "Murwillumbah 2016 - construction example", "VFG public projects page"),
]


def resize_jpeg(image: Image.Image, max_width: int, target: Path) -> None:
    image = ImageOps.exif_transpose(image.convert("RGB"))
    if image.width > max_width:
        ratio = max_width / image.width
        image = image.resize((max_width, int(image.height * ratio)), Image.Resampling.LANCZOS)
    target.parent.mkdir(parents=True, exist_ok=True)
    image.save(target, quality=84, optimize=True, progressive=True)


def extract_appendix_d(pdf_path: Path) -> list[dict[str, str]]:
    output_dir = ROOT / "assets" / "img" / "site-photos"
    doc = fitz.open(pdf_path)
    records = []
    for page_index, page in enumerate(doc, start=1):
        candidates = []
        for img in page.get_images(full=True):
            info = doc.extract_image(img[0])
            candidates.append((info.get("width", 0) * info.get("height", 0), info))
        if not candidates:
            continue
        _, info = max(candidates, key=lambda item: item[0])
        image = Image.open(io.BytesIO(info["image"]))
        filename = f"windemere-site-{page_index:02d}.jpg"
        resize_jpeg(image, 1600, output_dir / filename)
        records.append({
            "src": f"../assets/img/site-photos/{filename}",
            "homeSrc": f"assets/img/site-photos/{filename}",
            "caption": f"Appendix D site photo plate {page_index:02d}",
            "source": "Appendix D - Site Photos - 02 June 2026",
            "alt": f"Actual tender site photo from Appendix D, plate {page_index:02d}.",
        })
    (ROOT / "data" / "site-photos.json").write_text(json.dumps(records, indent=2), encoding="utf-8")
    return records


def download_vfg_images() -> list[dict[str, str]]:
    output_dir = ROOT / "assets" / "img" / "vfg"
    records = []
    for filename, url, caption, source in VFG_SOURCES:
        with urllib.request.urlopen(url, timeout=30) as response:
            image = Image.open(io.BytesIO(response.read()))
        resize_jpeg(image, 1400, output_dir / filename)
        records.append({
            "src": f"../assets/img/vfg/{filename}",
            "homeSrc": f"assets/img/vfg/{filename}",
            "caption": caption,
            "source": source,
            "sourceUrl": url,
            "alt": caption,
        })
    (ROOT / "data" / "vfg-images.json").write_text(json.dumps(records, indent=2), encoding="utf-8")
    return records


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract real tender/VFG images for the static site.")
    parser.add_argument("--appendix-d", type=Path, help="Path to Appendix D site photos PDF.")
    parser.add_argument("--skip-vfg", action="store_true", help="Do not download VFG public website images.")
    args = parser.parse_args()

    if args.appendix_d:
        site_records = extract_appendix_d(args.appendix_d)
        print(f"Extracted {len(site_records)} Appendix D images.")
    if not args.skip_vfg:
        vfg_records = download_vfg_images()
        print(f"Downloaded {len(vfg_records)} VFG images.")


if __name__ == "__main__":
    main()
