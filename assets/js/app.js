(function () {
  const topButton = document.querySelector(".back-to-top");
  if (topButton) {
    topButton.addEventListener("click", () => window.scrollTo({ top: 0, behavior: "smooth" }));
  }

  const statusClass = (status) => {
    const lower = String(status || "").toLowerCase();
    if (lower.includes("specialist") || lower.includes("parked")) return "warning";
    if (lower.includes("ready")) return "gum";
    if (lower.includes("review")) return "dark";
    return "";
  };

  const badge = (text) => `<span class="badge ${statusClass(text)}">${escapeHtml(text || "To confirm")}</span>`;

  const escapeHtml = (value) => String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");

  async function loadJson(src) {
    const response = await fetch(src, { cache: "no-store" });
    if (!response.ok) throw new Error(`Could not load ${src}`);
    return response.json();
  }

  async function renderQuestions() {
    const mount = document.querySelector("[data-questions-src]");
    if (!mount) return;
    try {
      const rows = await loadJson(mount.dataset.questionsSrc);
      mount.innerHTML = `
        <div class="table-wrap">
          <table>
            <thead>
              <tr>
                <th scope="col">ID</th>
                <th scope="col">Question</th>
                <th scope="col">Category</th>
                <th scope="col">Raised by</th>
                <th scope="col">Owner</th>
                <th scope="col">Due</th>
                <th scope="col">Status</th>
                <th scope="col">Answer / notes</th>
                <th scope="col">Tender impact</th>
              </tr>
            </thead>
            <tbody>
              ${rows.map((row) => `
                <tr>
                  <td>${escapeHtml(row.id)}</td>
                  <td>${escapeHtml(row.question)}</td>
                  <td>${escapeHtml(row.category)}</td>
                  <td>${escapeHtml(row.raisedBy)}</td>
                  <td>${escapeHtml(row.owner)}</td>
                  <td>${escapeHtml(row.due)}</td>
                  <td>${badge(row.status)}</td>
                  <td>${escapeHtml(row.notes || "")}</td>
                  <td>${escapeHtml(row.impact)}</td>
                </tr>`).join("")}
            </tbody>
          </table>
        </div>`;
    } catch (error) {
      mount.innerHTML = `<p class="warning-box">Questions could not load from JSON. Try viewing through a local server or GitHub Pages.</p>`;
    }
  }

  async function renderTasks() {
    const mount = document.querySelector("[data-tasks-src]");
    if (!mount) return;
    try {
      const rows = await loadJson(mount.dataset.tasksSrc);
      const columns = ["To confirm", "Ready to draft", "Drafting", "Needs VFG review", "Needs specialist", "Ready", "Parked / no bid"];
      mount.innerHTML = `<div class="board">${
        columns.map((column) => {
          const cards = rows.filter((row) => row.status === column).map((row) => `
            <article class="task-card">
              <strong>${escapeHtml(row.id)} - ${escapeHtml(row.title)}</strong>
              <small>Owner: ${escapeHtml(row.owner)}</small>
              <small>Due: ${escapeHtml(row.due)}</small>
              <p>${escapeHtml(row.notes)}</p>
            </article>
          `).join("");
          return `<section class="board-column"><h3>${escapeHtml(column)}</h3>${cards || "<p>No current cards.</p>"}</section>`;
        }).join("")
      }</div>`;
    } catch (error) {
      mount.innerHTML = `<p class="warning-box">Tasks could not load from JSON. Try viewing through a local server or GitHub Pages.</p>`;
    }
  }

  async function renderDocs() {
    const mount = document.querySelector("[data-docs-src]");
    if (!mount) return;
    try {
      const rows = await loadJson(mount.dataset.docsSrc);
      mount.innerHTML = `
        <div class="table-wrap docs-table-wrap">
          <table class="docs-table">
            <thead>
              <tr>
                <th scope="col">File name</th>
                <th scope="col">Purpose</th>
                <th scope="col">Key notes</th>
                <th scope="col">Used for</th>
                <th scope="col">Public/private caution</th>
                <th scope="col">Download</th>
              </tr>
            </thead>
            <tbody>
              ${rows.map((row) => `
                <tr>
                  <td data-label="File name">${escapeHtml(row.file)}</td>
                  <td data-label="Purpose">${escapeHtml(row.purpose)}</td>
                  <td data-label="Key notes">${escapeHtml(row.notes)}</td>
                  <td data-label="Used for">${escapeHtml(row.usedFor)}</td>
                  <td data-label="Public/private caution">${escapeHtml(row.caution)}</td>
                  <td data-label="Download" class="download-cell">${row.downloadPath ? `<a class="download-link" href="${escapeHtml(row.downloadPath)}" download>Download</a>` : ""}</td>
                </tr>`).join("")}
            </tbody>
          </table>
        </div>`;
    } catch (error) {
      mount.innerHTML = `<p class="warning-box">Document data could not load from JSON. Try viewing through a local server or GitHub Pages.</p>`;
    }
  }

  async function renderReturnables() {
    const mount = document.querySelector("[data-returnables-src]");
    if (!mount) return;
    try {
      const rows = await loadJson(mount.dataset.returnablesSrc);
      mount.innerHTML = `<div class="grid two">${
        rows.map((row) => `
          <article class="card">
            <div class="card-top"><span class="badge dark">Returnable ${escapeHtml(row.id)}</span></div>
            <h3>${escapeHtml(row.name)}</h3>
            <p><strong>What it asks for:</strong> ${escapeHtml(row.asks)}</p>
            <p><strong>Probable lead:</strong> ${escapeHtml(row.lead)}</p>
            <p><strong>Luke may help:</strong> ${escapeHtml(row.luke)}</p>
            <p><strong>Evidence needed:</strong> ${escapeHtml(row.evidence)}</p>
            <p><strong>Could become non-conforming if:</strong> ${escapeHtml(row.nonConforming)}</p>
          </article>
        `).join("")
      }</div>`;
    } catch (error) {
      mount.innerHTML = `<p class="warning-box">Returnables could not load from JSON. Try viewing through a local server or GitHub Pages.</p>`;
    }
  }

  renderQuestions();
  renderTasks();
  renderDocs();
  renderReturnables();
})();
