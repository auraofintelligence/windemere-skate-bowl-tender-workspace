(() => {
  const root = document.querySelector("[data-site-360]");
  if (!root) return;

  const stage = root.querySelector("[data-sphere-stage]");
  const count = root.querySelector("[data-view-count]");
  const title = root.querySelector("[data-view-title]");
  const captureTime = root.querySelector("[data-capture-time]");
  const locationLink = root.querySelector("[data-location-link]");
  const originalLink = root.querySelector("[data-download-original]");
  const status = root.querySelector("[data-viewer-status]");
  const previousButton = root.querySelector("[data-previous-view]");
  const nextButton = root.querySelector("[data-next-view]");
  const saveButton = root.querySelector("[data-save-view]");
  const copyButton = root.querySelector("[data-copy-view]");
  const thumbnails = document.querySelector("[data-view-thumbnails]");
  const trail = document.querySelector("[data-capture-trail]");
  const flatView = document.querySelector("[data-flat-view]");

  let points = [];
  let activeIndex = 0;
  let sphereViewer = null;

  function setStatus(message) {
    if (status) status.textContent = message;
  }

  function supportsWebGl() {
    try {
      const canvas = document.createElement("canvas");
      return Boolean(
        window.WebGLRenderingContext
        && (canvas.getContext("webgl") || canvas.getContext("experimental-webgl"))
      );
    } catch (error) {
      return false;
    }
  }

  function loadingLayer() {
    const loading = document.createElement("div");
    loading.className = "site-360-loading";
    loading.dataset.viewerLoading = "";
    loading.setAttribute("role", "status");
    loading.textContent = "Loading 360 view...";
    return loading;
  }

  function hashState() {
    return new URLSearchParams(window.location.hash.replace(/^#/, ""));
  }

  function numericState(params, key, fallback) {
    const rawValue = params.get(key);
    if (rawValue === null || rawValue.trim() === "") return fallback;
    const value = Number(rawValue);
    return Number.isFinite(value) ? value : fallback;
  }

  function currentOrientation() {
    return {
      yaw: sphereViewer?.getYaw?.() ?? 0,
      pitch: sphereViewer?.getPitch?.() ?? -4,
      hfov: sphereViewer?.getHfov?.() ?? 120,
    };
  }

  function viewUrl(point, orientation = currentOrientation()) {
    const params = new URLSearchParams({
      photo: point.id,
      yaw: orientation.yaw.toFixed(1),
      pitch: orientation.pitch.toFixed(1),
      hfov: orientation.hfov.toFixed(1),
    });
    const url = new URL(window.location.href);
    url.hash = params.toString();
    return url;
  }

  function updateHash(point, orientation) {
    const url = viewUrl(point, orientation);
    window.history.replaceState(null, "", url);
    return url;
  }

  function setActiveMarkers(point) {
    document.querySelectorAll("[data-360-point]").forEach((button) => {
      button.setAttribute("aria-pressed", String(button.dataset.pointId === point.id));
    });
  }

  function preloadAdjacent() {
    [activeIndex - 1, activeIndex + 1].forEach((index) => {
      const point = points[index];
      if (!point) return;
      const image = new Image();
      image.src = point.viewer;
    });
  }

  function renderFallback(point, message) {
    stage.replaceChildren();
    const image = document.createElement("img");
    image.className = "site-360-fallback";
    image.src = point.viewer;
    image.alt = `${point.title} equirectangular panorama`;
    stage.append(image);
    setStatus(message);
  }

  function loadSphere(point, orientation) {
    if (sphereViewer?.destroy) sphereViewer.destroy();
    sphereViewer = null;
    stage.replaceChildren(loadingLayer());

    if (!supportsWebGl()) {
      renderFallback(point, "WebGL is unavailable. Showing the lightweight flat panorama instead.");
      return;
    }

    if (!window.pannellum?.viewer) {
      renderFallback(point, "The 360 library did not load. Showing the lightweight flat panorama instead.");
      return;
    }

    sphereViewer = window.pannellum.viewer(stage, {
      type: "equirectangular",
      panorama: point.viewer,
      autoLoad: true,
      showControls: true,
      showFullscreenCtrl: true,
      keyboardZoom: true,
      compass: false,
      pitch: orientation.pitch,
      yaw: orientation.yaw,
      hfov: orientation.hfov,
      minHfov: 35,
      maxHfov: 120,
      preview: point.thumbnail,
      previewTitle: point.title,
      previewAuthor: "Windemere Road Park site inspection, 15 July 2026",
      backgroundColor: [7 / 255, 23 / 255, 32 / 255],
    });

    sphereViewer.on("load", () => {
      stage.querySelector("[data-viewer-loading]")?.classList.add("is-hidden");
      setStatus(`${point.title} loaded from the lightweight viewer copy.`);
      preloadAdjacent();
    });

    sphereViewer.on("error", () => {
      renderFallback(point, "This 360 view could not load. Showing the flat panorama instead.");
    });
  }

  function setActive(index, orientation = { yaw: 0, pitch: -4, hfov: 120 }) {
    activeIndex = Math.max(0, Math.min(points.length - 1, index));
    const point = points[activeIndex];

    count.textContent = `View ${String(point.sequence).padStart(2, "0")} of ${points.length}`;
    title.textContent = point.title;
    captureTime.textContent = point.captureTimeLocal;
    originalLink.href = point.original;
    originalLink.download = point.sourceFile;
    flatView.src = point.viewer;
    flatView.alt = `${point.title} as a flat equirectangular strip`;

    if (point.latitude !== null && point.longitude !== null) {
      locationLink.href = `https://www.google.com/maps?q=${point.latitude},${point.longitude}`;
      locationLink.textContent = `${point.latitude.toFixed(6)}, ${point.longitude.toFixed(6)}`;
      locationLink.title = point.gpsCaution;
    } else {
      locationLink.removeAttribute("href");
      locationLink.textContent = "No camera GPS";
    }

    previousButton.disabled = activeIndex === 0;
    nextButton.disabled = activeIndex === points.length - 1;
    setActiveMarkers(point);
    updateHash(point, orientation);
    loadSphere(point, orientation);
  }

  function renderThumbnails() {
    thumbnails.replaceChildren();
    points.forEach((point, index) => {
      const button = document.createElement("button");
      button.className = "site-360-thumb";
      button.type = "button";
      button.dataset.pointId = point.id;
      button.setAttribute("data-360-point", "");
      button.setAttribute("aria-label", `Open ${point.title}`);
      button.setAttribute("aria-pressed", "false");

      const image = document.createElement("img");
      image.src = point.thumbnail;
      image.alt = "";
      image.loading = "lazy";
      image.width = 640;
      image.height = 360;

      const label = document.createElement("span");
      label.textContent = `${String(point.sequence).padStart(2, "0")} / ${point.captureTimeLocal.split(", ")[1]}`;
      button.append(image, label);
      button.addEventListener("click", () => setActive(index));
      thumbnails.append(button);
    });
  }

  function normalisedTrailPoints() {
    const mapped = points.filter((point) => point.latitude !== null && point.longitude !== null);
    if (!mapped.length) return [];

    const latitudes = mapped.map((point) => point.latitude);
    const longitudes = mapped.map((point) => point.longitude);
    const minLat = Math.min(...latitudes);
    const maxLat = Math.max(...latitudes);
    const minLon = Math.min(...longitudes);
    const maxLon = Math.max(...longitudes);
    const latRange = maxLat - minLat || 0.000001;
    const lonRange = maxLon - minLon || 0.000001;

    return mapped.map((point) => ({
      point,
      x: 24 + ((point.longitude - minLon) / lonRange) * 36,
      y: 18 + ((maxLat - point.latitude) / latRange) * 38,
    }));
  }

  function renderTrail() {
    trail.replaceChildren();
    const positions = normalisedTrailPoints();
    if (!positions.length) {
      trail.textContent = "No camera GPS was recorded.";
      return;
    }

    positions.forEach(({ point, x, y }) => {
      const button = document.createElement("button");
      button.type = "button";
      button.dataset.pointId = point.id;
      button.setAttribute("data-360-point", "");
      button.style.left = `${x}%`;
      button.style.top = `${y}%`;
      button.textContent = point.sequence;
      button.setAttribute("aria-label", `Open ${point.title}`);
      button.setAttribute("aria-pressed", "false");
      button.addEventListener("click", () => setActive(points.indexOf(point)));
      trail.append(button);
    });
  }

  function downloadBlob(blob, filename) {
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = filename;
    link.click();
    window.setTimeout(() => URL.revokeObjectURL(url), 2000);
  }

  function saveCurrentView() {
    const point = points[activeIndex];
    if (!sphereViewer?.isLoaded?.()) {
      setStatus("The 360 view is still loading.");
      return;
    }

    try {
      sphereViewer.stopMovement?.();
      const canvas = sphereViewer.getRenderer?.()?.getCanvas?.() || stage.querySelector("canvas");
      const orientation = currentOrientation();
      canvas.toBlob((blob) => {
        if (!blob) {
          setStatus("This browser could not export the current view. A normal screenshot will still work.");
          return;
        }
        const filename = `${point.id}-yaw-${orientation.yaw.toFixed(0)}-pitch-${orientation.pitch.toFixed(0)}.png`;
        downloadBlob(blob, filename);
        setStatus(`Saved ${filename}.`);
      }, "image/png");
    } catch (error) {
      setStatus("This browser could not export the current view. A normal screenshot will still work.");
    }
  }

  async function copyCurrentView() {
    const point = points[activeIndex];
    const orientation = currentOrientation();
    const url = updateHash(point, orientation);
    const reference = [
      `${point.title} / ${point.sourceFile}`,
      `Yaw ${orientation.yaw.toFixed(1)}, pitch ${orientation.pitch.toFixed(1)}, field of view ${orientation.hfov.toFixed(1)}`,
      url.toString(),
    ].join("\n");

    try {
      await navigator.clipboard.writeText(reference);
      setStatus("Exact view reference copied.");
    } catch (error) {
      window.prompt("Copy view reference", reference);
      setStatus("View reference prepared for copying.");
    }
  }

  previousButton.addEventListener("click", () => setActive(activeIndex - 1));
  nextButton.addEventListener("click", () => setActive(activeIndex + 1));
  saveButton.addEventListener("click", saveCurrentView);
  copyButton.addEventListener("click", copyCurrentView);

  document.addEventListener("keydown", (event) => {
    if (event.target instanceof HTMLInputElement || event.target instanceof HTMLTextAreaElement) return;
    if (event.key === "[") setActive(activeIndex - 1);
    if (event.key === "]") setActive(activeIndex + 1);
  });

  fetch(root.dataset.source)
    .then((response) => {
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      return response.json();
    })
    .then((records) => {
      points = records;
      if (!points.length) throw new Error("No 360 records found");
      renderThumbnails();
      renderTrail();

      const params = hashState();
      const requestedIndex = points.findIndex((point) => point.id === params.get("photo"));
      const orientation = {
        yaw: numericState(params, "yaw", 0),
        pitch: numericState(params, "pitch", -4),
        hfov: numericState(params, "hfov", 120),
      };
      setActive(requestedIndex >= 0 ? requestedIndex : 0, orientation);
    })
    .catch((error) => {
      stage.replaceChildren();
      setStatus(`The 360 site record could not load: ${error.message}`);
    });
})();
