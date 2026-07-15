from __future__ import annotations

import html
import json
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
SITE_TITLE = "Strange But True x VFG exploratory workspace"
TENDER_TITLE = "PDG-20842-1 Skate Bowl Refurbishment"
SITE_URL = "https://auraofintelligence.github.io/windemere-skate-bowl-tender-workspace/"
DOCUMENT_ZIP = "PDG-20842-1_Windemere_tender_documents.zip"

NAV = [
    ("index.html", "Dashboard"),
    ("pages/tender-overview.html", "Tender overview"),
    ("pages/site-visit.html", "Site visit"),
    ("pages/site-visit-360.html", "360 site record"),
    ("pages/site-photos.html", "Site photos"),
    ("pages/partnership.html", "Partnership"),
    ("pages/vfg-capability-map.html", "VFG capability"),
    ("pages/strange-but-true-role.html", "Luke role"),
    ("pages/role-boundaries.html", "Boundaries"),
    ("pages/compliance-matrix.html", "Compliance matrix"),
    ("pages/project-brief-coverage.html", "Brief coverage"),
    ("pages/returnables.html", "Returnables"),
    ("pages/concept-design-workspace.html", "Concept design"),
    ("pages/cad-workflow.html", "CAD workflow"),
    ("pages/questions-register.html", "Questions"),
    ("pages/task-board.html", "Task board"),
    ("pages/decision-gate.html", "Decision gate"),
    ("pages/risk-and-assumptions.html", "Risks"),
    ("pages/document-register.html", "Documents"),
    ("pages/back-and-forth-log.html", "Back-and-forth"),
    ("pages/local-benefit.html", "Local benefit"),
    ("pages/submission-roadmap.html", "Roadmap"),
    ("pages/site-map.html", "Site map"),
]

NAV_GROUPS = [
    ("Tender", [
        ("pages/tender-overview.html", "Tender overview"),
        ("pages/compliance-matrix.html", "Compliance matrix"),
        ("pages/project-brief-coverage.html", "Brief coverage"),
        ("pages/returnables.html", "Returnables"),
        ("pages/document-register.html", "Documents"),
        ("pages/risk-and-assumptions.html", "Risks and assumptions"),
    ]),
    ("Site evidence", [
        ("pages/site-visit.html", "Site visit record"),
        ("pages/site-visit-360.html", "360 site record"),
        ("pages/site-photos.html", "Tender-pack photos"),
        ("pages/questions-register.html", "Questions register"),
    ]),
    ("Bid build", [
        ("pages/vfg-capability-map.html", "VFG capability"),
        ("pages/concept-design-workspace.html", "Concept design"),
        ("pages/cad-workflow.html", "CAD workflow"),
        ("pages/local-benefit.html", "Local benefit"),
        ("pages/submission-roadmap.html", "Submission roadmap"),
    ]),
    ("Team", [
        ("pages/partnership.html", "Partnership"),
        ("pages/strange-but-true-role.html", "Luke / Strange But True"),
        ("pages/role-boundaries.html", "Role boundaries"),
    ]),
    ("Tracking", [
        ("pages/task-board.html", "Task board"),
        ("pages/decision-gate.html", "Decision gate"),
        ("pages/back-and-forth-log.html", "Back-and-forth log"),
    ]),
]

site_photos = [
    {
        "src": f"../assets/img/site-photos/windemere-site-{i:02d}.jpg",
        "homeSrc": f"assets/img/site-photos/windemere-site-{i:02d}.jpg",
        "caption": f"Appendix D site photo plate {i:02d}",
        "source": "Appendix D - Site Photos - 02 June 2026",
        "alt": f"Actual tender site photo from Appendix D, plate {i:02d}.",
    }
    for i in range(1, 16)
]

vfg_images = [
    {
        "src": "../assets/img/vfg/vfg-home-facility.jpg",
        "homeSrc": "assets/img/vfg/vfg-home-facility.jpg",
        "caption": "VFG public website image - action sport facility context",
        "source": "VFG public website home page",
        "sourceUrl": "https://www.skateparkconstruction.com.au/userfiles/image/home-img.jpg",
        "alt": "VFG public website image showing an action sport facility context.",
    },
    {
        "src": "../assets/img/vfg/vfg-black-head-01.jpg",
        "homeSrc": "assets/img/vfg/vfg-black-head-01.jpg",
        "caption": "Black Head NSW 2025 - construction image from VFG public projects page",
        "source": "VFG public projects page",
        "sourceUrl": "https://www.skateparkconstruction.com.au/userfiles/image/black-head-skatepark-01.jpg",
        "alt": "Black Head NSW 2025 construction image from VFG public projects page.",
    },
    {
        "src": "../assets/img/vfg/vfg-black-head-02.jpg",
        "homeSrc": "assets/img/vfg/vfg-black-head-02.jpg",
        "caption": "Black Head NSW 2025 - construction image from VFG public projects page",
        "source": "VFG public projects page",
        "sourceUrl": "https://www.skateparkconstruction.com.au/userfiles/image/black-head-skatepark-02.jpg",
        "alt": "Black Head NSW 2025 construction image from VFG public projects page.",
    },
    {
        "src": "../assets/img/vfg/vfg-boorowa-2021.jpg",
        "homeSrc": "assets/img/vfg/vfg-boorowa-2021.jpg",
        "caption": "Boorowa 2021 - construction image from VFG public projects page",
        "source": "VFG public projects page",
        "sourceUrl": "https://www.skateparkconstruction.com.au/userfiles/image/Resized_20211207_125335%202.jpeg",
        "alt": "Boorowa 2021 construction image from VFG public projects page.",
    },
    {
        "src": "../assets/img/vfg/vfg-barham-2019.jpg",
        "homeSrc": "assets/img/vfg/vfg-barham-2019.jpg",
        "caption": "Barham 2019 - consultation, conceptualisation, design and construction example",
        "source": "VFG public projects page",
        "sourceUrl": "https://www.skateparkconstruction.com.au/userfiles/image/Barham.jpg",
        "alt": "Barham 2019 project image from VFG public projects page.",
    },
    {
        "src": "../assets/img/vfg/vfg-finley-2019.jpg",
        "homeSrc": "assets/img/vfg/vfg-finley-2019.jpg",
        "caption": "Finley 2019 - consultation, conceptualisation, design and construction example",
        "source": "VFG public projects page",
        "sourceUrl": "https://www.skateparkconstruction.com.au/userfiles/image/Finley.jpg",
        "alt": "Finley 2019 project image from VFG public projects page.",
    },
    {
        "src": "../assets/img/vfg/vfg-howlong-2018.jpg",
        "homeSrc": "assets/img/vfg/vfg-howlong-2018.jpg",
        "caption": "Howlong 2018 - construction example",
        "source": "VFG public projects page",
        "sourceUrl": "https://www.skateparkconstruction.com.au/userfiles/image/Howlong.jpg",
        "alt": "Howlong 2018 project image from VFG public projects page.",
    },
    {
        "src": "../assets/img/vfg/vfg-murwillumbah-2016.jpg",
        "homeSrc": "assets/img/vfg/vfg-murwillumbah-2016.jpg",
        "caption": "Murwillumbah 2016 - construction example",
        "source": "VFG public projects page",
        "sourceUrl": "https://www.skateparkconstruction.com.au/userfiles/image/Murwilumbah.jpg",
        "alt": "Murwillumbah 2016 project image from VFG public projects page.",
    },
]


def write(path: str, content: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    cleaned = "\n".join(line.rstrip() for line in content.strip().splitlines())
    target.write_text(cleaned + "\n", encoding="utf-8")


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def url_parts(path: str) -> str:
    return "/".join(quote(part) for part in path.split("/"))


def base_for(path: str) -> str:
    return "../" if path.startswith("pages/") else ""


def nav_html(current: str, base: str) -> str:
    def nav_link(href: str, label: str, class_name: str = "") -> str:
        active = " aria-current=\"page\"" if href == current else ""
        classes = f" class=\"{class_name}\"" if class_name else ""
        return f"<a{classes} href=\"{base}{href}\"{active}>{esc(label)}</a>"

    desktop_groups = []
    mobile_groups = []
    for group_label, links in NAV_GROUPS:
        active_class = " has-current" if any(href == current for href, _label in links) else ""
        group_links = "".join(nav_link(href, label) for href, label in links)
        desktop_groups.append(f"""
          <details class="nav-group{active_class}">
            <summary>{esc(group_label)}</summary>
            <div class="nav-group-panel">{group_links}</div>
          </details>
        """)
        mobile_groups.append(f"""
          <section class="nav-mobile-section">
            <strong>{esc(group_label)}</strong>
            <div>{group_links}</div>
          </section>
        """)

    dashboard = nav_link("index.html", "Dashboard", "nav-direct")
    site_map = nav_link("pages/site-map.html", "Site map", "nav-direct")
    return f"""
        <nav class="site-nav" aria-label="Primary">
          <div class="nav-desktop">
            {dashboard}
            {''.join(desktop_groups)}
            {site_map}
          </div>
          <details class="nav-mobile">
            <summary>Browse {len(NAV)} pages</summary>
            <div class="nav-mobile-panel">
              <div class="nav-mobile-direct">{dashboard}{site_map}</div>
              {''.join(mobile_groups)}
            </div>
          </details>
        </nav>
    """


def page_links(current: str, base: str) -> str:
    index = next((i for i, item in enumerate(NAV) if item[0] == current), 0)
    prev_item = NAV[index - 1] if index > 0 else None
    next_item = NAV[index + 1] if index + 1 < len(NAV) else None
    links = []
    if prev_item:
        links.append(f"<a class=\"pager-link\" href=\"{base}{prev_item[0]}\">Previous: {esc(prev_item[1])}</a>")
    if next_item:
        links.append(f"<a class=\"pager-link\" href=\"{base}{next_item[0]}\">Next: {esc(next_item[1])}</a>")
    if not links:
        return ""
    return f"<nav class=\"page-pager\" aria-label=\"Page sequence\">{''.join(links)}</nav>"


def layout(
    path: str,
    title: str,
    intro: str,
    body: str,
    *,
    body_class: str = "",
    extra_head: str = "",
    extra_scripts: str = "",
) -> str:
    base = base_for(path)
    current = path
    class_attr = f" {body_class}" if body_class else ""
    return f"""<!doctype html>
<html lang="en-AU">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)} | {esc(SITE_TITLE)}</title>
  <meta name="description" content="Exploratory tender partnership workspace for {esc(TENDER_TITLE)}.">
  <link rel="icon" href="{base}favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="{base}assets/css/style.css">
  {extra_head}
</head>
<body class="{class_attr.strip()}">
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="brand-row">
      <a class="brand" href="{base}index.html" aria-label="Workspace dashboard">
        <span class="brand-mark" aria-hidden="true">SB</span>
        <span>
          <strong>{esc(SITE_TITLE)}</strong>
          <small>{esc(TENDER_TITLE)}</small>
        </span>
      </a>
      <span class="header-status">Exploratory tender workspace</span>
    </div>
    {nav_html(current, base)}
  </header>

  <aside class="caution-banner" role="note">
    <strong>Public/private caution:</strong> Source tender documents are downloadable here for easy review. Keep filled returnables, prices, signatures, private contacts and final tender material out of the public site unless the team explicitly agrees.
  </aside>

  <main id="main" class="page-shell">
    <section class="page-intro">
      <p class="kicker">Not for construction / exploratory tender workspace</p>
      <h1>{esc(title)}</h1>
      <p>{esc(intro)}</p>
    </section>
    {body}
    {page_links(current, base)}
  </main>

  <button class="back-to-top" type="button" aria-label="Back to top">^</button>
  <footer class="site-footer">
    <p>{esc(SITE_TITLE)}. Not official Redland City Council material. Not VFG's final tender submission. All rights reserved.</p>
  </footer>
  <script src="{base}assets/js/app.js" defer></script>
  {extra_scripts}
</body>
</html>"""


def card(title: str, text: str, status: str = "", href: str | None = None) -> str:
    badge = f"<span class=\"badge\">{esc(status)}</span>" if status else ""
    link = f"<a class=\"card-link\" href=\"{esc(href)}\">Open</a>" if href else ""
    return f"""
      <article class="card">
        <div class="card-top">{badge}</div>
        <h3>{esc(title)}</h3>
        <p>{esc(text)}</p>
        {link}
      </article>
    """


def list_items(items: list[str], cls: str = "check-list") -> str:
    return f"<ul class=\"{cls}\">" + "".join(f"<li>{esc(item)}</li>" for item in items) + "</ul>"


def badge(text: str, kind: str = "") -> str:
    classes = f"badge {kind}".strip()
    return f"<span class=\"{classes}\">{esc(text)}</span>"


def table(headers: list[str], rows: list[list[str]], classes: str = "") -> str:
    ths = "".join(f"<th scope=\"col\">{esc(h)}</th>" for h in headers)
    trs = []
    for row in rows:
        cells = "".join(f"<td>{cell}</td>" for cell in row)
        trs.append(f"<tr>{cells}</tr>")
    return f"""
      <div class="table-wrap {esc(classes)}">
        <table>
          <thead><tr>{ths}</tr></thead>
          <tbody>{''.join(trs)}</tbody>
        </table>
      </div>
    """


def photo_grid(items: list[dict[str, str]], *, home: bool = False, limit: int | None = None) -> str:
    selected = items[:limit] if limit else items
    cards = []
    for item in selected:
        src = item["homeSrc"] if home else item["src"]
        source = item.get("source", "")
        source_url = item.get("sourceUrl")
        source_html = (
            f"<a href=\"{esc(source_url)}\" rel=\"noopener\">{esc(source)}</a>"
            if source_url
            else esc(source)
        )
        cards.append(f"""
          <figure class="photo-card">
            <img src="{esc(src)}" alt="{esc(item['alt'])}" loading="lazy">
            <figcaption>
              <strong>{esc(item['caption'])}</strong>
              <span>{source_html}</span>
            </figcaption>
          </figure>
        """)
    return f"<div class=\"photo-grid\">{''.join(cards)}</div>"


questions = [
    {"id": "Q01", "question": "What are VFG's practical ideas for the bowl repairs?", "category": "Bowl repair", "raisedBy": "Luke", "owner": "VFG", "due": "Site visit", "status": "To confirm", "notes": "", "impact": "Shapes repair method and Returnable I."},
    {"id": "Q02", "question": "Which defects are safety-critical vs desirable improvements?", "category": "Safety", "raisedBy": "Luke", "owner": "VFG / Specialist", "due": "Site visit", "status": "To confirm", "notes": "", "impact": "Separates mandatory repair scope from enhancement ideas."},
    {"id": "Q03", "question": "How would VFG approach cracks over 5 mm and height irregularities over 3 mm?", "category": "Audit priority", "raisedBy": "Tender audit", "owner": "VFG", "due": "Before concept response", "status": "Needs VFG review", "notes": "", "impact": "Priority 1 repair response."},
    {"id": "Q04", "question": "What coping repairs are likely?", "category": "Audit priority", "raisedBy": "Tender audit", "owner": "VFG", "due": "Before concept response", "status": "Needs VFG review", "notes": "", "impact": "Repair methodology and BOQ review."},
    {"id": "Q05", "question": "What street elements would broaden use without overbuilding the site?", "category": "Concept design", "raisedBy": "Luke", "owner": "VFG / Joint", "due": "Site visit", "status": "To confirm", "notes": "", "impact": "Supports participation and concept design weighting."},
    {"id": "Q06", "question": "Where could ledges, rails, manual pads or banks sit while respecting existing flow?", "category": "Layout", "raisedBy": "Luke", "owner": "VFG", "due": "After sketches", "status": "To confirm", "notes": "", "impact": "Feeds concept CAD layout."},
    {"id": "Q07", "question": "Is drainage a design issue, maintenance issue, or both?", "category": "Drainage", "raisedBy": "Site photos", "owner": "VFG / Specialist", "due": "Site visit", "status": "Open question", "notes": "", "impact": "Important because June photos show water while the audit did not."},
    {"id": "Q08", "question": "How do the June photos showing standing water change the site assessment?", "category": "Drainage", "raisedBy": "Luke", "owner": "VFG / Specialist", "due": "Site visit", "status": "Open question", "notes": "", "impact": "May affect survey, levels and repair sequencing."},
    {"id": "Q09", "question": "What survey, levels and service information is needed before CAD gets serious?", "category": "CAD inputs", "raisedBy": "Luke", "owner": "Joint", "due": "After site visit", "status": "To confirm", "notes": "", "impact": "Controls drawing caveats and specialist pathway."},
    {"id": "Q10", "question": "What is VFG comfortable sketching at tender stage?", "category": "Concept design", "raisedBy": "Luke", "owner": "VFG", "due": "Site visit", "status": "To confirm", "notes": "", "impact": "Defines Luke drafting support boundary."},
    {"id": "Q11", "question": "What needs RPEQ or specialist confirmation?", "category": "Certification", "raisedBy": "Tender brief", "owner": "VFG / Specialist", "due": "Before submission", "status": "Specialist required", "notes": "", "impact": "Critical to design-and-construct compliance."},
    {"id": "Q12", "question": "What is excluded from Luke's role?", "category": "Role boundaries", "raisedBy": "Luke", "owner": "Joint", "due": "Before drafting", "status": "To confirm", "notes": "", "impact": "Protects the partnership and keeps claims honest."},
    {"id": "Q13", "question": "What returnables can each party provide?", "category": "Returnables", "raisedBy": "Section B", "owner": "Joint", "due": "Before bid decision", "status": "To confirm", "notes": "", "impact": "Bid/no-bid decision."},
    {"id": "Q14", "question": "Who owns pricing, construction methodology, WHS, environmental and QA plans?", "category": "Ownership", "raisedBy": "Luke", "owner": "VFG", "due": "Before submission", "status": "Needs VFG review", "notes": "", "impact": "These should be led by VFG or qualified specialists."},
    {"id": "Q15", "question": "What would make this a no-bid?", "category": "Decision gate", "raisedBy": "Luke", "owner": "Joint", "due": "Before submission work ramps up", "status": "Open question", "notes": "", "impact": "Avoids wasting effort if core risks cannot be solved."},
    {"id": "Q16", "question": "What would make this a strong bid?", "category": "Decision gate", "raisedBy": "Luke", "owner": "Joint", "due": "Before submission work ramps up", "status": "Open question", "notes": "", "impact": "Clarifies the winning argument if the team proceeds."},
]

tasks = [
    {"id": "T01", "title": "Confirm repo publication boundary", "status": "Ready", "owner": "Luke", "due": "Now", "notes": "Source tender files are public here by project direction; filled forms, prices and private details stay out."},
    {"id": "T02", "title": "Confirm VFG contact details to display or keep private", "status": "To confirm", "owner": "VFG / Luke", "due": "Before public sharing", "notes": "Prefer website links, not personal contact details."},
    {"id": "T03", "title": "Confirm mandatory site inspection attendance", "status": "To confirm", "owner": "VFG / Luke", "due": "RSVP by 2:00 pm Tuesday 14 July 2026", "notes": "Addendum 1 updated the site inspection details."},
    {"id": "T04", "title": "Confirm addendum signed and returnable", "status": "To confirm", "owner": "Tender lead", "due": "Tender submission", "notes": "Signed Addendum 1 must come back with tender documents."},
    {"id": "T05", "title": "Review BOQ structure", "status": "Ready to draft", "owner": "VFG", "due": "Before pricing", "notes": "No prices in this public workspace."},
    {"id": "T06", "title": "Create concept design sketch capture workflow", "status": "Ready to draft", "owner": "Luke / VFG", "due": "After site visit", "notes": "Sketches should be labelled tender concept only."},
    {"id": "T07", "title": "Draft site visit notes template", "status": "Ready", "owner": "Luke", "due": "Before site visit", "notes": "Printable agenda and note sections are seeded."},
    {"id": "T08", "title": "Draft role boundaries", "status": "Ready", "owner": "Luke", "due": "Before partnership decision", "notes": "Boundary page separates support from certification."},
    {"id": "T09", "title": "Build compliance matrix", "status": "Ready", "owner": "Luke", "due": "Before bid decision", "notes": "Initial matrix seeded from prompt and source check."},
    {"id": "T10", "title": "Draft local benefit and social benefit angle", "status": "Ready to draft", "owner": "Luke / VFG", "due": "Before Returnable G", "notes": "Keep it tender-grounded, not grandiose."},
    {"id": "T11", "title": "Collect VFG project examples and referees", "status": "Needs VFG review", "owner": "VFG", "due": "Before Returnable J", "notes": "Use VFG-supplied evidence and permissions."},
    {"id": "T12", "title": "Confirm RPEQ and design consultant pathway", "status": "Needs specialist", "owner": "VFG / Specialist", "due": "Before proceeding", "notes": "Critical design-and-construct requirement."},
    {"id": "T13", "title": "Confirm survey and service location requirements", "status": "Needs specialist", "owner": "VFG / Specialist", "due": "After site visit", "notes": "Needed before serious CAD."},
    {"id": "T14", "title": "Draft CAD layer standard", "status": "Ready", "owner": "Luke", "due": "Before CAD sketches", "notes": "Layer list is seeded under cad/."},
    {"id": "T15", "title": "Draft Returnable I concept response outline", "status": "Ready to draft", "owner": "Luke / VFG", "due": "After concept direction", "notes": "Requires VFG design intent."},
    {"id": "T16", "title": "Draft Returnable K methodology outline", "status": "Ready to draft", "owner": "VFG / Luke", "due": "After delivery method", "notes": "Construction method must be VFG-led."},
    {"id": "T17", "title": "Decide bid / no-bid", "status": "Parked / no bid", "owner": "Joint", "due": "Decision gate", "notes": "Only proceed if roles, returnables, pricing and certification pathway are credible."},
]

docs = [
    {"file": "(Addendum)_PDG-20842-1_Addendum_1.pdf", "purpose": "Updates tender timing and site inspection details.", "notes": "Closing moved to 2:00 pm 6 August 2026. Mandatory site inspection moved to 10:00 am Wednesday 15 July 2026. RSVP by 2:00 pm Tuesday 14 July 2026.", "usedFor": "Dates, attendance, signed addendum task.", "caution": "Downloadable source document. Upload only blank/source copy, not a signed return copy."},
    {"file": "PDG-20842-1_ITT_Invitation_To_Tender.pdf", "purpose": "Invitation, tender rules, evaluation criteria and lodgement structure.", "notes": "Section A retained by tenderers. Section B deliverables become the tender offer.", "usedFor": "Tender overview, compliance matrix, returnables.", "caution": "Downloadable source document. Site pages still use summary language for readability."},
    {"file": "PDG-20842-1_Project_Brief.pdf", "purpose": "Technical project brief and design-and-construct scope.", "notes": "Includes staged design, RPEQ for-construction drawings, as-constructed and Form 16 pathway.", "usedFor": "Scope, CAD workflow, specialist boundaries.", "caution": "Downloadable source document. Summaries are not engineering advice."},
    {"file": "PDG-20842-1_Section_B_Returnable_Schedule_Attachments.docx", "purpose": "Returnable schedules A-L to complete and lodge.", "notes": "Failure to provide required schedules may make a tender non-conforming.", "usedFor": "Returnables page and compliance matrix.", "caution": "Blank/source schedule is downloadable. Filled forms, signatures and private evidence stay out."},
    {"file": "PDG-20842-1_Bill_of_Quantities.xlsm", "purpose": "BOQ workbook for tendered sum structure.", "notes": "Use for structure only in this workspace. Pricing belongs outside the public site.", "usedFor": "Returnable H planning.", "caution": "Blank/source workbook is downloadable. Completed prices, rates and totals stay out."},
    {"file": "Appendix_A-PDG-20842_CIP_Skate_Bowl-Windemere_Road_Park__Alexandra_Hills-Ow (1).pdf", "purpose": "Owner's consent / property-related appendix.", "notes": "Supports site authority context.", "usedFor": "Document register and planning context.", "caution": "Downloadable source document for tender context."},
    {"file": "Appendix_B-2023_Redland_City_Council_Wayfinding_Signage_Manual_Core_Standar (2).pdf", "purpose": "Wayfinding signage core standards.", "notes": "Any signage concept should be RCC-style compliant, accessible, visible and non-hazardous.", "usedFor": "Concept design and signage notes.", "caution": "Downloadable source document. Reuse in final tender material should stay source-faithful."},
    {"file": "Appendix_C-RCC_Skatepark_Audit_Jan_2026.pdf", "purpose": "Skatepark audit for Windemere Road Park.", "notes": "Condition rating 3 - Fair. Priority actions include cracks/wide joints over 5 mm, height irregularities over 3 mm and coping repairs.", "usedFor": "Repair priorities, site visit questions, concept options.", "caution": "Downloadable source document. Do not turn audit notes into final design recommendations without VFG/specialist review."},
    {"file": "Appendix_D-Site_Photos-02_June_2026.pdf", "purpose": "June 2026 site photo pack.", "notes": "Photos show water/pooling, debris, graffiti, cracking and existing shelter/fencing context.", "usedFor": "Drainage questions, site observations and public visual context.", "caution": "Downloadable source document. Extracted web images are also shown on the site photos page."},
    {"file": "Appendix_E-FBD-106_A_Fencing_Welded_Mesh_Fencing_&_Control_Fence.pdf", "purpose": "Welded mesh fencing / control fence detail.", "notes": "Use standard detail as source where fencing is relevant.", "usedFor": "Fencing and ancillary works planning.", "caution": "Downloadable source document. Concept only until confirmed against standards and site."},
    {"file": "PDG-20842-1_AS4300-1995_General_Conditions.pdf", "purpose": "General contract conditions.", "notes": "Important for risk review and formal tender/legal review.", "usedFor": "Risk and assumptions.", "caution": "Downloadable source document. Not legal advice."},
    {"file": "READ ME - TRUNCATED FILE NAMES.txt", "purpose": "VendorPanel package note.", "notes": "Explains that some downloaded filenames may be truncated.", "usedFor": "Download-pack housekeeping.", "caution": "Downloadable package note."},
]

for doc in docs:
    doc["downloadPath"] = f"../tender-documents/{url_parts(doc['file'])}"

returnables = [
    {"id": "A", "name": "Form of Tender", "asks": "Formal tender offer details and signing.", "lead": "VFG / tender lead", "luke": "Can help organise wording and check completeness.", "evidence": "Authorised signer, legal entity details, final offer package.", "nonConforming": "Unsigned, incomplete or inconsistent offer details."},
    {"id": "B", "name": "Compliance and Declarations", "asks": "Statement of compliance, non-compliance and declarations.", "lead": "VFG / tender lead", "luke": "Can help track exceptions and plain-English notes.", "evidence": "Reviewed tender conditions and specialist/legal input if needed.", "nonConforming": "Unclear exceptions, missing declarations or unsupported compliance claims."},
    {"id": "C", "name": "Social Responsibility", "asks": "Social benefit and responsibility response.", "lead": "Joint", "luke": "Can draft local/community benefit language for review.", "evidence": "Practical local benefit commitments VFG can actually deliver.", "nonConforming": "Grand claims without delivery pathway."},
    {"id": "D", "name": "Insurance", "asks": "Required insurance evidence.", "lead": "VFG", "luke": "Can list documents needed.", "evidence": "Certificates of currency and required policy details.", "nonConforming": "Expired, insufficient or missing cover."},
    {"id": "E", "name": "Licences / Certificates", "asks": "Relevant licences, certificates and qualifications.", "lead": "VFG / Specialist", "luke": "Can build the evidence checklist.", "evidence": "Licences, accreditations, RPEQ or consultant evidence where required.", "nonConforming": "Missing required qualifications or unverified specialist claims."},
    {"id": "F", "name": "Subcontractors / Subconsultants", "asks": "Nominate subcontractors and consultants.", "lead": "VFG", "luke": "Can maintain the register.", "evidence": "Names, scopes, capability evidence, insurance/licence info.", "nonConforming": "Unclear critical roles or missing specialist pathway."},
    {"id": "G", "name": "Local Business and Benefit", "asks": "Local benefit response worth 15 percent.", "lead": "Joint", "luke": "Can draft Redlands/SEQ benefit framing.", "evidence": "Actual local suppliers, spend categories and community benefit commitments.", "nonConforming": "Unsupported local benefit promises."},
    {"id": "H", "name": "Tendered Sum and BOQ", "asks": "Tendered sum and bill of quantities.", "lead": "VFG", "luke": "Can help cross-reference structure, not price.", "evidence": "Final rates, lump sum, BOQ checks, exclusions and assumptions.", "nonConforming": "Arithmetic errors, missing BOQ items, public leakage of pricing."},
    {"id": "I", "name": "Proposed Concept Design", "asks": "Concept response worth 10 percent.", "lead": "VFG / Joint", "luke": "Can translate VFG design intent into tender-friendly narrative and concept drawings labelled correctly.", "evidence": "VFG sketches, repair method, progression feature intent, signage/fencing notes.", "nonConforming": "Design claims without VFG/specialist confirmation."},
    {"id": "J", "name": "Experience and Operational Capability", "asks": "Company and project team experience worth 30 percent.", "lead": "VFG", "luke": "Can format capability mapping and case-study prompts.", "evidence": "Project examples, referees, team CVs and relevant delivery history.", "nonConforming": "Unsupported experience claims or missing referees."},
    {"id": "K", "name": "Program / Methodology / Cashflow", "asks": "Works program, methodology and anticipated cashflow worth 15 percent.", "lead": "VFG", "luke": "Can structure the written methodology from VFG inputs.", "evidence": "Construction sequence, access, hold points, program, resources and cashflow.", "nonConforming": "Unrealistic program or non-specialist methodology claims."},
    {"id": "L", "name": "QMS / WHSMP / SSEMP", "asks": "Accreditation systems and management plans. Mandatory.", "lead": "VFG / Specialist", "luke": "Can track plan names and required attachments.", "evidence": "Quality, safety and environmental systems and project-specific plans.", "nonConforming": "Missing mandatory management systems or plans."},
]


def write_assets() -> None:
    write("assets/css/style.css", r"""
:root {
  --navy: #102433;
  --navy-2: #17374a;
  --concrete: #eef1ef;
  --concrete-2: #d8dedb;
  --ink: #172126;
  --muted: #5a6870;
  --sand: #c7ad7a;
  --sand-soft: #f3ead7;
  --teal: #2d7776;
  --teal-soft: #d9eeee;
  --gum: #3f704c;
  --gum-soft: #dfeade;
  --warning: #8d5d21;
  --white: #ffffff;
  --border: #ccd5d2;
  --shadow: 0 16px 40px rgba(16, 36, 51, 0.12);
  --radius: 8px;
  --max: 1180px;
}

* {
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  margin: 0;
  background: var(--concrete);
  color: var(--ink);
  font-family: Arial, Helvetica, sans-serif;
  line-height: 1.55;
}

a {
  color: var(--teal);
}

a:hover,
a:focus {
  color: var(--navy);
}

.skip-link {
  position: absolute;
  left: 1rem;
  top: -5rem;
  z-index: 10;
  background: var(--white);
  color: var(--navy);
  padding: 0.7rem 1rem;
  border: 2px solid var(--teal);
}

.skip-link:focus {
  top: 1rem;
}

.site-header {
  background: var(--navy);
  color: var(--white);
  padding: 1rem clamp(1rem, 4vw, 2.5rem) 1.2rem;
  border-bottom: 5px solid var(--teal);
}

.brand-row,
.site-nav,
.page-shell,
.site-footer {
  max-width: var(--max);
  margin: 0 auto;
}

.brand-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}

.brand {
  color: var(--white);
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 0.8rem;
}

.brand strong,
.brand small {
  display: block;
}

.brand small {
  color: #c9d9dc;
  font-size: 0.8rem;
}

.brand-mark {
  width: 2.5rem;
  height: 2.5rem;
  border: 2px solid var(--sand);
  display: grid;
  place-items: center;
  font-weight: 800;
  letter-spacing: 0;
}

.header-status {
  border: 1px solid rgba(255, 255, 255, 0.25);
  color: #dbe7e6;
  padding: 0.45rem 0.7rem;
  font-size: 0.84rem;
}

.site-nav {
  margin-top: 1rem;
  position: relative;
}

.nav-desktop {
  display: flex;
  flex-wrap: wrap;
  gap: 0.45rem;
  align-items: flex-start;
}

.nav-desktop > a,
.nav-group > summary,
.nav-mobile > summary {
  color: var(--white);
  text-decoration: none;
  border: 1px solid rgba(255, 255, 255, 0.2);
  padding: 0.45rem 0.6rem;
  min-height: 2.35rem;
  display: inline-flex;
  align-items: center;
  font-size: 0.9rem;
  background: rgba(255, 255, 255, 0.06);
}

.nav-desktop > a[aria-current="page"],
.nav-group.has-current > summary,
.nav-mobile-section a[aria-current="page"],
.nav-mobile-direct a[aria-current="page"] {
  background: var(--sand);
  color: var(--navy);
  border-color: var(--sand);
  font-weight: 700;
}

.nav-group {
  position: relative;
}

.nav-group > summary,
.nav-mobile > summary {
  cursor: pointer;
  list-style: none;
}

.nav-group > summary::-webkit-details-marker,
.nav-mobile > summary::-webkit-details-marker {
  display: none;
}

.nav-group > summary::after,
.nav-mobile > summary::after {
  content: "+";
  margin-left: 0.5rem;
  color: #b8ced0;
  font-weight: 900;
}

.nav-group[open] > summary::after,
.nav-mobile[open] > summary::after {
  content: "-";
}

.nav-group-panel {
  position: absolute;
  left: 0;
  top: calc(100% + 0.4rem);
  z-index: 8;
  display: grid;
  gap: 0.35rem;
  width: 18rem;
  padding: 0.55rem;
  background: var(--navy-2);
  border: 1px solid rgba(255, 255, 255, 0.22);
  box-shadow: var(--shadow);
}

.nav-group:nth-last-of-type(-n + 2) .nav-group-panel {
  right: 0;
  left: auto;
}

.nav-group-panel a,
.nav-mobile-panel a {
  display: flex;
  align-items: center;
  min-height: 2.45rem;
  padding: 0.5rem 0.65rem;
  border: 1px solid transparent;
  color: #e5eeee;
  text-decoration: none;
  overflow-wrap: anywhere;
}

.nav-group-panel a:hover,
.nav-group-panel a:focus-visible,
.nav-mobile-panel a:hover,
.nav-mobile-panel a:focus-visible {
  border-color: rgba(255, 255, 255, 0.24);
  background: rgba(255, 255, 255, 0.1);
  color: var(--white);
}

.nav-mobile {
  display: none;
}

.caution-banner {
  background: var(--sand-soft);
  color: #3d2d13;
  border-bottom: 1px solid #dfca9d;
  padding: 0.85rem clamp(1rem, 4vw, 2.5rem);
}

.caution-banner strong {
  color: #211707;
}

.page-shell {
  padding: clamp(1.2rem, 4vw, 2.6rem);
}

.page-intro {
  max-width: 860px;
  margin-bottom: 1.6rem;
}

.page-intro h1 {
  margin: 0.15rem 0 0.6rem;
  color: var(--navy);
  font-size: clamp(2rem, 4vw, 4.1rem);
  line-height: 1.04;
}

.page-intro p {
  color: var(--muted);
  font-size: 1.05rem;
}

.kicker {
  margin: 0;
  color: var(--warning);
  font-weight: 800;
  text-transform: uppercase;
  font-size: 0.78rem;
}

.hero-grid {
  display: grid;
  grid-template-columns: minmax(0, 1.05fr) minmax(280px, 0.95fr);
  gap: clamp(1rem, 3vw, 2rem);
  align-items: stretch;
}

.hero-panel {
  background: var(--navy);
  color: var(--white);
  padding: clamp(1.2rem, 3vw, 2rem);
  border-radius: var(--radius);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  min-height: 25rem;
}

.hero-panel h2 {
  font-size: clamp(2.1rem, 5vw, 5rem);
  line-height: 0.98;
  margin: 0 0 1rem;
}

.hero-panel p {
  color: #d6e2e2;
  max-width: 45rem;
}

.hero-image {
  margin: 0;
  background: #c7d1cf;
  border-radius: var(--radius);
  overflow: hidden;
  min-height: 25rem;
  box-shadow: var(--shadow);
}

.hero-image img {
  display: block;
  width: 100%;
  height: 100%;
  min-height: 25rem;
  object-fit: cover;
}

.hero-image figcaption {
  background: rgba(16, 36, 51, 0.92);
  color: #d9e7e7;
  padding: 0.65rem 0.8rem;
  font-size: 0.82rem;
}

.photo-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1rem;
}

.photo-card {
  margin: 0;
  background: var(--white);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  overflow: hidden;
}

.photo-card img {
  display: block;
  width: 100%;
  aspect-ratio: 4 / 3;
  object-fit: cover;
  background: var(--concrete-2);
}

.photo-card figcaption {
  padding: 0.75rem;
  font-size: 0.86rem;
  color: var(--muted);
}

.photo-card figcaption strong,
.photo-card figcaption span {
  display: block;
}

.photo-card figcaption strong {
  color: var(--navy);
  margin-bottom: 0.22rem;
}

.image-rail {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 0.75rem;
}

.image-rail img {
  width: 100%;
  aspect-ratio: 4 / 3;
  object-fit: cover;
  border-radius: var(--radius);
  border: 1px solid var(--border);
}

.sbt-intro {
  display: grid;
  grid-template-columns: minmax(0, 0.9fr) minmax(280px, 1.1fr);
  gap: clamp(1rem, 3vw, 2rem);
  align-items: stretch;
  background: #121c27;
  color: var(--white);
  border-radius: var(--radius);
  padding: clamp(1.1rem, 3vw, 2rem);
  box-shadow: var(--shadow);
}

.sbt-logo-panel {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  min-height: 21rem;
}

.sbt-logo-panel img {
  width: min(14rem, 70vw);
  border-radius: 6px;
  border: 1px solid rgba(255, 255, 255, 0.24);
  box-shadow: 0 16px 38px rgba(0, 0, 0, 0.28);
}

.sbt-intro h2 {
  color: var(--white);
  font-size: clamp(2rem, 4vw, 4rem);
  line-height: 1;
  margin: 0 0 1rem;
}

.sbt-intro p,
.sbt-intro li {
  color: #dce8ea;
}

.sbt-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.7rem;
  margin-top: 1rem;
}

.project-link-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 0.9rem;
}

.project-link-card {
  display: flex;
  flex-direction: column;
  gap: 0.45rem;
  min-height: 13rem;
  padding: 1rem;
  border: 1px solid var(--border);
  border-radius: var(--radius);
  background: var(--white);
  color: var(--ink);
  text-decoration: none;
}

.project-link-card span {
  width: fit-content;
  padding: 0.2rem 0.45rem;
  border-radius: 4px;
  background: var(--teal-soft);
  color: #124948;
  font-size: 0.74rem;
  font-weight: 800;
}

.project-link-card strong {
  color: var(--navy);
  font-size: 1.03rem;
}

.project-link-card p {
  margin: 0;
  color: var(--muted);
}

.project-link-card:hover,
.project-link-card:focus {
  border-color: var(--teal);
  box-shadow: 0 10px 28px rgba(16, 36, 51, 0.12);
}

.quick-status {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-top: 1.2rem;
}

.section {
  margin: clamp(1.2rem, 4vw, 2.6rem) 0;
}

.section h2 {
  color: var(--navy);
  font-size: clamp(1.5rem, 3vw, 2.2rem);
  margin: 0 0 0.7rem;
}

.section > p {
  max-width: 860px;
  color: var(--muted);
}

.band {
  background: var(--white);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: clamp(1rem, 3vw, 1.6rem);
  box-shadow: 0 1px 0 rgba(16, 36, 51, 0.04);
}

.band.tint {
  background: #f7f8f4;
}

.grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1rem;
}

.grid.two {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}

.card {
  background: var(--white);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1rem;
  min-height: 12rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.card h3 {
  color: var(--navy);
  margin: 0.35rem 0 0.45rem;
  font-size: 1.12rem;
}

.card p {
  color: var(--muted);
  margin: 0;
}

.card-link,
.button-link,
.download-link,
.pager-link {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 2.35rem;
  width: fit-content;
  margin-top: 0.9rem;
  padding: 0.45rem 0.75rem;
  background: var(--teal);
  color: var(--white);
  text-decoration: none;
  border-radius: 4px;
  font-weight: 700;
}

.card-link:hover,
.button-link:hover,
.download-link:hover,
.pager-link:hover,
.card-link:focus,
.button-link:focus,
.download-link:focus,
.pager-link:focus {
  background: var(--navy);
  color: var(--white);
}

.button-link.secondary {
  background: var(--navy);
}

.button-link.secondary:hover,
.button-link.secondary:focus {
  background: var(--teal);
}

.download-link {
  margin-top: 0;
  white-space: nowrap;
}

.badge {
  display: inline-flex;
  align-items: center;
  min-height: 1.65rem;
  width: fit-content;
  padding: 0.22rem 0.5rem;
  border-radius: 4px;
  background: var(--teal-soft);
  color: #124948;
  font-size: 0.76rem;
  font-weight: 800;
}

.badge.warning {
  background: var(--sand-soft);
  color: var(--warning);
}

.badge.gum {
  background: var(--gum-soft);
  color: #24512f;
}

.badge.dark {
  background: var(--navy);
  color: var(--white);
}

.status-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.6rem;
  margin: 1rem 0;
}

.check-list,
.plain-list {
  padding-left: 1.1rem;
}

.check-list li,
.plain-list li {
  margin: 0.35rem 0;
}

.split {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(280px, 0.75fr);
  gap: 1rem;
  align-items: start;
}

.note-box {
  border-left: 5px solid var(--teal);
  background: var(--teal-soft);
  padding: 1rem;
  border-radius: 0 var(--radius) var(--radius) 0;
}

.warning-box {
  border-left: 5px solid var(--warning);
  background: var(--sand-soft);
  padding: 1rem;
  border-radius: 0 var(--radius) var(--radius) 0;
}

.table-wrap {
  width: 100%;
  overflow-x: auto;
  background: var(--white);
  border: 1px solid var(--border);
  border-radius: var(--radius);
}

table {
  width: 100%;
  border-collapse: collapse;
  min-width: 760px;
}

.docs-table-wrap {
  overflow-x: visible;
}

.docs-table {
  table-layout: fixed;
  min-width: 0;
}

.docs-table th,
.docs-table td {
  overflow-wrap: anywhere;
  word-break: normal;
  hyphens: auto;
}

.docs-table th:nth-child(1),
.docs-table td:nth-child(1) {
  width: 24%;
}

.docs-table th:nth-child(2),
.docs-table td:nth-child(2) {
  width: 14%;
}

.docs-table th:nth-child(3),
.docs-table td:nth-child(3) {
  width: 22%;
}

.docs-table th:nth-child(4),
.docs-table td:nth-child(4) {
  width: 15%;
}

.docs-table th:nth-child(5),
.docs-table td:nth-child(5) {
  width: 15%;
}

.docs-table th:nth-child(6),
.docs-table td:nth-child(6) {
  width: 10%;
}

.docs-table .download-cell {
  text-align: center;
}

.docs-table .download-link {
  display: inline-flex;
  width: min(100%, 7rem);
  justify-content: center;
  white-space: nowrap;
  overflow-wrap: normal;
  line-height: 1.15;
  padding: 0.45rem 0.5rem;
  font-size: 0.84rem;
}

th,
td {
  text-align: left;
  vertical-align: top;
  border-bottom: 1px solid var(--border);
  padding: 0.72rem 0.8rem;
}

th {
  color: var(--navy);
  background: #e8eeec;
  font-size: 0.84rem;
}

td {
  font-size: 0.92rem;
}

tbody tr:hover {
  background: #f8faf9;
}

.board {
  display: grid;
  grid-template-columns: repeat(4, minmax(220px, 1fr));
  gap: 1rem;
}

.board-column {
  border: 1px solid var(--border);
  background: #f8faf9;
  border-radius: var(--radius);
  min-height: 10rem;
  padding: 0.8rem;
}

.board-column h3 {
  margin: 0 0 0.8rem;
  color: var(--navy);
  font-size: 1rem;
}

.task-card {
  background: var(--white);
  border: 1px solid var(--border);
  border-radius: 6px;
  padding: 0.8rem;
  margin-bottom: 0.7rem;
}

.task-card strong {
  display: block;
  color: var(--navy);
  margin-bottom: 0.35rem;
}

.task-card small {
  display: block;
  color: var(--muted);
}

.timeline {
  border-left: 4px solid var(--teal);
  padding-left: 1rem;
}

.timeline article {
  background: var(--white);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1rem;
  margin: 0 0 1rem;
}

.label-strip {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-top: 0.8rem;
}

.site-footer {
  color: #d9e6e5;
  background: var(--navy);
  padding: 1.2rem clamp(1rem, 4vw, 2.5rem);
}

.site-footer p {
  margin: 0 auto;
  max-width: var(--max);
}

.page-pager {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
  margin-top: 2rem;
  border-top: 1px solid var(--border);
  padding-top: 1rem;
}

.back-to-top {
  position: fixed;
  right: 1rem;
  bottom: 1rem;
  width: 2.75rem;
  height: 2.75rem;
  border-radius: 50%;
  border: 2px solid var(--teal);
  background: var(--white);
  color: var(--navy);
  font-weight: 900;
  cursor: pointer;
  box-shadow: var(--shadow);
}

.back-to-top:hover,
.back-to-top:focus {
  background: var(--teal);
  color: var(--white);
}

@media (max-width: 900px) {
  .hero-grid,
  .sbt-intro,
  .split,
  .grid.two {
    grid-template-columns: 1fr;
  }

  .grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .project-link-grid,
  .photo-grid,
  .image-rail {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .board {
    grid-template-columns: repeat(2, minmax(220px, 1fr));
  }

  .brand-row {
    align-items: flex-start;
    flex-direction: column;
  }

}

@media (max-width: 760px) {
  .nav-desktop {
    display: none;
  }

  .nav-mobile {
    display: block;
    width: 100%;
  }

  .nav-mobile > summary {
    width: 100%;
    justify-content: space-between;
  }

  .nav-mobile-panel {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 0.65rem;
    margin-top: 0.5rem;
    padding: 0.7rem;
    border: 1px solid rgba(255, 255, 255, 0.2);
    background: var(--navy-2);
  }

  .nav-mobile-direct {
    grid-column: 1 / -1;
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 0.4rem;
  }

  .nav-mobile-section {
    min-width: 0;
    padding: 0.45rem;
    border-top: 3px solid var(--teal);
    background: rgba(255, 255, 255, 0.05);
  }

  .nav-mobile-section strong {
    display: block;
    margin: 0.15rem 0.2rem 0.4rem;
    color: #c8dddd;
    font-size: 0.78rem;
    text-transform: uppercase;
  }

  .nav-mobile-section div {
    display: grid;
    gap: 0.25rem;
  }
}

@media (max-width: 820px) {
  .docs-table-wrap {
    overflow-x: visible;
  }

  .docs-table,
  .docs-table thead,
  .docs-table tbody,
  .docs-table tr,
  .docs-table th,
  .docs-table td {
    display: block;
    width: 100%;
  }

  .docs-table thead {
    display: none;
  }

  .docs-table tr {
    border-bottom: 1px solid var(--border);
    padding: 0.8rem;
  }

  .docs-table td {
    border-bottom: 0;
    padding: 0.4rem 0;
  }

  .docs-table td::before {
    content: attr(data-label);
    display: block;
    margin-bottom: 0.15rem;
    color: var(--navy);
    font-size: 0.78rem;
    font-weight: 900;
  }

  .docs-table .download-cell {
    text-align: left;
  }
}

@media (max-width: 620px) {
  .page-shell {
    padding: 1rem;
  }

  .grid,
  .board,
  .project-link-grid,
  .photo-grid,
  .image-rail {
    grid-template-columns: 1fr;
  }

  .hero-panel,
  .hero-image,
  .hero-image img {
    min-height: 18rem;
  }

  .hero-panel h2 {
    font-size: 2.4rem;
  }

  .site-nav {
    width: 100%;
  }

  .nav-mobile-panel {
    grid-template-columns: 1fr;
  }

  .nav-mobile-direct {
    grid-template-columns: 1fr;
  }

  .page-pager {
    flex-direction: column;
  }
}

@media print {
  .site-header,
  .caution-banner,
  .site-footer,
  .page-pager,
  .back-to-top,
  .skip-link,
  .card-link,
  .button-link {
    display: none !important;
  }

  body {
    background: #fff;
    color: #000;
    font-size: 11pt;
  }

  .page-shell {
    max-width: none;
    padding: 0;
  }

  .page-intro h1 {
    font-size: 24pt;
  }

  .band,
  .card,
  .table-wrap,
  .note-box,
  .warning-box {
    border: 1px solid #999;
    box-shadow: none;
    break-inside: avoid;
  }

  table {
    min-width: 0;
    font-size: 9pt;
  }

  th,
  td {
    padding: 5pt;
  }
}
""")

    write("assets/js/app.js", r"""
(function () {
  const topButton = document.querySelector(".back-to-top");
  if (topButton) {
    topButton.addEventListener("click", () => window.scrollTo({ top: 0, behavior: "smooth" }));
  }

  const navGroups = [...document.querySelectorAll(".nav-group")];
  navGroups.forEach((group) => {
    group.addEventListener("toggle", () => {
      if (!group.open) return;
      navGroups.forEach((other) => {
        if (other !== group) other.open = false;
      });
    });
  });

  document.addEventListener("click", (event) => {
    if (event.target.closest(".site-nav")) return;
    navGroups.forEach((group) => { group.open = false; });
  });

  document.addEventListener("keydown", (event) => {
    if (event.key !== "Escape") return;
    navGroups.forEach((group) => { group.open = false; });
  });

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
""")


def write_data() -> None:
    write("data/questions.json", json.dumps(questions, indent=2))
    write("data/tasks.json", json.dumps(tasks, indent=2))
    write("data/docs.json", json.dumps(docs, indent=2))
    write("data/returnables.json", json.dumps(returnables, indent=2))
    write("data/site-photos.json", json.dumps(site_photos, indent=2))
    write("data/vfg-images.json", json.dumps(vfg_images, indent=2))


def write_meta_files() -> None:
    write("favicon.svg", """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="SB">
  <rect width="64" height="64" fill="#102433"/>
  <rect x="8" y="8" width="48" height="48" fill="none" stroke="#c7ad7a" stroke-width="4"/>
  <text x="32" y="39" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#ffffff">SB</text>
</svg>
""")
    write(".gitignore", r"""
# Private/local working folders stay out of the public repo.
RequestDocs/
source-docs/
source_docs/
private/
_private/

# Raw site-meeting recordings stay local until reviewed for publication.
assets/site-audio/

# The public source tender pack is intentionally tracked here.
!tender-documents/
!tender-documents/**

# Local tooling clutter.
.DS_Store
Thumbs.db
__pycache__/
.venv/
node_modules/
tmp/
""")
    write(".nojekyll", "")
    sitemap_urls = "\n".join(
        f"  <url><loc>{esc(SITE_URL + href)}</loc></url>"
        for href, _label in NAV
    )
    write("sitemap.xml", f"""
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{sitemap_urls}
</urlset>
""")
    write("LICENSE.md", """
Copyright (c) 2026 Luke Nathan Hayes. All rights reserved.

No licence is granted to copy, modify, distribute, sublicense, commercially use, or reuse this material without prior written permission from Luke Nathan Hayes.

Authorised project collaborators may review this repository for the limited purpose of exploring and preparing the PDG-20842-1 tender partnership.

Tender source documents, council materials, VFG public website material, and third-party content remain the property of their respective rights holders.
""")
    write("README.md", """
# Windemere skate bowl tender workspace

This is an exploratory tender collaboration workspace for Redland City Council Tender PDG-20842-1, Skate Bowl Refurbishment, Windemere Road Park, Alexandra Hills.

It is not official Redland City Council material. It is not VFG's final tender submission. It is not engineering advice. It is not for construction.

The workspace helps organise tender facts, role boundaries, questions, tasks, draft CAD workflow and tender response thinking for a possible Strange But True x VFG collaboration.

## Public/private caution

The blank/source tender pack is included in `tender-documents/` for easy public review by project direction.

Keep filled returnables, prices, signatures, private contact details, supplier quotes, private evidence and commercial-in-confidence material out of this repository.

The `.gitignore` file blocks private working folders while allowing the published source tender pack.

## Licence

All rights reserved. See `LICENSE.md`.

## Suggested workflow

1. Review the website pages, `tender-documents/` source pack and 360 site record.
2. Capture site-visit answers and update `data/questions.json` and `data/tasks.json`.
3. Confirm role split and role boundaries.
4. Decide bid / no-bid.
5. Draft returnables and concept CAD in a private working area.
6. VFG and relevant specialists review before anything goes to Council.

## Local preview

From this folder, run:

```powershell
python -m http.server 8000
```

Then open:

```text
http://localhost:8000/
```

The site is plain HTML, CSS and JavaScript. There is no frontend build step.

## Rebuild the 360 site record

When new GoPro equirectangular JPG files are added to `assets/img/GoPro360-site-visit/`, run:

```powershell
python tools/build_site_visit_360.py
python tools/build_static_site.py
```

The first command creates lightweight viewer copies, thumbnails and the public photo manifest. The original JPG files remain available for full-resolution download.

## GitHub Pages

The site is designed to publish from the repository root on the `main` branch.
""")


def write_cad_files() -> None:
    cad_readme = """
# CAD workspace notes

This folder is for tender-stage concept drafting support only.

Every drawing or exported sheet should be labelled:

- Tender Concept Only
- Not For Construction
- Subject to Survey
- Subject to RPEQ Certification
- Prepared for exploratory tender partnership discussion

## Inputs needed from VFG

- Hand sketches, preferred elements and rough intent.
- Dimensions, clearances and rideability requirements where known.
- Repair method and construction sequence.
- Example projects, reference photos and lessons learned.

## Inputs needed from site

- Survey, levels and service information.
- Existing bowl geometry.
- Drainage low points.
- Tree/root constraints.
- Shelter, fencing and seating locations.

## Proposed drawing outputs

- Existing conditions / opportunity plan.
- Proposed concept layout plan.
- Repair and scope annotation plan.
- Staging / access / laydown plan.
- Signage / fencing / ancillary works plan.
- Details or sections only where VFG supplies intent and they are labelled concept only.
"""
    layers = """
# CAD layer standard

Use these starting layer names for concept drafting. They are placeholders and should be refined by the design/CAD lead if the project proceeds.

| Layer | Purpose |
| --- | --- |
| EXST_SITE | Existing site boundary and base context |
| EXST_BOWL | Existing bowl geometry |
| EXST_SHELTER | Existing shelter / shade context |
| EXST_FENCE | Existing fencing |
| DEMO_REMOVALS | Possible removals, subject to confirmation |
| REPAIR_CRACKS | Crack and joint repair annotations |
| REPAIR_COPING | Coping repair annotations |
| NEW_SKATE_ELEMENTS | Proposed street/progression elements |
| NEW_SEATING | Seating replacements or refresh |
| NEW_FENCING | Fencing / control fence works |
| NEW_SIGNAGE | Signage locations and notes |
| DRAINAGE_REVIEW | Drainage observations and review areas |
| TREE_TPZ | Tree protection zones |
| KOALA_HABITAT | Koala habitat / environmental control notes |
| ACCESS_STAGING | Access and staging paths |
| LAYDOWN | Laydown and compound ideas |
| ANNO_TEXT | Annotation text |
| ANNO_DIM | Dimensions |
| HOLD_POINTS | Hold points and review gates |
"""
    titleblock = """
# Titleblock notes

Suggested titleblock labels:

- Tender Concept Only
- Not For Construction
- Subject to Survey
- Subject to Service Location
- Subject to Structural Investigation
- Subject to RPEQ Certification
- Subject to RCC Review
- Prepared from VFG supplied design intent
- Prepared for exploratory tender partnership discussion

Suggested filenames:

- PDG20842_Windemere_Concept_ExistingConditions_v01.dwg
- PDG20842_Windemere_Concept_Layout_v01.dwg
- PDG20842_Windemere_RepairScope_v01.dwg
- PDG20842_Windemere_StagingAccess_v01.dwg

Do not call a drawing final, certified or for construction unless the proper project team and certification pathway have confirmed it.
"""
    write("cad/README.md", cad_readme)
    write("cad/layers.md", layers)
    write("cad/titleblock-notes.md", titleblock)

    layer_names = [
        "EXST_SITE", "EXST_BOWL", "EXST_SHELTER", "EXST_FENCE", "DEMO_REMOVALS",
        "REPAIR_CRACKS", "REPAIR_COPING", "NEW_SKATE_ELEMENTS", "NEW_SEATING",
        "NEW_FENCING", "NEW_SIGNAGE", "DRAINAGE_REVIEW", "TREE_TPZ", "KOALA_HABITAT",
        "ACCESS_STAGING", "LAYDOWN", "ANNO_TEXT", "ANNO_DIM", "HOLD_POINTS",
    ]
    dxf_parts = ["0", "SECTION", "2", "HEADER", "9", "$ACADVER", "1", "AC1009", "0", "ENDSEC"]
    dxf_parts += ["0", "SECTION", "2", "TABLES", "0", "TABLE", "2", "LAYER", "70", str(len(layer_names) + 1)]
    dxf_parts += ["0", "LAYER", "2", "0", "70", "0", "62", "7", "6", "CONTINUOUS"]
    for i, name in enumerate(layer_names, start=1):
        dxf_parts += ["0", "LAYER", "2", name, "70", "0", "62", str((i % 7) + 1), "6", "CONTINUOUS"]
    dxf_parts += ["0", "ENDTAB", "0", "ENDSEC"]
    dxf_parts += ["0", "SECTION", "2", "ENTITIES"]
    dxf_parts += [
        "0", "TEXT", "8", "ANNO_TEXT", "10", "0", "20", "130", "40", "5",
        "1", "PDG-20842-1 Windemere Road Park - Tender Concept Only / Not For Construction",
        "0", "TEXT", "8", "ANNO_TEXT", "10", "0", "20", "120", "40", "3",
        "1", "Placeholder seed DXF. Not survey accurate. Subject to survey, services, VFG intent and RPEQ certification.",
        "0", "LINE", "8", "EXST_SITE", "10", "0", "20", "0", "11", "160", "21", "0",
        "0", "LINE", "8", "EXST_SITE", "10", "160", "20", "0", "11", "160", "21", "100",
        "0", "LINE", "8", "EXST_SITE", "10", "160", "20", "100", "11", "0", "21", "100",
        "0", "LINE", "8", "EXST_SITE", "10", "0", "20", "100", "11", "0", "21", "0",
        "0", "CIRCLE", "8", "EXST_BOWL", "10", "55", "20", "55", "40", "22",
        "0", "CIRCLE", "8", "EXST_BOWL", "10", "105", "20", "55", "40", "20",
        "0", "LINE", "8", "DRAINAGE_REVIEW", "10", "15", "20", "22", "11", "145", "21", "22",
        "0", "TEXT", "8", "DRAINAGE_REVIEW", "10", "18", "20", "26", "40", "3",
        "1", "Drainage/pooling review area - confirm on site",
        "0", "TEXT", "8", "NEW_SKATE_ELEMENTS", "10", "40", "20", "8", "40", "3",
        "1", "Possible compact progression zone - VFG intent required",
    ]
    dxf_parts += ["0", "ENDSEC", "0", "EOF"]
    write("cad/PDG20842_Windemere_Concept_Seed_NotForConstruction.dxf", "\n".join(dxf_parts))


def write_pages() -> None:
    homepage = f"""
    <section class="hero-grid">
      <div class="hero-panel">
        <div>
          <h2>Decide clearly before the tender sprint.</h2>
          <p>This workspace turns the tender pack into a practical conversation tool for Luke, Paolo and Kieran. It supports a calm bid/no-bid decision, then a compliant response only if the partnership feels workable.</p>
        </div>
        <div class="quick-status">
          {badge("Exploratory", "gum")}
          {badge("Not for construction", "warning")}
          {badge("All rights reserved", "dark")}
        </div>
      </div>
      <figure class="hero-image">
        <img src="assets/img/site-photos/windemere-site-01.jpg" alt="Actual Appendix D site photo showing water pooling near the skate bowl.">
        <figcaption>Actual Appendix D site photo, 02 June 2026. The visible pooling is a key site-visit verification issue.</figcaption>
      </figure>
    </section>

    <section class="section">
      <h2>Dashboard</h2>
      <div class="grid">
        {card("Tender snapshot", "PDG-20842-1 asks for design-and-construct refurbishment of the Windemere Road Park skate bowl, including repair, new elements, ancillary works, certification and management plans.", "Tender fact", "pages/tender-overview.html")}
        {card("Project Brief coverage", "The first audit says the workspace covers the tender skeleton, but several Project Brief controls still need a stronger register or VFG/specialist confirmation.", "New audit", "pages/project-brief-coverage.html")}
        {card("Site visit record", "The mandatory inspection was attended on 15 July 2026. Ten geotagged GoPro 360 captures now record the bowls, surfaces, fencing, shelter and surrounding park.", "New field evidence", "pages/site-visit-360.html")}
        {card("Actual site photos", "Appendix D photos are now included as web images so drainage, cracking, debris, shelter and fencing context can be reviewed directly.", "Source imagery", "pages/site-photos.html")}
        {card("Partnership status", "Luke, Paolo and Kieran are testing fit. The workspace should help the team proceed, pause or no-bid respectfully.", "Exploratory", "pages/partnership.html")}
        {card("Decision gate", "Proceed only if VFG can lead the technical/design/build response and the specialist pathway is credible.", "Decision point", "pages/decision-gate.html")}
        {card("VFG capability fit", "Public VFG material maps well to consulting, design, construction, maintenance, repairs and skatepark-specific delivery evidence.", "Needs VFG review", "pages/vfg-capability-map.html")}
        {card("Luke possible contribution", "Tender narrative, information design, role clarity, local benefit framing, task tracking and concept drafting from supplied intent.", "Possible role", "pages/strange-but-true-role.html")}
        {card("Key tender risks", "Certification pathway, BOQ/pricing, drainage, role boundaries, non-conforming returnables and contract risk need early attention.", "Open risk", "pages/risk-and-assumptions.html")}
        {card("Open questions", "Seed questions are ready for the site visit and can be edited in data/questions.json.", "Register", "pages/questions-register.html")}
        {card("Next actions", "Review the site-visit evidence, capture VFG repair and concept notes, collect capability evidence, review the BOQ structure and decide whether the partnership should bid.", "Task board", "pages/task-board.html")}
      </div>
    </section>

    <section class="section band tint">
      <h2>Keep this clean</h2>
      <p>The public version is an organising layer, not the tender submission. Blank/source tender documents, actual site photos and VFG public images are included for context. Prices, signatures, private contact details, filled returnables and final tender material stay out of GitHub Pages unless the team agrees otherwise.</p>
    </section>
    """
    write("index.html", layout("index.html", "Exploratory tender dashboard", "A practical workspace for understanding the Redland skate bowl tender, testing the partnership fit, and keeping the response pathway honest.", homepage, body_class="home"))

    tender_overview = f"""
    <section class="section split">
      <div class="band">
        <h2>What RCC is asking for</h2>
        <p>This appears to be more than a simple surface repair. The tender asks for a design-and-construct response covering investigation, design, reporting, labour, plant, materials, construction, supervision and certification for the Windemere Road Park skate bowl refurbishment.</p>
        <p>The work includes evaluating and repairing the existing skate bowl, incorporating new skatepark elements, replacing or refreshing ancillary items such as seating, signage, bollards and fencing, and handling concrete, earthworks, landscaping or turf where required.</p>
      </div>
      <aside class="warning-box">
        <h2>Dates to treat as current</h2>
        {list_items([
            "Tender closes at 2:00 pm on 6 August 2026.",
            "Mandatory site inspection is listed in Addendum 1 as 10:00 am Wednesday 15 July 2026.",
            "RSVP is listed as due by 2:00 pm Tuesday 14 July 2026 to pdgprocurement@redland.qld.gov.au.",
            "Project completion is noted as 30 March 2027.",
            "Addendum 1 overrides the earlier site inspection and closing details.",
        ])}
      </aside>
    </section>

    <section class="section grid two">
      <article class="card">
        <h3>What the audit says</h3>
        <p>Appendix C rates Windemere Road Park as condition rating 3 - Fair. The facility has two large open bowl structures suited to intermediate and advanced transition riding. The primary bowl structures are described as structurally sound and serviceable, but the audit notes worn surfaces, significant cracks and minor surface hazards.</p>
      </article>
      <article class="card">
        <h3>What the photos suggest</h3>
        <p>The June 2026 site photos show standing water or pooling, debris, graffiti, cracking and the surrounding shelter and fencing context. Drainage should be treated as a verification issue because the audit says no water was seen pooling at the time of inspection.</p>
      </article>
    </section>

    <section class="section band">
      <h2>Actual site-photo evidence</h2>
      <p>The images below are extracted from Appendix D and resized for the web. They should guide site-visit questions about drainage, cracking, debris, shelter, fencing and surrounding park context.</p>
      <div class="image-rail">
        <img src="../assets/img/site-photos/windemere-site-01.jpg" alt="Actual Appendix D photo showing water pooling near the skate bowl.">
        <img src="../assets/img/site-photos/windemere-site-09.jpg" alt="Actual Appendix D close photo showing debris and surface marks.">
        <img src="../assets/img/site-photos/windemere-site-13.jpg" alt="Actual Appendix D close photo showing cracking in concrete.">
        <img src="../assets/img/site-photos/windemere-site-07.jpg" alt="Actual Appendix D photo showing shelter and seating context.">
      </div>
      <p><a class="button-link" href="site-photos.html">Open the full site photo gallery</a></p>
    </section>

    <section class="section band">
      <h2>Evaluation weighting</h2>
      {table(["Criteria", "Weighting", "Working note"], [
        ["Local Business and Benefit", "15%", "Needs a real Redlands/SEQ benefit story that VFG can deliver."],
        ["Tendered Sum", "30%", "VFG-led. Do not put prices in this public workspace."],
        ["Proposed Concept Design", "10%", "Needs VFG design intent and careful concept-only labelling."],
        ["Experience and Operational Capability", "30%", "VFG project evidence, team capability and referees are likely central."],
        ["Program of Works", "15%", "Construction sequencing and methodology should be VFG-led."],
        ["Accreditation Systems and Management Plans", "Mandatory", "QMS, WHSMP and SSEMP must be checked carefully."],
      ])}
    </section>

    <section class="section band tint">
      <h2>Things not to miss</h2>
      {list_items([
        "Mandatory site inspection attendance and RSVP.",
        "Signed Addendum 1 returned with the tender documents.",
        "Section B returnable schedules completed, signed and lodged.",
        "BOQ and tendered sum completed outside this public workspace.",
        "Certificates of currency, insurances, licences and management plans checked.",
        "RPEQ, survey, service locating, Safety in Design, as-constructed, ADAC and Form 16 pathway confirmed.",
        "Project Brief coverage page reviewed for the deeper codes, controls, hold points and handover requirements.",
      ])}
    </section>
    """
    write("pages/tender-overview.html", layout("pages/tender-overview.html", "Tender overview", "A plain-English summary of the tender, the source-pack priorities and the dates that should guide the next conversation.", tender_overview))

    site_questions = [q["question"] for q in questions]
    site_visit = f"""
    <section class="section band">
      <h2>Inspection record</h2>
      <p><strong>Purpose:</strong> test the site conditions, repair questions and partnership fit against the real place.</p>
      <p><strong>Recorded event:</strong> the mandatory site inspection at Windemere Road Park, 42-46 Windemere Road, Alexandra Hills QLD 4161, was attended on Wednesday 15 July 2026.</p>
      <p><strong>Field imagery:</strong> ten GoPro 360 photographs were captured between 9:12 am and 9:14 am before the 10:00 am inspection. Camera GPS is useful for orientation but is not survey-grade.</p>
      <div class="label-strip">{badge("Inspection attended", "gum")}{badge("10 new 360 views", "dark")}{badge("Not survey-grade", "warning")}</div>
      <p><a class="button-link" href="site-visit-360.html">Open the 360 site record</a></p>
    </section>

    <section class="section">
      <h2>Questions to ask on site</h2>
      <div class="band">{list_items(site_questions)}</div>
    </section>

    <section class="section grid two">
      <article class="card"><h3>Observations</h3><p>Condition, cracking, surface levels, coping, water marks, graffiti, debris, access, shelter, fencing, seating, signs and vegetation.</p></article>
      <article class="card"><h3>VFG practical ideas</h3><p>Repair method, rideability, sequencing, feature options, what is realistic at tender stage and what needs specialist confirmation.</p></article>
      <article class="card"><h3>Luke translation / CAD tasks</h3><p>Sketch capture, concept-only drawings, compliance cross-reference, questions register and draft narrative tasks.</p></article>
      <article class="card"><h3>Tender questions</h3><p>Returnables, exclusions, assumptions, risks, no-bid triggers and evidence needed before submission.</p></article>
      <article class="card"><h3>Risks</h3><p>Drainage, certification, BOQ, site access, environmental controls, role blur and tender timing.</p></article>
      <article class="card"><h3>Decisions</h3><p>Proceed, pause or no-bid. Confirm who owns each next action and who must review it.</p></article>
    </section>
    """
    write("pages/site-visit.html", layout("pages/site-visit.html", "Site visit record", "The mandatory inspection record, field questions and follow-up prompts for the exploratory tender partnership.", site_visit))

    site_visit_360 = f"""
    <section class="site-360-experience" data-site-360 data-source="../data/site-visit-360.json">
      <header class="site-360-toolbar">
        <div class="site-360-title-block">
          <span data-view-count>View 01 of 10</span>
          <strong data-view-title>Windemere site view 01</strong>
        </div>
        <div class="site-360-step-controls" aria-label="Panorama selection">
          <button class="site-360-button" type="button" data-previous-view>Previous</button>
          <button class="site-360-button" type="button" data-next-view>Next</button>
        </div>
      </header>

      <div class="site-360-stage" data-sphere-stage aria-label="Interactive 360 site photograph">
        <div class="site-360-loading" data-viewer-loading role="status">Loading 360 view...</div>
      </div>

      <footer class="site-360-footer">
        <div class="site-360-meta">
          <span data-capture-time>15 July 2026</span>
          <a data-location-link target="_blank" rel="noopener noreferrer">Camera GPS</a>
          <span>5760 x 2880 original</span>
        </div>
        <div class="site-360-actions">
          <button class="site-360-button primary" type="button" data-save-view>Save view PNG</button>
          <button class="site-360-button" type="button" data-copy-view>Copy view reference</button>
          <a class="site-360-button" data-download-original download>Download original</a>
        </div>
      </footer>
      <p class="site-360-status" data-viewer-status aria-live="polite">Preparing site record...</p>
    </section>

    <section class="site-360-index section" aria-label="360 capture index">
      <div class="site-360-trail-panel">
        <div>
          <p class="kicker">Camera GPS / not survey-grade</p>
          <h2>Capture map</h2>
          <p>Ten camera-GPS positions around the existing bowls, recorded immediately before the mandatory inspection.</p>
        </div>
        <div class="site-360-trail" data-capture-trail aria-label="Google Maps satellite screenshot with relative camera-GPS photo points"></div>
      </div>
      <div class="site-360-thumbnails" data-view-thumbnails aria-label="360 photograph thumbnails"></div>
    </section>

    <section class="section band tint">
      <h2>Field evidence boundary</h2>
      <p>These photographs are a visual record of conditions seen on 15 July 2026. They help with tender questions and concept discussion, but they do not replace survey, service locating, structural inspection, engineering advice or the tender documents.</p>
      <details class="site-360-flat-details">
        <summary>Open selected equirectangular strip</summary>
        <div class="site-360-flat-strip"><img data-flat-view alt="Selected Windemere 360 photograph as a flat equirectangular strip"></div>
      </details>
    </section>
    """
    write(
        "pages/site-visit-360.html",
        layout(
            "pages/site-visit-360.html",
            "360 site record",
            "A geotagged, look-around record captured at Windemere Road Park on the morning of the mandatory tender inspection, 15 July 2026.",
            site_visit_360,
            body_class="site-360-page",
            extra_head="""
  <link rel="stylesheet" href="../assets/vendor/pannellum/pannellum.css">
  <link rel="stylesheet" href="../assets/css/site-visit-360.css">
            """.strip(),
            extra_scripts="""
  <script src="../assets/vendor/pannellum/pannellum.js"></script>
  <script src="../assets/js/site-visit-360.js" defer></script>
            """.strip(),
        ),
    )

    site_photos_page = f"""
    <section class="section band">
      <h2>Appendix D extracted images</h2>
      <p>These are the actual site-photo images extracted from Appendix D - Site Photos - 02 June 2026 and resized for GitHub Pages. They are included as working visual context for the site visit, concept discussion and tender questions.</p>
      <p>The source PDF is also downloadable from the document register. This page gives the team the practical visual evidence without asking everyone to dig through the PDF pack.</p>
      <div class="label-strip">{badge("Actual tender-pack imagery", "gum")}{badge("Working evidence", "dark")}{badge("Not design recommendation", "warning")}</div>
    </section>

    <section class="section">
      <h2>Full photo set</h2>
      {photo_grid(site_photos)}
    </section>

    <section class="section band tint">
      <h2>What to check on site</h2>
      {list_items([
        "Whether the visible water pooling is drainage design, maintenance, recent rain, low spots or a mix.",
        "Which surface cracks and joints match the Appendix C priority repair thresholds.",
        "Whether debris and organic build-up are isolated maintenance issues or signal ongoing water/shelter/vegetation interactions.",
        "How the shelter, fencing, seating and surrounding trees affect access, staging, safety and user experience.",
        "Which conditions need survey, levels, service locating, structural review or RPEQ input before drawings get serious.",
      ])}
    </section>
    """
    write("pages/site-photos.html", layout("pages/site-photos.html", "Actual site photos", "The Appendix D site photos brought into the workspace as real visual evidence, not just text summary.", site_photos_page))

    partnership = f"""
    <section class="section band">
      <h2>Working frame</h2>
      <p>We are testing fit, not assuming agreement. The useful question is whether the group can prepare a strong, compliant and deliverable tender without blurring roles or overpromising.</p>
      <p>VFG brings skatepark design, build and repair experience. Luke / Strange But True may bring social and digital civic planning, tender narrative support, information design, community benefit framing and CAD/documentation support within clear limits.</p>
    </section>

    <section class="section split">
      <div class="band">
        <h2>Possible partnership logic</h2>
        {list_items([
            "VFG leads technical skatepark design, repair method, construction delivery and pricing.",
            "Luke supports information organisation, tender language, local benefit framing, meeting structure, question tracking and concept drafting from supplied intent.",
            "Specialists confirm engineering, certification, survey, service locating, statutory approvals and anything outside either party's direct competence.",
            "Everyone keeps the option to pause or no-bid if the risks are not manageable.",
        ])}
      </div>
      <aside class="note-box">
        <h2>Conversation note to confirm</h2>
        <p>Paolo mentioned that skatepark tenders of this kind may often attract only three or four applicants and that VFG works nationally. Treat this as field context to confirm, not tender evidence.</p>
      </aside>
    </section>
    """
    write("pages/partnership.html", layout("pages/partnership.html", "Exploratory partnership", "A respectful frame for deciding whether Strange But True and VFG should proceed together.", partnership))

    vfg = f"""
    <section class="section band">
      <h2>Public VFG positioning to map</h2>
      <p>VFG's public website describes the company as a skateboarder-owned and run skatepark design and construct company providing action sport facilities and public spaces. Its services page covers consulting, design, construction and maintenance, including safety and maintenance audits, repair solutions and in-house concrete grinding.</p>
      <p>Use these as public source leads only. VFG should confirm the exact claims, evidence, project examples and referees used in any tender response.</p>
      <p><a href="https://www.skateparkconstruction.com.au/" rel="noopener">VFG home</a> | <a href="https://www.skateparkconstruction.com.au/services" rel="noopener">VFG services</a> | <a href="https://www.skateparkconstruction.com.au/projects" rel="noopener">VFG projects</a></p>
    </section>

    <section class="section">
      <h2>Capability fit map</h2>
      {table(["VFG public capability lead", "Tender-fit area", "Evidence to request from VFG"], [
        ["Consulting / design / construction / maintenance", "Design-and-construct scope, practical repair method and construction methodology.", "Relevant project examples, team roles and delivery method."],
        ["Safety and maintenance audits", "Condition assessment, defect prioritisation and repair recommendations.", "Audit examples or maintenance/refurbishment experience."],
        ["Innovative repair solutions", "Crack, chip, joint, coping and surface repair approach.", "Method statements, photos, lessons learned and product/system notes."],
        ["In-house concrete grinding", "Priority 1 audit response for height irregularities and surface hazards.", "Process, plant, finish quality and risk controls."],
        ["Australia-wide project delivery", "Operational capability and program confidence.", "Comparable public skatepark projects and referees."],
        ["Skateboarder-owned practical design sensibility", "Rideability, terrain diversity and feature selection.", "Examples of bowls, street elements and progression layouts."],
      ])}
    </section>
    <section class="section band tint">
      <h2>Public project examples to request evidence for</h2>
      <p>VFG's public projects page includes examples such as Black Head NSW 2025, Newcastle Beach NSW current, Boorowa 2021, Barham 2019, Finley 2019, Howlong 2018 and Murwillumbah 2016. Treat these as source leads only. The tender response should use VFG-approved project descriptions, scopes, referees and permissions.</p>
    </section>
    <section class="section">
      <h2>VFG public imagery</h2>
      <p>These images are taken from VFG's public website and project pages so the capability discussion can use real VFG visual context. They should be replaced, approved or refined by VFG before any final tender material is prepared.</p>
      {photo_grid(vfg_images)}
    </section>
    """
    write("pages/vfg-capability-map.html", layout("pages/vfg-capability-map.html", "VFG capability map", "A source-aware way to connect VFG's public capability signals to the tender response, pending VFG confirmation.", vfg))

    sbt = f"""
    <section class="section sbt-intro">
      <div class="sbt-logo-panel">
        <img src="../assets/img/sbt/sbt-icon.webp" alt="Strange But True neon logo.">
        <div class="sbt-actions">
          <a class="button-link" href="https://auraofintelligence.github.io/strange-but-true/" rel="noopener">Open Strange But True</a>
          <a class="button-link secondary" href="https://auraofintelligence.github.io/strange-but-true/community-ledger.html" rel="noopener">Open community ledger</a>
        </div>
      </div>
      <div>
        <h2>Public-safe civic planning support, not skatepark certification.</h2>
        <p>Luke / Strange But True can help turn a messy tender pack into a clear working system: source summaries, task boards, question registers, public/private boundaries, local benefit framing and draft narrative that VFG can review.</p>
        <p>The fit here is practical translation. VFG holds the skatepark expertise. Specialists hold engineering, certification and construction compliance. Strange But True can help the team keep evidence, story, roles and next actions readable.</p>
      </div>
    </section>

    <section class="section band">
      <h2>Selective project-family references</h2>
      <p>The Community Ledger has many public project cards. For this tender workspace, only the closest lanes are referenced: tender readiness, public-space activation, event planning, local capability and grant-to-infrastructure thinking.</p>
      <div class="project-link-grid">
        <a class="project-link-card" href="https://auraofintelligence.github.io/straddie-tenders-lab/" rel="noopener"><span>Tenders</span><strong>Straddie Tenders Lab</strong><p>Official-source watching, bid readiness, role clarity and local-capability pathways.</p></a>
        <a class="project-link-card" href="https://auraofintelligence.github.io/ballow-road-sand-screen-hub/" rel="noopener"><span>Public space</span><strong>Ballow Road Sand & Screen Hub</strong><p>Public-space activation, youth roles, events, sport, screen culture and source trails.</p></a>
        <a class="project-link-card" href="https://auraofintelligence.github.io/ready-set-co-op-trust-hub/" rel="noopener"><span>Trust</span><strong>Ready S.E.T. Co-op Trust Hub</strong><p>Practical work pathways, co-working, public/private boundaries and local support roles.</p></a>
        <a class="project-link-card" href="https://auraofintelligence.github.io/quandamooka-country-events-engine/" rel="noopener"><span>Events</span><strong>Quandamooka Country Events Engine</strong><p>Event builders, approvals thinking, public notices, supply lanes and planning flows.</p></a>
        <a class="project-link-card" href="https://auraofintelligence.github.io/amity-outdoor-fitness-grant/" rel="noopener"><span>Grant logic</span><strong>Amity Outdoor Fitness</strong><p>Grant-facing public infrastructure framing, evidence, site checks and support pathways.</p></a>
        <a class="project-link-card" href="https://auraofintelligence.github.io/strange-but-true/community-ledger.html" rel="noopener"><span>Ledger</span><strong>Community Ledger</strong><p>The wider public project index remains available without importing every card into this tender page.</p></a>
      </div>
    </section>

    <section class="section grid two">
      <article class="card"><h3>Possible contribution</h3>{list_items([
        "Translate practical site experience into tender-friendly design language.",
        "Build and maintain this repo/workspace.",
        "Create compliance matrix and task tracking.",
        "Help draft Returnable I concept explanation and supporting diagrams.",
        "Help draft local benefit/social benefit narrative.",
        "Prepare non-certified concept drawings or AutoCAD-ready drafting from VFG sketches/markups.",
        "Organise document naming, revision control and cross-referencing.",
        "Produce meeting agendas, question registers and decision logs.",
        "Draft plain-speaking community activation ideas if appropriate.",
      ])}</article>
      <article class="card"><h3>Requires VFG / specialist confirmation</h3>{list_items([
        "Skate geometry and rideability decisions.",
        "Structural repair design.",
        "Engineering, RPEQ certification, geotechnical advice, Form 15/Form 16.",
        "AS EN 14974 compliance sign-off.",
        "Construction method and plant selection.",
        "Pricing, BOQ and tendered sum.",
        "WHSMP, SSEMP and QMP final acceptance.",
        "Permits, legal and contractual compliance.",
        "Final tender sign-off.",
      ])}</article>
    </section>
    """
    write("pages/strange-but-true-role.html", layout("pages/strange-but-true-role.html", "Strange But True and Luke's role", "A selective, boundary-aware outline of how Luke can support the tender workspace without stepping into skatepark certification or construction responsibility.", sbt))

    boundaries = f"""
    <section class="section grid two">
      <article class="card"><h3>Luke can support</h3><p>Organisation, meeting structure, compliance tracking, information design, source summaries and tender drafting support.</p></article>
      <article class="card"><h3>Luke can draft</h3><p>Plain-English narratives, local benefit framing, question registers, decision logs and draft response outlines for review.</p></article>
      <article class="card"><h3>Luke can draw concept / CAD from supplied intent</h3><p>Concept-only plans, annotations and AutoCAD-ready drafting from VFG sketches or markups, with clear caveats.</p></article>
      <article class="card"><h3>Luke cannot certify</h3><p>Luke is not the engineer, RPEQ, building certifier, surveyor, lawyer, WHS principal contractor or skatepark contractor.</p></article>
    </section>

    <section class="section band">
      <h2>Tender language that needs specialist sign-off</h2>
      {list_items([
        "Structural adequacy and repair design.",
        "Drainage design and levels.",
        "RPEQ certification, Form 15/Form 16 and as-constructed obligations.",
        "AS EN 14974 compliance or other technical standards compliance.",
        "Construction methodology, plant selection, WHS, environmental controls and quality systems.",
        "Tendered sum, BOQ assumptions, exclusions and commercial risk.",
      ])}
    </section>

    <section class="section warning-box">
      <h2>Specialist standard to check</h2>
      <p><strong>AS EN 14974:2021 - Skateparks, safety requirements and test methods</strong> is listed by Standards Australia as the current skatepark safety standard. The store page should be checked by VFG or the design/certification lead before anyone buys it.</p>
      <p>Standards Australia pricing checked 8 July 2026: Web Reader 1 licence AUD $154.97 incl. GST; hard copy AUD $172.02 incl. GST. Prices can change, and VFG or the specialist consultant may already have access.</p>
      <p><a class="button-link" href="https://store.standards.org.au/product/as-en-14974-2021" rel="noopener">Open Standards Australia product page</a></p>
    </section>

    <section class="section band tint">
      <h2>Drawing labels</h2>
      {list_items([
        "Tender Concept Only.",
        "Prepared from VFG supplied design intent.",
        "Not for Construction.",
        "Subject to survey, service location, structural investigation, RPEQ certification and RCC review.",
      ])}
    </section>
    """
    write("pages/role-boundaries.html", layout("pages/role-boundaries.html", "Role boundaries", "A clear, humble boundary page so the tender support stays practical and honest.", boundaries))

    brief_covered_rows = [
        ["Tender admin and source pack", "Document register, ZIP download, addendum notes and site map are in place.", badge("Covered", "gum"), "Keep current if RCC issues further addenda."],
        ["Returnables A-L", "Section B returnables are mapped in plain English with likely owners.", badge("Covered", "gum"), "Still requires filled private forms and VFG evidence."],
        ["Role boundaries", "Luke/VFG/specialist boundaries are explicit, including AS EN 14974 and RPEQ limits.", badge("Covered", "gum"), "Good public-facing guardrail."],
        ["Site photos and audit issues", "Appendix D images and Appendix C audit themes are visible for site discussion.", badge("Covered", "gum"), "Need VFG to convert observations into technical response."],
        ["Main design stages", "Stage 1-4, RPEQ, permits, service locating, Safety in Design and ADAC/Form 16 are in the compliance matrix.", badge("Covered at high level", "gum"), "High-level only, not a full deliverables register yet."],
        ["Public/private separation", "Pricing, signatures, filled returnables and private submission material are clearly excluded from the public site.", badge("Covered", "gum"), "Keep this discipline."],
    ]

    brief_thin_rows = [
        ["Codes governing work", "The site mentions AS EN 14974 and specialist standards, but the full codes list was not yet tracked.", badge("Thin", "dark"), "Added a codes register below. VFG/specialist must confirm applicability."],
        ["Cultural heritage duty of care", "Project Brief requires ACHA duty of care, procedures, stop-work response and staff acknowledgement.", badge("Thin", "dark"), "Needs a named contractor-side action."],
        ["Design drawing and data standards", "CAD page exists, but AS1100, A3/A1 title block, DWG/xref packs, 12D and RCC coordinate requirements need stronger treatment.", badge("Thin", "dark"), "Add to CAD workflow before drafting final outputs."],
        ["Permit and application pathway", "Permits are noted, but the detailed permit report, applicant/landowner confirmation, lodgement, fees and hold points need a checklist.", badge("Thin", "dark"), "VFG/specialist owned."],
        ["SSQMP, WHSMP and SSEMP", "Management plans are visible as mandatory, but the Project Brief lists contents, examples, final acceptance and on-site storage requirements.", badge("Thin", "dark"), "Needs plan evidence pack from VFG."],
        ["Koala habitat and environmental controls", "Risk page mentions it, but the stop-work triggers and Redlands Wildlife Rescue contact are not yet unpacked.", badge("Thin", "dark"), "Add to SSEMP questions."],
        ["Wayfinding and construction signage", "Appendix B is downloadable, but the site does not yet have a wayfinding/signage checklist.", badge("Thin", "dark"), "Use RCC manual plus Project Brief public notification section."],
        ["Fencing and site security", "Appendix E is downloadable, but temporary fencing, no-advertising rule and control-fence details are not mapped.", badge("Thin", "dark"), "Add construction controls if bidding proceeds."],
        ["Practical completion and handover", "Final deliverables are mentioned, but the full hard copy/electronic copy, manuals, warranties, Form 15/16/21 and as-constructed detail is not fully itemised.", badge("Thin", "dark"), "Needs a closeout checklist."],
    ]

    brief_missing_rows = [
        ["Detailed Project Brief clause register", "The current matrix is useful but not clause-by-clause.", badge("Missing", "warning"), "Create only if the team proceeds to serious submission work."],
        ["Technical data sheet and warranty register", "Project Brief calls out product data sheets, manuals, guarantees, warranties and maintenance schedules.", badge("Missing", "warning"), "VFG/suppliers to provide."],
        ["Design option comparison report", "If multiple design options are offered, the brief asks for limitations, benefits and suitability comparison.", badge("Missing", "warning"), "Needed if Options A/B/C stay in play."],
        ["Testing and inspection register", "Brief includes tests, hold points, inspections, notices and potential SAA/BSI test requirements.", badge("Missing", "warning"), "Specialist/contractor register."],
        ["Dilapidation survey method detail", "Pre/post survey is listed, but the crack gauges, photos, adjoining areas and endorsed copies are not fully broken out.", badge("Missing detail", "warning"), "Survey/contractor owned."],
        ["Laydown, visual impact, noise and traffic controls", "Brief includes detailed site rules, delivery timing, parking, footpath signage and water tanker filling station rules.", badge("Missing", "warning"), "Construction methodology/WHSMP input."],
        ["Turf, fireweed and tree protection detail", "Brief includes turf supply/placement, maintenance period, fireweed guarantee and AS4970 tree protection zones.", badge("Missing detail", "warning"), "Landscape/specialist input."],
        ["Defects and final completion pathway", "52-week defects period and final certificate process need their own handover/closeout notes.", badge("Missing detail", "warning"), "Contractor/program owner."],
    ]

    code_rows = [
        ["Aboriginal Cultural Heritage Act 2003", "Duty of care, staff procedures, stop-work response and notification pathway.", "Project Brief section 4", badge("Needs owner", "warning")],
        ["AS EN 14974:2021 Skateparks", "Skatepark safety requirements and test methods.", "Project Brief sections 3 and 1", badge("Specialist", "warning")],
        ["Building Act 1975 and building codes", "Building application, decision notices, certification and permits.", "Project Brief sections 3, 6.3 and 12", badge("Specialist", "warning")],
        ["Queensland Environmental Protection Act 1994 and Regulations 2008", "SSEMP, environmental due diligence and harm controls.", "Project Brief sections 3 and 7.3", badge("Plan evidence", "dark")],
        ["Work Health and Safety Act 2011 and Regulation 2011", "Principal Contractor duties, WHSMP, PPE, site traffic and high-risk work controls.", "Project Brief sections 3 and 7.2", badge("VFG / contractor", "dark")],
        ["AS4970-2009 Protection of trees on development sites", "Tree protection zones, restricted activities and arborist advice.", "Project Brief sections 3 and 11.9", badge("Needs detail", "warning")],
        ["AS1428 Design for access and mobility", "Access and mobility implications for public use and paths.", "Project Brief section 3", badge("Needs review", "warning")],
        ["AS1726 Geotechnical Site Investigations", "Geotech investigations and testing for design certification.", "Project Brief sections 3 and 6.1", badge("Specialist", "warning")],
        ["AS 4685 SET:2021 Playground equipment and surfacing Set", "Surfacing/play equipment relevance to be confirmed for skatepark elements.", "Project Brief section 3", badge("Needs review", "warning")],
        ["AS 4419-2003 Soils for Landscaping and Garden Use", "Topsoil and landscape soil suitability.", "Project Brief section 3 and landscape works", badge("Needs detail", "warning")],
        ["AS 1289.D1.1-1977 Methods of Testing Soil for Engineering Purposes", "Soil testing method reference.", "Project Brief section 3", badge("Specialist", "warning")],
        ["AS 4454-2012 Composts, Soil Conditioners and Mulches", "Landscape material quality.", "Project Brief section 3", badge("Needs detail", "warning")],
        ["AS 2303:2018 Tree Stock for Landscaping Use", "Tree stock quality if planting is required.", "Project Brief section 3", badge("Needs detail", "warning")],
        ["Plumbing and Drainage Act 2018", "Drainage/plumbing permits and compliance pathway.", "Project Brief section 3", badge("Specialist", "warning")],
        ["Standards Association of Australia codes and guidelines", "Any other applicable SAA standards for components of the work.", "Project Brief section 3", badge("Needs specialist review", "warning")],
        ["Industry regulations, manuals and codes of practice", "Recognised manuals, codes and supplier requirements.", "Project Brief section 3", badge("Needs register", "warning")],
        ["Product technical data sheets and warranties", "Product datasheets, limitations, benefits, suitability and warranty requirements.", "Project Brief section 3 and 12", badge("Missing register", "warning")],
        ["Redland City Plan policies, infrastructure plans, codes, schedules and standard drawings", "Local government design, ASCON and infrastructure requirements.", "Project Brief sections 3 and 12", badge("Needs review", "warning")],
    ]

    brief_coverage = f"""
    <section class="section warning-box">
      <h2>Quick answer</h2>
      <p>No, not fully yet. The site covers the tender skeleton, the supplied documents, the major returnables, the role boundaries and the first specialist gates. The Project Brief adds a deeper contractor-control layer that still needs a stronger register if the team decides to bid.</p>
      <p>The good news: the missing pieces are mostly trackable. They are not things Luke should personally certify. They are VFG, RPEQ, survey, certifier, WHS, environmental, landscape and contractor-delivery items that need to be called out early.</p>
    </section>

    <section class="section grid three">
      <article class="card"><h3>Covered enough to start</h3><p>Admin, documents, returnables, source photos, role boundaries and big specialist warnings are in place.</p></article>
      <article class="card"><h3>Thin</h3><p>The governing codes, management plans, permits, signage, fencing, handover and technical registers need more explicit tracking.</p></article>
      <article class="card"><h3>Missing detail</h3><p>A serious submission should add clause-level controls, product data sheets, tests, hold points, turf/tree details and closeout obligations.</p></article>
    </section>

    <section class="section">
      <h2>Covered enough to start</h2>
      {table(["Project Brief area", "Current site coverage", "Status", "Next note"], brief_covered_rows)}
    </section>

    <section class="section">
      <h2>Thin / strengthen before submission</h2>
      {table(["Project Brief area", "Why it is thin", "Status", "Suggested action"], brief_thin_rows)}
    </section>

    <section class="section">
      <h2>Missing or not really broken out yet</h2>
      {table(["Project Brief area", "Gap", "Status", "Suggested action"], brief_missing_rows)}
    </section>

    <section class="section band">
      <h2>Codes governing work register</h2>
      <p>This register is pulled from the Project Brief's codes section. It is a tracking aid only. VFG and the relevant specialists need to confirm which standards apply, who owns them, and whether they already have paid standards access.</p>
      {table(["Code / standard / source", "Tender relevance", "Where it appears", "Current status"], code_rows)}
    </section>

    <section class="section band tint">
      <h2>Practical next step</h2>
      <p>If the team proceeds after the site inspection, the next useful build is a private or internal Project Brief clause checklist. That should map each obligation to owner, evidence, due date, public/private status and whether it belongs in the tender response, the construction methodology, a management plan or a post-award delivery register.</p>
    </section>
    """
    write("pages/project-brief-coverage.html", layout("pages/project-brief-coverage.html", "Project Brief coverage", "A practical audit of what the site already covers, where it is thin, and what the Project Brief still needs VFG or specialist owners to confirm.", brief_coverage))

    compliance_rows = [
        ["Mandatory site inspection", "Addendum 1 / ITT", "Attendance confirmation", "Joint", badge("To confirm"), "Confirm who attends and how attendance is recorded."],
        ["Signed addendum", "Addendum 1", "Signed addendum returned", "Tender lead", badge("To confirm"), "Must be returned with tender documents."],
        ["Section B Returnable A Form of Tender", "Section B", "Returnable A", "VFG", badge("Not started"), "Formal offer and authorised signature."],
        ["B Compliance and Declarations", "Section B", "Returnable B", "VFG / Joint", badge("Needs info"), "Declare full, partial or non-compliance."],
        ["C Social Responsibility", "Section B", "Returnable C", "Joint", badge("Drafting", "gum"), "Luke can help draft grounded social benefit."],
        ["D Insurance", "Section B", "Returnable D", "VFG", badge("Needs info"), "Certificates of currency required."],
        ["E Licences/certificates", "Section B", "Returnable E", "VFG / Specialist", badge("Needs specialist", "warning"), "Confirm required licences and specialist evidence."],
        ["F Subcontractors/subconsultants", "Section B", "Returnable F", "VFG", badge("Needs info"), "Includes RPEQ/design/survey pathway if subcontracted."],
        ["G Local Business and Benefit", "ITT / Section B", "Returnable G", "Joint", badge("Drafting", "gum"), "15 percent weighting."],
        ["H Tendered Sum and BOQ", "ITT / BOQ", "Returnable H", "VFG", badge("Not started"), "30 percent weighting. Keep prices private."],
        ["I Proposed Concept Design", "ITT / Project Brief", "Returnable I", "VFG / Joint", badge("Needs VFG review", "dark"), "10 percent weighting. Concept only until confirmed."],
        ["J Company and project team experience", "ITT / Section B", "Returnable J", "VFG", badge("Needs VFG review", "dark"), "30 percent weighting with operational capability."],
        ["K Program/methodology/cashflow", "ITT / Section B", "Returnable K", "VFG", badge("Needs VFG review", "dark"), "15 percent weighting."],
        ["L QMS/WHSMP/SSEMP", "ITT / Section B", "Returnable L", "VFG / Specialist", badge("Mandatory", "warning"), "Mandatory accreditation systems and management plans."],
        ["Stage 1 Structural Investigation", "Project Brief", "Project deliverable", "VFG / Specialist", badge("Needs specialist", "warning"), "Confirm scope and engineering pathway."],
        ["Stage 2 Detailed Design", "Project Brief", "Project deliverable", "VFG / Specialist", badge("Needs specialist", "warning"), "Design pathway and review responsibilities."],
        ["Stage 3 Permits/Applications", "Project Brief", "Project deliverable", "VFG / Specialist", badge("Needs specialist", "warning"), "If required by statutory approvals."],
        ["Stage 4 Final RPEQ For Construction", "Project Brief", "Certified drawings", "RPEQ / Specialist", badge("Needs specialist", "warning"), "Not Luke-owned."],
        ["Pre/post dilapidation survey", "Project Brief", "Project deliverable", "VFG / Specialist", badge("Needs info"), "Confirm timing and responsibility."],
        ["Service locating", "Project Brief", "Project deliverable", "VFG / Specialist", badge("Needs info"), "Needed before serious design/construction."],
        ["Safety in Design", "Project Brief", "Report", "Specialist / VFG", badge("Needs specialist", "warning"), "Needs qualified design input."],
        ["Environmental and koala habitat controls", "Project Brief", "Management controls", "VFG / Specialist", badge("Needs info"), "Protect adjacent vegetation and habitat."],
        ["As Constructed/ADAC/Form 16", "Project Brief", "Final deliverables", "RPEQ / Specialist", badge("Needs specialist", "warning"), "Final certification pathway."],
        ["Defects Liability Period", "Contract / Project Brief", "Post-completion obligation", "VFG", badge("To confirm"), "Check contract obligations and risk."],
      ]
    compliance = f"""
    <section class="section band">
      <h2>Matrix status</h2>
      <p>This is a starting matrix, not a final compliance statement. Owners and status labels should be confirmed before any tender response is lodged.</p>
      <p><a class="button-link secondary" href="project-brief-coverage.html">Open Project Brief coverage audit</a></p>
    </section>
    <section class="section">
      {table(["Tender requirement", "Source document / section", "Returnable or deliverable", "Owner", "Status", "Notes"], compliance_rows)}
    </section>
    """
    write("pages/compliance-matrix.html", layout("pages/compliance-matrix.html", "Compliance matrix", "A starting point for tracking tender requirements, ownership, status and open notes.", compliance))

    returnables_page = """
    <section class="section band">
      <h2>Section B in plain language</h2>
      <p>The ITT and Section B source files say the returnable schedules are the tender offer. This page is a working guide only. Filled forms, signatures, prices and private evidence should stay outside the public Pages site.</p>
    </section>
    <section class="section" data-returnables-src="../data/returnables.json">
      <p class="warning-box">Loading returnables from data/returnables.json...</p>
    </section>
    """
    write("pages/returnables.html", layout("pages/returnables.html", "Returnables", "A plain-English guide to returnables A-L, who likely leads them, and what evidence is needed.", returnables_page))

    concept = f"""
    <section class="section band">
      <h2>Draft design intent for discussion</h2>
      <p>The working intent is to retain the two transition bowls as the core identity, repair priority hazards, verify drainage and surface levels, add modest street/progression features if appropriate, refresh ancillary elements, improve signage and presentation, protect adjacent vegetation and keep the facility durable and maintainable.</p>
      <p>This is a discussion structure only. VFG and relevant specialists must confirm rideability, geometry, repair method, drainage, certification and buildability.</p>
      <div class="label-strip">{badge("Tender Concept Only", "warning")}{badge("Requires VFG review", "dark")}{badge("Not for construction", "warning")}</div>
    </section>
    <section class="section grid">
      {card("Option A: Minimal repair and refresh", "Repair priority defects, address coping, refresh signage/seating/ancillary works and keep the facility close to current form.", "Discussion option")}
      {card("Option B: Repair plus compact progression street zone", "Retain bowls, repair hazards and explore a small street/progression area with ledges, rails, manual pad or banks if the flow works.", "Discussion option")}
      {card("Option C: Broader participation upgrade", "Repair the bowls and explore a more complete participation upgrade, subject to budget, site constraints, safety, certification and VFG intent.", "Discussion option")}
    </section>
    <section class="section band tint">
      <h2>Verification issues</h2>
      {list_items([
        "Drainage and water pooling shown in June photos.",
        "Cracks, wide joints and height irregularities identified by the audit.",
        "Coping repair method and construction practicality.",
        "Where street-style elements can sit without damaging bowl flow.",
        "Signage, fencing and seating requirements against source details.",
        "Tree, root, koala habitat and environmental controls.",
      ])}
    </section>
    """
    write("pages/concept-design-workspace.html", layout("pages/concept-design-workspace.html", "Concept design workspace", "A careful place to capture design options without pretending they are final recommendations.", concept))

    cad = f"""
    <section class="section band">
      <h2>CAD approach</h2>
      <p>CAD should turn field ideas into clear tender-stage concept drawings, not certified construction drawings. Luke can help draft from supplied VFG design intent, but geometry, rideability, engineering, survey, service locations and RPEQ matters require the right project team.</p>
      <div class="label-strip">{badge("NOT FOR CONSTRUCTION", "warning")}{badge("Subject to survey", "dark")}{badge("RPEQ required", "warning")}</div>
    </section>
    <section class="section grid two">
      <article class="card"><h3>Inputs needed from VFG</h3>{list_items(["Hand sketches and preferred elements.", "Dimensions, clearances and rideability intent.", "Repair method and construction sequence.", "Example projects and photos."])}</article>
      <article class="card"><h3>Inputs needed from site</h3>{list_items(["Survey, levels and services.", "Existing bowl geometry.", "Drainage low points.", "Tree/root constraints.", "Shelter, fencing and seating locations."])}</article>
      <article class="card"><h3>Drawing outputs</h3>{list_items(["Existing conditions / opportunity plan.", "Proposed concept layout plan.", "Repair and scope annotation plan.", "Staging / access / laydown plan.", "Signage / fencing / ancillary works plan."])}</article>
      <article class="card"><h3>CAD files in this repo</h3>{list_items(["cad/README.md", "cad/layers.md", "cad/titleblock-notes.md", "cad/PDG20842_Windemere_Concept_Seed_NotForConstruction.dxf"])}</article>
    </section>
    """
    write("pages/cad-workflow.html", layout("pages/cad-workflow.html", "CAD workflow", "Guidance for concept-only CAD support from site notes and VFG-supplied design intent.", cad))

    questions_page = """
    <section class="section band">
      <h2>Editable source</h2>
      <p>This table is rendered from <code>data/questions.json</code>. Edit the JSON file to add answers, owners or tender impact notes after the site visit.</p>
    </section>
    <section class="section" data-questions-src="../data/questions.json">
      <p class="warning-box">Loading questions from data/questions.json...</p>
    </section>
    """
    write("pages/questions-register.html", layout("pages/questions-register.html", "Questions register", "A seeded register for site-visit questions, ownership, status and tender impact.", questions_page))

    task_page = """
    <section class="section band">
      <h2>Editable source</h2>
      <p>This board is rendered from <code>data/tasks.json</code>. Move a task by changing its status to one of the column names.</p>
    </section>
    <section class="section" data-tasks-src="../data/tasks.json">
      <p class="warning-box">Loading tasks from data/tasks.json...</p>
    </section>
    """
    write("pages/task-board.html", layout("pages/task-board.html", "Task board", "A simple Kanban-style board for the immediate tender partnership tasks.", task_page))

    decision = f"""
    <section class="section grid two">
      <article class="card"><h3>Proceed if</h3>{list_items([
        "VFG confirms technical/design/build capability and wants to lead as Principal Contractor.",
        "RPEQ, design, survey and certification pathway is credible.",
        "Returnables can be completed on time.",
        "Pricing and program can be competitive.",
        "Luke's role is clearly scoped and accepted.",
        "Tender risk feels manageable.",
      ])}</article>
      <article class="card"><h3>Pause or no-bid if</h3>{list_items([
        "Mandatory site inspection or addendum compliance is missed.",
        "RPEQ/certification pathway is unclear.",
        "BOQ/pricing cannot be completed credibly.",
        "Roles remain blurry.",
        "Tender timing is too tight.",
        "Contract risk is not acceptable.",
      ])}</article>
    </section>
    <section class="section band tint">
      <h2>Decision record</h2>
      <p>Use the back-and-forth log and task board to capture the decision, the reason, and any next action. A no-bid can still be a good outcome if it prevents a messy or non-compliant tender.</p>
    </section>
    """
    write("pages/decision-gate.html", layout("pages/decision-gate.html", "Decision gate", "A simple bid/no-bid framework to keep the partnership decision clear and respectful.", decision))

    risks = f"""
    <section class="section">
      <h2>Risk register starter</h2>
      {table(["Risk / assumption", "Why it matters", "Current response", "Owner"], [
        ["Drainage and water pooling", "Photos show water while the audit recorded no pooling at the inspection time.", "Verify on site and identify whether it is design, maintenance or both.", "VFG / Specialist"],
        ["RPEQ and certification pathway", "The project brief requires certified for-construction and as-constructed deliverables.", "Confirm consultant pathway before proceeding.", "VFG / Specialist"],
        ["BOQ/pricing confidence", "Tendered sum is heavily weighted and must be credible.", "Keep pricing private and VFG-led.", "VFG"],
        ["Role blur", "Luke can support drafting but cannot certify, price, engineer or act as contractor.", "Use role-boundary labels and specialist review gates.", "Joint"],
        ["Tender timing", "Returnables, site inspection, concept design, pricing and evidence may compress quickly.", "Use the task board and bid/no-bid gate.", "Joint"],
        ["Public leakage", "A public repo could expose tender-sensitive material if unmanaged.", "Source docs are published intentionally; prices, signatures, filled forms and private details stay out.", "Luke"],
        ["Environmental / koala habitat controls", "Adjacent vegetation and habitat controls may affect works.", "Confirm project brief requirements and site constraints.", "VFG / Specialist"],
      ])}
    </section>
    """
    write("pages/risk-and-assumptions.html", layout("pages/risk-and-assumptions.html", "Risks and assumptions", "A starter register for the assumptions and risks that should be checked before submission effort ramps up.", risks))

    docs_page = f"""
    <section class="section band">
      <h2>Source tender downloads</h2>
      <p>This register lists the tender files, explains how they are used, and links to the published source copies. The full pack is also available as a single ZIP download.</p>
      <p><a class="button-link" href="../tender-documents/{esc(DOCUMENT_ZIP)}" download>Download full tender source pack ZIP</a></p>
      <p>Keep filled returnables, signatures, prices, supplier quotes, private evidence and final submission material outside the public repo.</p>
    </section>
    <section class="section" data-docs-src="../data/docs.json">
      <p class="warning-box">Loading document register from data/docs.json...</p>
    </section>
    """
    write("pages/document-register.html", layout("pages/document-register.html", "Document register", "A plain-language register of the supplied tender documents and their public/private caution notes.", docs_page))

    log = f"""
    <section class="section timeline">
      <article><h2>Introduced by mutual friend</h2><p><strong>Date:</strong> To confirm. <strong>People:</strong> Luke, Paolo, Kieran, mutual friend. <strong>Decision:</strong> Explore whether there is a possible tender collaboration.</p><p><strong>Next action:</strong> Review tender pack and prepare site-visit questions.</p></article>
      <article><h2>VFG asked Luke to help translate practical experience</h2><p><strong>Date:</strong> To confirm. <strong>Summary:</strong> Working note that VFG may want help turning practical ideas and experience into tender-compliant designs and AutoCAD documentation.</p><p><strong>Decision:</strong> Keep scope exploratory and confirm boundaries.</p></article>
      <article><h2>Luke registered on VendorPanel</h2><p><strong>Date:</strong> To confirm. <strong>Summary:</strong> Luke registered under urban design and master planning through Strange But True.</p><p><strong>Next action:</strong> Keep role description honest and non-technical where appropriate.</p></article>
      <article><h2>Site meeting planned</h2><p><strong>Date:</strong> Working assumption: Wednesday 15 July 2026. <strong>People:</strong> Luke, Paolo and Kieran at mandatory site inspection.</p><p><strong>Next action:</strong> Confirm RSVP and capture observations.</p></article>
      <article><h2>Partnership remains exploratory</h2><p><strong>Summary:</strong> Proceed only if the team agrees they can win and deliver cleanly.</p><p><strong>Decision:</strong> Use bid/no-bid gate before major submission effort.</p></article>
    </section>
    """
    write("pages/back-and-forth-log.html", layout("pages/back-and-forth-log.html", "Back-and-forth log", "A lightweight chronology for the relationship, decisions and next actions.", log))

    local_benefit = f"""
    <section class="section band">
      <h2>Tender-grounded themes</h2>
      <p>The local benefit response should be practical and evidence-led. It should describe what the team can actually do, not make grand civic promises that cannot be backed up.</p>
    </section>
    <section class="section grid two">
      <article class="card"><h3>Local spend</h3><p>Redlands/SEQ suppliers where practical, including fuel, food, accommodation, materials, plant hire, fencing, turf, concrete support or other legitimate project spend.</p></article>
      <article class="card"><h3>Youth recreation and public space</h3><p>A refreshed skate bowl can support youth recreation, public-space pride, visibility, durability and a broader mix of wheeled users where safe and appropriate.</p></article>
      <article class="card"><h3>Broader participation</h3><p>Street/progression features may help beginners and intermediate users without losing the advanced transition identity of the two bowls, subject to VFG design review.</p></article>
      <article class="card"><h3>Handover activation</h3><p>A small community handover/opening activation may be considered if VFG and RCC think it is appropriate. Treat it as optional, not core scope.</p></article>
    </section>
    """
    write("pages/local-benefit.html", layout("pages/local-benefit.html", "Local benefit", "Practical themes Luke can help shape for local business and social benefit, pending VFG confirmation.", local_benefit))

    roadmap = f"""
    <section class="section">
      <h2>Submission pathway</h2>
      {table(["Phase", "Purpose", "Key outputs", "Decision"], [
        ["1. Source pack and site visit", "Understand tender and site conditions.", "Agenda, questions, observations, document register.", "Is there enough information to proceed?"],
        ["2. Role split and evidence", "Confirm who owns each returnable and specialist pathway.", "Compliance matrix, VFG evidence list, role boundaries.", "Are roles clear enough?"],
        ["3. Concept direction", "Turn VFG practical intent into tender concept structure.", "Options, sketches, concept-only CAD notes, Returnable I outline.", "Can the concept be credible and compliant?"],
        ["4. Commercial and program check", "Confirm price, BOQ and method can be competitive.", "Private BOQ/pricing, program, methodology, cashflow.", "Does the bid stack up?"],
        ["5. Review and submit", "Complete Section B and attachments.", "Signed forms, reviewed plans, evidence pack, final tender package.", "Submit only after VFG/specialist review."],
      ])}
    </section>
    <section class="section warning-box">
      <h2>Review gate</h2>
      <p>Nothing in this site should go to RCC as-is. It is scaffolding for the team, not the tender submission.</p>
    </section>
    """
    write("pages/submission-roadmap.html", layout("pages/submission-roadmap.html", "Submission roadmap", "A staged pathway from site visit through bid/no-bid, concept response, review and possible submission.", roadmap))

    site_map_rows = []
    for href, label in NAV:
      page_href = f"../{href}"
      site_map_rows.append([label, f"<a href=\"{esc(page_href)}\">Open page</a>"])
    site_map = f"""
    <section class="section band">
      <h2>Quick routes</h2>
      <p>Use this page when the navigation menu feels too small for the full workspace. It points to the main pages, the document downloads and the public repo surfaces.</p>
      <div class="sbt-actions">
        <a class="button-link" href="../tender-documents/{esc(DOCUMENT_ZIP)}" download>Download full tender source pack ZIP</a>
        <a class="button-link secondary" href="../pages/document-register.html">Open document register</a>
        <a class="button-link secondary" href="../sitemap.xml">Open sitemap.xml</a>
      </div>
    </section>

    <section class="section">
      <h2>All site pages</h2>
      {table(["Page", "Link"], site_map_rows)}
    </section>

    <section class="section grid two">
      <article class="card"><h3>Most useful starting points</h3>{list_items([
        "Dashboard for the current working summary.",
        "Document register for source downloads.",
        "360 site record for the 15 July 2026 inspection imagery.",
        "Site photos for actual tender-pack image evidence.",
        "Questions register and task board for the next conversation.",
        "Decision gate before any serious submission effort.",
      ])}</article>
      <article class="card"><h3>Public repo surfaces</h3>{list_items([
        "GitHub Pages site: https://auraofintelligence.github.io/windemere-skate-bowl-tender-workspace/",
        "GitHub repo: https://github.com/auraofintelligence/windemere-skate-bowl-tender-workspace",
        "Machine sitemap: sitemap.xml at the repository root.",
        "Source documents: tender-documents/ at the repository root.",
      ])}</article>
    </section>
    """
    write("pages/site-map.html", layout("pages/site-map.html", "Site map", "A plain navigation map for the tender workspace, source downloads, public repo links and key work paths.", site_map))


def main() -> None:
    write_assets()
    write_data()
    write_meta_files()
    write_cad_files()
    write_pages()


if __name__ == "__main__":
    main()
