#!/usr/bin/env python3
import html
import hashlib
import json
import math
import textwrap
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "benchmarks.json"
CHART_DIR = ROOT / "charts"
REPORT_DIR = ROOT / "report"

OKABE_ITO = ["#0072B2", "#E69F00", "#009E73", "#D55E00", "#CC79A7", "#56B4E9", "#000000", "#F0E442"]

PALETTE = {
    "9470C": "#0072B2",
    "Xeon Max 9470C 1S | 64GB HBM2e": "#0072B2",
    "Xeon Max 9470C HBM2": "#0072B2",
    "Reference": "#666666",
    "EPYC 9755": "#E69F00",
    "EPYC 9745": "#D55E00",
    "EPYC 9455P": "#CC79A7",
    "EPYC 9555P": "#CC79A7",
    "EPYC 9655P": "#009E73",
    "EPYC 9654": "#009E73",
    "EPYC 9654 2S | 24ch DDR5-4800": "#009E73",
    "2x EPYC 9655": "#009E73",
    "2x EPYC 9475F": "#56B4E9",
    "2x EPYC 9455": "#F0E442",
    "2x EPYC 9755": "#000000",
    "EPYC 9754 2S | 24ch DDR5-4800": "#E69F00",
    "2x Xeon 6980P": "#56B4E9",
    "TR 9980X": "#D55E00",
    "TR 7980X": "#CC79A7",
    "Threadripper 9980X": "#D55E00",
    "Threadripper 7980X": "#CC79A7",
    "Ryzen 9 9950X": "#009E73",
    "Ryzen 9 9950X3D": "#56B4E9",
    "Ryzen 7 9800X3D": "#F0E442",
    "Core Ultra 9 285K": "#E69F00",
    "Core Ultra 7 270K+": "#56B4E9",
    "Core i9-14900K": "#000000",
    "Core i5-12600K": "#CC79A7",
    "Ryzen 9 7950X": "#009E73",
    "Xeon Gold 6414U": "#666666",
    "Xeon 8490H": "#56B4E9",
    "Xeon 6972P 2S | 24ch DDR5-6400": "#000000",
    "Xeon SPR 2S | 16ch DDR5-4800": "#56B4E9",
    "Xeon 8592+ 2S | 16ch DDR5-5600": "#D55E00",
    "Xeon CLX 2S | 12ch DDR4-2933": "#CC79A7",
    "Xeon 8380 2S | 16ch DDR4-3200": "#666666",
    "Desktop DDR5 dual-ch low": "#999999",
    "Desktop DDR5 dual-ch high": "#666666"
}

DEFAULT_COLORS = OKABE_ITO


def esc(value):
    return html.escape(str(value), quote=True)


def fmt(value):
    if value >= 1000:
        return f"{value:,.0f}"
    if value >= 100:
        return f"{value:,.1f}".rstrip("0").rstrip(".")
    if value >= 10:
        return f"{value:,.2f}".rstrip("0").rstrip(".")
    return f"{value:,.2f}".rstrip("0").rstrip(".")


def color_for(series):
    if series in PALETTE:
        return PALETTE[series]
    idx = int(hashlib.sha1(series.encode("utf-8")).hexdigest()[:8], 16) % len(DEFAULT_COLORS)
    return DEFAULT_COLORS[idx]


def wrap_label(text, width=18, max_lines=3):
    lines = textwrap.wrap(text, width=width, break_long_words=False)
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        lines[-1] = lines[-1].rstrip(".") + "..."
    return lines or [text]


def nice_max(max_value):
    if max_value <= 0:
        return 1
    order = 10 ** math.floor(math.log10(max_value))
    for step in (1, 2, 2.5, 5, 10):
        top = step * order
        if top >= max_value:
            return top
    return 10 * order


def render_bar_chart(chart):
    data = chart["data"]
    labels = list(dict.fromkeys(item["label"] for item in data))
    grouped = defaultdict(list)
    for item in data:
        grouped[item["label"]].append(item)

    max_value = max(item["value"] for item in data)
    axis_max = nice_max(max_value * 1.12)
    width = max(1040, 120 + len(labels) * 118)
    height = 650
    left = 92
    right = 34
    top = 104
    bottom = 158
    plot_w = width - left - right
    plot_h = height - top - bottom
    group_w = plot_w / len(labels)

    parts = [svg_open(width, height, chart)]
    parts.append(grid(axis_max, left, top, plot_w, plot_h, chart["unit"]))

    for i, label in enumerate(labels):
        items = grouped[label]
        inner_gap = 4
        bar_w = min(46, (group_w - 24 - inner_gap * (len(items) - 1)) / len(items))
        start_x = left + i * group_w + (group_w - (bar_w * len(items) + inner_gap * (len(items) - 1))) / 2
        for j, item in enumerate(items):
            value = item["value"]
            bar_h = plot_h * value / axis_max
            x = start_x + j * (bar_w + inner_gap)
            y = top + plot_h - bar_h
            series = item["series"]
            parts.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{bar_h:.1f}" rx="3" fill="{color_for(series)}"/>')
            parts.append(f'<text x="{x + bar_w / 2:.1f}" y="{y - 7:.1f}" class="value" text-anchor="middle">{esc(fmt(value))}</text>')

        for line_no, line in enumerate(wrap_label(label)):
            y = top + plot_h + 30 + line_no * 16
            parts.append(f'<text x="{left + i * group_w + group_w / 2:.1f}" y="{y:.1f}" class="xlabel" text-anchor="middle">{esc(line)}</text>')

    parts.append(legend(sorted(set(item["series"] for item in data)), left, height - 40))
    parts.append("</svg>")
    return "\n".join(parts)


def svg_open(width, height, chart):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{esc(chart["title"])}">
<style>
  .title {{ font: 700 24px Inter, ui-sans-serif, system-ui, -apple-system, Segoe UI, sans-serif; fill: #1f2937; }}
  .subtitle {{ font: 400 14px Inter, ui-sans-serif, system-ui, -apple-system, Segoe UI, sans-serif; fill: #5f6b7a; }}
  .axis {{ stroke: #8b97a7; stroke-width: 1; }}
  .grid {{ stroke: #d8dee8; stroke-width: 1; }}
  .tick {{ font: 12px Inter, ui-sans-serif, system-ui, -apple-system, Segoe UI, sans-serif; fill: #657084; }}
  .xlabel {{ font: 12px Inter, ui-sans-serif, system-ui, -apple-system, Segoe UI, sans-serif; fill: #364152; }}
  .value {{ font: 700 11px Inter, ui-sans-serif, system-ui, -apple-system, Segoe UI, sans-serif; fill: #202938; }}
  .legend {{ font: 12px Inter, ui-sans-serif, system-ui, -apple-system, Segoe UI, sans-serif; fill: #364152; }}
</style>
<rect x="0" y="0" width="{width}" height="{height}" fill="#fbfcfe"/>
<text x="34" y="42" class="title">{esc(chart["title"])}</text>
<text x="34" y="68" class="subtitle">{esc(chart["subtitle"])}</text>'''


def grid(axis_max, left, top, plot_w, plot_h, unit):
    parts = []
    for i in range(6):
        value = axis_max * i / 5
        y = top + plot_h - plot_h * i / 5
        parts.append(f'<line x1="{left}" y1="{y:.1f}" x2="{left + plot_w}" y2="{y:.1f}" class="grid"/>')
        parts.append(f'<text x="{left - 10}" y="{y + 4:.1f}" class="tick" text-anchor="end">{esc(fmt(value))}</text>')
    parts.append(f'<line x1="{left}" y1="{top}" x2="{left}" y2="{top + plot_h}" class="axis"/>')
    parts.append(f'<line x1="{left}" y1="{top + plot_h}" x2="{left + plot_w}" y2="{top + plot_h}" class="axis"/>')
    parts.append(f'<text x="{left}" y="{top - 16}" class="tick">{esc(unit)}</text>')
    return "\n".join(parts)


def legend(series, x, y):
    parts = []
    cursor = x
    for name in series:
        text_w = min(180, 8 * len(name) + 24)
        parts.append(f'<rect x="{cursor}" y="{y - 11}" width="12" height="12" rx="2" fill="{color_for(name)}"/>')
        parts.append(f'<text x="{cursor + 18}" y="{y}" class="legend">{esc(name)}</text>')
        cursor += text_w
        if cursor > 940:
            cursor = x
            y += 20
    return "\n".join(parts)



def render_interactive_section(chart):
    entries_by_label = defaultdict(list)
    for row in chart["data"]:
        entries_by_label[row["label"]].append(dict(row))

    subtests = {}
    for item in chart.get("local_subtests", []):
        label = item["label"]
        entries = entries_by_label[label]
        comparison_count = max(0, len({entry["series"] for entry in entries}) - 1)
        if chart.get("type") == "stream_interactive":
            note = f"Includes {comparison_count} public comparison systems for this STREAM subtest. Mixed platform classes are shown together; values are not normalized across socket count, memory type/channel, compiler, NUMA mode, or tuning."
        elif chart["id"] == "seven_zip":
            note = f"Includes {comparison_count} public comparison CPUs for this metric. Higher MIPS means better 7-Zip throughput."
        elif chart["id"] == "vllm_cpu":
            if label == "Latency speed":
                note = f"Includes {comparison_count} public comparison CPUs. This view converts average latency seconds to 1/s so taller bars mean lower latency."
            else:
                note = f"Includes {comparison_count} public comparison CPUs. This view uses native tokens/s throughput."
        elif chart["id"] == "gromacs_lammps":
            note = f"Includes {comparison_count} public comparison systems for this molecular dynamics workload. Higher ns/day means faster simulation throughput."
        elif chart["id"] == "cp2k_speed":
            note = f"Includes {comparison_count} public comparison systems for this CP2K input. Original seconds are converted to speed relative to the 9470C baseline."
        elif chart["id"] == "compile_fftw_ycruncher":
            if label == "FFTW 1D 4096":
                note = f"Includes {comparison_count} public comparison CPUs. Original Mflops are normalized to the 9470C baseline for bar length."
            else:
                note = f"Includes {comparison_count} public comparison CPUs/systems. Original seconds are converted to speed relative to the 9470C baseline."
        elif chart["id"] == "onednn_fp16_fp32_limited":
            if comparison_count:
                note = f"Limited comparison: includes {comparison_count} public comparison CPU for this oneDNN mode."
            else:
                note = "Limited comparison: no verified public comparison CPU is included for this oneDNN mode yet."
        elif chart["id"] == "openvino_genai_ttft":
            note = f"Includes {comparison_count} public comparison CPUs. Original TTFT milliseconds are converted to first-token speed for bar length."
        elif chart["id"] == "openvino_2026":
            note = f"Includes {comparison_count} comparison systems where verified values are available. Labels retain latency ms when the local run recorded it."
        elif chart["id"] == "numpy_single_thread":
            note = f"Includes {comparison_count} public comparison CPUs. This PTS profile is forced single-threaded, so it is not a platform-wide throughput benchmark."
        else:
            note = f"Includes {comparison_count} public comparison entries where verified values are available."
        subtests[item["id"]] = {
            "label": label,
            "formula": item["formula"],
            "unit": item.get("unit", chart["unit"]),
            "decimals": item.get("decimals"),
            "notation": item.get("notation"),
            "entries": entries,
            "note": note,
        }

    title = "STREAM 2013 Memory Bandwidth" if chart.get("type") == "stream_interactive" else chart["title"]
    intro = chart["subtitle"]
    aria = "STREAM subtests" if chart.get("type") == "stream_interactive" else f'{chart["title"]} metrics'
    meta_label = chart.get("meta_label") or ("Kernel" if chart.get("type") == "stream_interactive" else "Metric")
    groups = chart.get("comparison_groups") or []
    payload = {
        "title": title,
        "subtests": subtests,
        "order": [item["id"] for item in chart.get("local_subtests", [])],
        "groups": groups,
        "groupOrder": [group["id"] for group in groups],
        "palette": OKABE_ITO,
    }
    payload_json = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
    buttons = "".join(
        f'<button type="button" data-interactive-button="{esc(item["id"])}">{esc(item["label"])}</button>'
        for item in chart.get("local_subtests", [])
    )
    group_buttons = "".join(
        f'<button type="button" data-interactive-group="{esc(group["id"])}">{esc(group["label"])}</button>'
        for group in groups
    )
    group_controls = f'<div class="stream-tabs stream-group-tabs" role="tablist" aria-label="Comparison groups">{group_buttons}</div>' if groups else ""
    return f"""
      <section class="chart stream-card" data-interactive-chart>
        <div class="chart-head">
          <div>
            <h2>{esc(title)}</h2>
            <p>{esc(intro)}</p>
          </div>
          <div class="stream-tab-stack">
            {group_controls}
            <div class="stream-tabs" role="tablist" aria-label="{esc(aria)}">
              {buttons}
            </div>
          </div>
        </div>
        <div class="stream-panel">
          <div class="stream-plot" aria-live="polite">
            <div class="stream-axis" data-interactive-axis></div>
            <div class="stream-bars" data-interactive-bars></div>
          </div>
          <aside class="stream-meta">
            <div class="stream-meta-label">{esc(meta_label)}</div>
            <div class="stream-meta-title" data-interactive-title></div>
            <code data-interactive-formula></code>
            <p data-interactive-note></p>
          </aside>
        </div>
        <script type="application/json" data-interactive-json>{payload_json}</script>
      </section>"""



def render_paged_grouped_section(chart):
    entries_by_label = defaultdict(list)
    for row in chart["data"]:
        entries_by_label[row["label"]].append(dict(row))

    pages = {}
    for item in chart.get("local_subtests", []):
        label = item["label"]
        entries = entries_by_label[label]
        pages[item["id"]] = {
            "label": label,
            "formula": item["formula"],
            "unit": chart["unit"],
            "entries": entries,
        }

    payload = {
        "title": chart["title"],
        "pages": pages,
        "order": [item["id"] for item in chart.get("local_subtests", [])],
        "palette": OKABE_ITO,
    }
    payload_json = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
    buttons = "".join(
        f'<button type="button" data-paged-button="{esc(item["id"])}">{esc(item["label"])}</button>'
        for item in chart.get("local_subtests", [])
    )
    return f"""
      <section class="chart paged-card" data-paged-chart>
        <div class="chart-head">
          <div>
            <h2>{esc(chart["title"])}</h2>
            <p>{esc(chart["subtitle"])}</p>
          </div>
          <div class="stream-tabs" role="tablist" aria-label="{esc(chart.get("page_label", "Page"))}">
            {buttons}
          </div>
        </div>
        <div class="paged-plot-wrap">
          <div class="paged-title" data-paged-title></div>
          <div class="paged-subtitle" data-paged-formula></div>
          <div class="paged-plot" data-paged-plot aria-live="polite"></div>
          <div class="paged-note" data-paged-note></div>
        </div>
        <script type="application/json" data-paged-json>{payload_json}</script>
      </section>"""


def stream_interaction_script():
    return r"""
<script>
(() => {
  const roots = Array.from(document.querySelectorAll('[data-interactive-chart]'));
  if (!roots.length) return;

  const formatValue = (value, decimals = 0, notation = 'standard') => {
    if (notation === 'scientific') return value.toExponential(decimals);
    return value.toLocaleString(undefined, { minimumFractionDigits: decimals, maximumFractionDigits: decimals });
  };
  const niceMax = (value) => {
    const raw = value * 1.12;
    const order = Math.pow(10, Math.floor(Math.log10(raw || 1)));
    for (const step of [1, 2, 2.5, 5, 10]) {
      const top = step * order;
      if (top >= raw) return top;
    }
    return 10 * order;
  };

  roots.forEach((root) => {
    const data = JSON.parse(root.querySelector('[data-interactive-json]').textContent);
    const buttons = Array.from(root.querySelectorAll('[data-interactive-button]'));
    const groupButtons = Array.from(root.querySelectorAll('[data-interactive-group]'));
    const groupsById = Object.fromEntries((data.groups || []).map((group) => [group.id, group]));
    let activeGroup = data.groupOrder?.[0] || null;
    let activeMetric = data.order[0];
    const axis = root.querySelector('[data-interactive-axis]');
    const bars = root.querySelector('[data-interactive-bars]');
    const title = root.querySelector('[data-interactive-title]');
    const formula = root.querySelector('[data-interactive-formula]');
    const note = root.querySelector('[data-interactive-note]');
    const colorFor = (entry, index) => entry.series.includes('9470C') ? '#0072B2' : data.palette[(index + 1) % data.palette.length];

    function render(id) {
      activeMetric = id;
      const subtest = data.subtests[id];
      const decimals = Number.isInteger(subtest.decimals) ? subtest.decimals : 0;
      const notation = subtest.notation || 'standard';
      const entries = activeGroup ? subtest.entries.filter((entry) => (entry.group || 'local_hbm') === activeGroup) : subtest.entries;
      const max = niceMax(Math.max(...entries.map((entry) => entry.value)));
      const ticks = [0, 0.25, 0.5, 0.75, 1].map((ratio) => Math.round(max * ratio));

      buttons.forEach((button) => {
        const active = button.dataset.interactiveButton === id;
        button.classList.toggle('is-active', active);
        button.setAttribute('aria-selected', active ? 'true' : 'false');
      });
      groupButtons.forEach((button) => {
        const active = button.dataset.interactiveGroup === activeGroup;
        button.classList.toggle('is-active', active);
        button.setAttribute('aria-selected', active ? 'true' : 'false');
      });

      title.textContent = activeGroup ? `${subtest.label} / ${groupsById[activeGroup]?.label || activeGroup} (${subtest.unit})` : `${subtest.label} (${subtest.unit})`;
      formula.textContent = subtest.formula;
      note.textContent = activeGroup ? (groupsById[activeGroup]?.note || subtest.note) : subtest.note;
      axis.innerHTML = ticks.map((tick) => `<span style="left:${(tick / max) * 100}%">${formatValue(tick, decimals, notation)}</span>`).join('');
      bars.innerHTML = entries.map((entry, index) => {
        const width = Math.max(1.5, (entry.value / max) * 100);
        const color = colorFor(entry, index);
        const own = entry.series.includes('9470C') ? ' is-own' : '';
        const valueSuffix = entry.value_unit || 'x';
        const valueLabel = Number.isFinite(entry.raw_value)
          ? `${formatValue(entry.raw_value, 3)} ${entry.raw_unit || ''} · ${formatValue(entry.value, decimals, notation)}${valueSuffix}`
          : `${formatValue(entry.value, decimals, notation)}${entry.value_unit || ''}`;
        return `<div class="stream-row${own}">
          <div class="stream-name">${entry.series}</div>
          <div class="stream-track"><div class="stream-fill" style="width:${width}%;background:${color}"></div></div>
          <div class="stream-value">${valueLabel}</div>
        </div>`;
      }).join('');
    }

    buttons.forEach((button) => button.addEventListener('click', () => render(button.dataset.interactiveButton)));
    groupButtons.forEach((button) => button.addEventListener('click', () => { activeGroup = button.dataset.interactiveGroup; render(activeMetric); }));
    render(data.order[0]);
  });
})();
</script>"""



def paged_grouped_script():
    return r"""
<script>
(() => {
  const roots = Array.from(document.querySelectorAll('[data-paged-chart]'));
  if (!roots.length) return;

  const escapeHtml = (value) => String(value).replace(/[&<>"]/g, (char) => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[char]));
  const formatValue = (value) => value.toLocaleString(undefined, { maximumFractionDigits: 2 });
  const niceMax = (value) => {
    const raw = value * 1.14;
    const order = Math.pow(10, Math.floor(Math.log10(raw || 1)));
    for (const step of [1, 2, 2.5, 5, 10]) {
      const top = step * order;
      if (top >= raw) return top;
    }
    return 10 * order;
  };
  const wrapLines = (text, maxChars = 15, maxLines = 4) => {
    const words = String(text).replace(/ \| /g, ' ').split(/\s+/);
    const lines = [];
    let current = '';
    words.forEach((word) => {
      const next = current ? `${current} ${word}` : word;
      if (next.length > maxChars && current) {
        lines.push(current);
        current = word;
      } else {
        current = next;
      }
    });
    if (current) lines.push(current);
    if (lines.length > maxLines) {
      lines.length = maxLines;
      lines[maxLines - 1] = `${lines[maxLines - 1].slice(0, Math.max(3, maxChars - 3))}...`;
    }
    return lines;
  };

  roots.forEach((root) => {
    const data = JSON.parse(root.querySelector('[data-paged-json]').textContent);
    const buttons = Array.from(root.querySelectorAll('[data-paged-button]'));
    const title = root.querySelector('[data-paged-title]');
    const formula = root.querySelector('[data-paged-formula]');
    const plot = root.querySelector('[data-paged-plot]');
    const note = root.querySelector('[data-paged-note]');

    function render(id) {
      const page = data.pages[id];
      const entries = page.entries;
      const max = niceMax(Math.max(...entries.map((entry) => entry.value)));
      const ticks = [0, 0.25, 0.5, 0.75, 1].map((ratio) => Math.round(max * ratio));
      const width = Math.max(980, 170 + entries.length * 88);
      const height = 520;
      const left = 72;
      const right = 28;
      const top = 30;
      const bottom = 128;
      const plotW = width - left - right;
      const plotH = height - top - bottom;
      const step = plotW / entries.length;
      const barW = Math.min(46, step * 0.56);

      buttons.forEach((button) => {
        const active = button.dataset.pagedButton === id;
        button.classList.toggle('is-active', active);
        button.setAttribute('aria-selected', active ? 'true' : 'false');
      });

      title.textContent = `${page.label} (${page.unit})`;
      formula.textContent = page.formula;
      note.textContent = `Showing ${entries.length} verified comparison entries for this model only.`;

      const grid = ticks.map((tick) => {
        const y = top + plotH - (tick / max) * plotH;
        return `<line x1="${left}" y1="${y}" x2="${width - right}" y2="${y}" class="paged-grid" />
          <text x="${left - 10}" y="${y + 4}" class="paged-tick" text-anchor="end">${formatValue(tick)}</text>`;
      }).join('');

      const bars = entries.map((entry, index) => {
        const barH = Math.max(2, (entry.value / max) * plotH);
        const x = left + index * step + (step - barW) / 2;
        const y = top + plotH - barH;
        const color = entry.series === '9470C' ? '#0072B2' : data.palette[(index + 1) % data.palette.length];
        const stroke = entry.series === '9470C' ? ' stroke="#1f2937" stroke-width="2"' : '';
        const labelLines = wrapLines(entry.series);
        const label = labelLines.map((line, lineIndex) => `<tspan x="${x + barW / 2}" dy="${lineIndex ? 12 : 0}">${escapeHtml(line)}</tspan>`).join('');
        return `<rect x="${x}" y="${y}" width="${barW}" height="${barH}" rx="4" fill="${color}"${stroke}/>
          <text x="${x + barW / 2}" y="${y - 7}" class="paged-value" text-anchor="middle">${formatValue(entry.value)}</text>
          <text x="${x + barW / 2}" y="${top + plotH + 24}" class="paged-xlabel" text-anchor="middle">${label}</text>`;
      }).join('');
      const mobileRows = entries.map((entry, index) => {
        const color = entry.series === '9470C' ? '#0072B2' : data.palette[(index + 1) % data.palette.length];
        const own = entry.series === '9470C' ? ' is-own' : '';
        const width = Math.max(1.5, (entry.value / max) * 100);
        return `<div class="mobile-bar-row${own}">
          <div class="mobile-bar-label">${escapeHtml(entry.series)}</div>
          <div class="mobile-bar-value">${formatValue(entry.value)} ${escapeHtml(page.unit)}</div>
          <div class="mobile-bar-track"><div class="mobile-bar-fill" style="width:${width}%;background:${color}"></div></div>
        </div>`;
      }).join('');

      plot.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${width} ${height}" role="img" aria-label="${escapeHtml(page.label)} OpenVINO GenAI throughput">
        <line x1="${left}" y1="${top}" x2="${left}" y2="${top + plotH}" class="paged-axis" />
        <line x1="${left}" y1="${top + plotH}" x2="${width - right}" y2="${top + plotH}" class="paged-axis" />
        <text x="${left}" y="18" class="paged-unit">${escapeHtml(page.unit)}</text>
        ${grid}
        ${bars}
      </svg><div class="mobile-bars">${mobileRows}</div>`;
    }

    buttons.forEach((button) => button.addEventListener('click', () => render(button.dataset.pagedButton)));
    render(data.order[0]);
  });
})();
</script>"""



def render_matrix_section(chart):
    matrix = defaultdict(lambda: defaultdict(list))
    for row in chart["data"]:
        matrix[row["model"]][row["batch"]].append({
            "series": row["series"],
            "value": row["value"],
        })
    payload = {
        "title": chart["title"],
        "unit": chart["unit"],
        "models": chart["models"],
        "batches": chart["batches"],
        "matrix": matrix,
        "palette": OKABE_ITO,
    }
    payload_json = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
    model_buttons = "".join(
        f'<button type="button" data-matrix-model="{esc(item["id"])}">{esc(item["label"])}</button>'
        for item in chart["models"]
    )
    batch_buttons = "".join(
        f'<button type="button" data-matrix-batch="{esc(item["id"])}">{esc(item["label"])}</button>'
        for item in chart["batches"]
    )
    return f"""
      <section class="chart matrix-card" data-matrix-chart>
        <div class="chart-head">
          <div>
            <h2>{esc(chart["title"])}</h2>
            <p>{esc(chart["subtitle"])}</p>
          </div>
          <div class="matrix-controls">
            <div class="stream-tabs" role="tablist" aria-label="PyTorch models">{model_buttons}</div>
            <div class="stream-tabs" role="tablist" aria-label="PyTorch batch sizes">{batch_buttons}</div>
          </div>
        </div>
        <div class="stream-panel">
          <div class="stream-plot" aria-live="polite">
            <div class="stream-axis" data-matrix-axis></div>
            <div class="stream-bars" data-matrix-bars></div>
          </div>
          <aside class="stream-meta">
            <div class="stream-meta-label">Model / Batch</div>
            <div class="stream-meta-title" data-matrix-title></div>
            <code data-matrix-formula>batches/s; higher is better</code>
            <p data-matrix-note></p>
          </aside>
        </div>
        <script type="application/json" data-matrix-json>{payload_json}</script>
      </section>"""


def matrix_interaction_script():
    return r"""
<script>
(() => {
  const roots = Array.from(document.querySelectorAll('[data-matrix-chart]'));
  if (!roots.length) return;

  const formatValue = (value) => value.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  const niceMax = (value) => {
    const raw = value * 1.12;
    const order = Math.pow(10, Math.floor(Math.log10(raw || 1)));
    for (const step of [1, 2, 2.5, 5, 10]) {
      const top = step * order;
      if (top >= raw) return top;
    }
    return 10 * order;
  };

  roots.forEach((root) => {
    const data = JSON.parse(root.querySelector('[data-matrix-json]').textContent);
    const modelButtons = Array.from(root.querySelectorAll('[data-matrix-model]'));
    const batchButtons = Array.from(root.querySelectorAll('[data-matrix-batch]'));
    const axis = root.querySelector('[data-matrix-axis]');
    const bars = root.querySelector('[data-matrix-bars]');
    const title = root.querySelector('[data-matrix-title]');
    const note = root.querySelector('[data-matrix-note]');
    let activeModel = data.models[0].id;
    let activeBatch = data.batches[0].id;

    function labelFor(list, id) {
      return list.find((item) => item.id === id)?.label || id;
    }

    function render() {
      const entries = data.matrix[activeModel][activeBatch] || [];
      const max = niceMax(Math.max(...entries.map((entry) => entry.value)));
      const ticks = [0, 0.25, 0.5, 0.75, 1].map((ratio) => Math.round(max * ratio));

      modelButtons.forEach((button) => {
        const active = button.dataset.matrixModel === activeModel;
        button.classList.toggle('is-active', active);
        button.setAttribute('aria-selected', active ? 'true' : 'false');
      });
      batchButtons.forEach((button) => {
        const active = button.dataset.matrixBatch === activeBatch;
        button.classList.toggle('is-active', active);
        button.setAttribute('aria-selected', active ? 'true' : 'false');
      });

      title.textContent = `${labelFor(data.models, activeModel)} / ${labelFor(data.batches, activeBatch)} (${data.unit})`;
      note.textContent = `Showing ${entries.length} verified entries for this PyTorch subtest.`;
      axis.innerHTML = ticks.map((tick) => `<span style="left:${(tick / max) * 100}%">${formatValue(tick)}</span>`).join('');
      bars.innerHTML = entries.map((entry, index) => {
        const width = Math.max(1.5, (entry.value / max) * 100);
        const color = entry.series.includes('9470C') ? '#0072B2' : data.palette[(index + 1) % data.palette.length];
        const own = entry.series.includes('9470C') ? ' is-own' : '';
        return `<div class="stream-row${own}">
          <div class="stream-name">${entry.series}</div>
          <div class="stream-track"><div class="stream-fill" style="width:${width}%;background:${color}"></div></div>
          <div class="stream-value">${formatValue(entry.value)}</div>
        </div>`;
      }).join('');
    }

    modelButtons.forEach((button) => button.addEventListener('click', () => { activeModel = button.dataset.matrixModel; render(); }));
    batchButtons.forEach((button) => button.addEventListener('click', () => { activeBatch = button.dataset.matrixBatch; render(); }));
    render();
  });
})();
</script>"""



def render_abstract(payload):
    metadata = payload["metadata"]
    groups = []
    for group in metadata.get("classification", []):
        items = "".join(f'<li>{esc(item)}</li>' for item in group["items"])
        groups.append(f"""
          <div class="abstract-group">
            <h3>{esc(group["label"])}</h3>
            <ul>{items}</ul>
          </div>""")
    return f"""
      <section class="abstract">
        <h2>Abstract</h2>
        <p>{esc(metadata.get("abstract", ""))}</p>
        <div class="abstract-grid">
          {''.join(groups)}
        </div>
      </section>"""


def render_sources(payload):
    metadata = payload["metadata"]
    primary = "\n".join(
        f'<li><a href="{esc(src["url"])}">{esc(src["name"])}</a></li>'
        for src in metadata.get("primary_sources", [])
    )
    additional = "\n".join(
        f'<li><a href="{esc(src["url"])}">{esc(src["name"])}</a></li>'
        for src in metadata.get("sources", [])
    )
    return f"""
    <h2>Sources</h2>
    <div class="source-grid">
      <section>
        <h3>Original 9470C Result Links</h3>
        <ul>{primary}</ul>
      </section>
      <section>
        <h3>Additional Comparison Sources</h3>
        <ul>{additional}</ul>
      </section>
    </div>"""

def render_html(payload):
    cards = []
    for chart in payload["charts"]:
        if chart.get("type") in {"stream_interactive", "metric_interactive"}:
            cards.append(render_interactive_section(chart))
            continue
        if chart.get("type") == "paged_grouped_bar":
            cards.append(render_paged_grouped_section(chart))
            continue
        if chart.get("type") == "matrix_interactive":
            cards.append(render_matrix_section(chart))
            continue
        cards.append(f'''
      <section class="chart">
        <h2>{esc(chart["title"])}</h2>
        <p>{esc(chart["subtitle"])}</p>
        <img src="../charts/{esc(chart["id"])}.svg" alt="{esc(chart["title"])}">
      </section>''')

    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Xeon Max 9470C Benchmark Charts</title>
  <style>
    :root {{
      color-scheme: light;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      color: #1f2937;
      background: #f4f6f9;
    }}
    body {{
      margin: 0;
    }}
    header {{
      padding: 34px clamp(18px, 4vw, 56px) 18px;
      background: #ffffff;
      border-bottom: 1px solid #d9e0ea;
    }}
    main {{
      max-width: 1200px;
      margin: 0 auto;
      padding: 28px clamp(14px, 3vw, 32px) 56px;
    }}
    h1 {{
      margin: 0 0 8px;
      font-size: clamp(28px, 4vw, 44px);
      line-height: 1.1;
      letter-spacing: 0;
    }}
    h2 {{
      margin: 0 0 4px;
      font-size: 20px;
      letter-spacing: 0;
    }}
    p {{
      margin: 0;
      color: #596579;
      line-height: 1.55;
    }}
    .chart {{
      margin: 0 0 26px;
      padding: 22px;
      background: #ffffff;
      border: 1px solid #dce3ee;
      border-radius: 8px;
      overflow: auto;
    }}
    img {{
      display: block;
      max-width: none;
      margin-top: 16px;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      background: #fbfcfe;
    }}
    footer {{
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 clamp(14px, 3vw, 32px) 40px;
      color: #596579;
    }}
    a {{
      color: #295f98;
      overflow-wrap: anywhere;
    }}
    .abstract {{
      margin: 0 0 26px;
      padding: 24px;
      background: #ffffff;
      border: 1px solid #dce3ee;
      border-radius: 8px;
    }}
    .abstract > p {{
      max-width: 1000px;
      color: #3f4d63;
    }}
    .abstract-grid {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 16px;
      margin-top: 20px;
    }}
    .abstract-group {{
      padding: 16px;
      border: 1px solid #e0e6ef;
      border-radius: 8px;
      background: #fbfcfe;
    }}
    .abstract-group h3, footer h3 {{
      margin: 0 0 10px;
      color: #1f2937;
      font-size: 15px;
      letter-spacing: 0;
    }}
    .abstract-group ul, footer ul {{
      margin: 0;
      padding-left: 18px;
      color: #4f5e73;
      line-height: 1.55;
    }}
    .source-grid {{
      display: grid;
      grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
      gap: 24px;
    }}
    .source-grid section {{
      padding: 18px;
      border: 1px solid #dce3ee;
      border-radius: 8px;
      background: #ffffff;
    }}
    .chart-head {{
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 18px;
    }}
    .stream-tab-stack {{
      display: grid;
      gap: 8px;
      justify-items: end;
    }}
    .stream-tabs {{
      display: inline-flex;
      flex-wrap: wrap;
      gap: 6px;
      padding: 3px;
      border: 1px solid #cfd8e6;
      border-radius: 8px;
      background: #f8fafc;
    }}
    .stream-tabs button {{
      min-width: 72px;
      height: 34px;
      border: 0;
      border-radius: 6px;
      padding: 0 12px;
      background: transparent;
      color: #39465a;
      font: 700 13px Inter, ui-sans-serif, system-ui, sans-serif;
      cursor: pointer;
    }}
    .stream-tabs button.is-active {{
      background: #1f2937;
      color: #ffffff;
      box-shadow: 0 1px 2px rgba(15, 23, 42, 0.16);
    }}
    .stream-panel {{
      display: grid;
      grid-template-columns: minmax(620px, 1fr) 260px;
      gap: 26px;
      margin-top: 22px;
      min-width: 980px;
    }}
    .stream-plot {{
      padding: 18px 18px 16px;
      border: 1px solid #d8e0eb;
      border-radius: 8px;
      background: #ffffff;
    }}
    .stream-axis {{
      position: relative;
      height: 24px;
      margin: 0 148px 8px 272px;
      border-bottom: 1px solid #b7c3d4;
    }}
    .stream-axis span {{
      position: absolute;
      top: 0;
      transform: translateX(-50%);
      color: #60708a;
      font-size: 11px;
      white-space: nowrap;
    }}
    .stream-bars {{
      display: grid;
      gap: 12px;
    }}
    .stream-row {{
      display: grid;
      grid-template-columns: 260px minmax(320px, 1fr) 138px;
      align-items: center;
      gap: 12px;
    }}
    .stream-name {{
      color: #263244;
      font-weight: 700;
      font-size: 13px;
      text-align: right;
    }}
    .stream-track {{
      height: 26px;
      border-left: 1px solid #8b9bb0;
      background: repeating-linear-gradient(to right, #eef2f7 0, #eef2f7 1px, transparent 1px, transparent 25%);
    }}
    .stream-fill {{
      height: 100%;
      border-radius: 0 4px 4px 0;
      transition: width 180ms ease;
    }}
    .stream-row.is-own .stream-fill {{
      outline: 2px solid #1f2937;
      outline-offset: 1px;
    }}
    .stream-value {{
      color: #1f2937;
      font-weight: 800;
      font-size: 13px;
      text-align: right;
      font-variant-numeric: tabular-nums;
    }}
    .stream-meta {{
      padding: 18px;
      border: 1px solid #d8e0eb;
      border-radius: 8px;
      background: #fbfcfe;
    }}
    .stream-meta-label {{
      color: #6b778c;
      font-size: 12px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.06em;
    }}
    .stream-meta-title {{
      margin-top: 8px;
      color: #1f2937;
      font-size: 22px;
      font-weight: 800;
    }}
    .stream-meta code {{
      display: block;
      margin-top: 12px;
      padding: 9px 10px;
      border-radius: 6px;
      background: #eef2f7;
      color: #1f2937;
      font-size: 13px;
      white-space: normal;
    }}
    .stream-meta p {{
      margin-top: 14px;
      font-size: 13px;
    }}
    .paged-plot-wrap {{
      margin-top: 22px;
      padding: 18px;
      min-width: 980px;
      border: 1px solid #d8e0eb;
      border-radius: 8px;
      background: #ffffff;
    }}
    .paged-title {{
      color: #1f2937;
      font-size: 22px;
      font-weight: 800;
    }}
    .paged-subtitle {{
      margin-top: 5px;
      color: #60708a;
      font-size: 13px;
    }}
    .paged-plot {{
      margin-top: 16px;
      overflow-x: auto;
    }}
    .paged-plot svg {{
      display: block;
      width: 100%;
      min-width: 980px;
      height: auto;
    }}
    .paged-axis {{
      stroke: #9aa8ba;
      stroke-width: 1;
    }}
    .paged-grid {{
      stroke: #e1e7ef;
      stroke-width: 1;
    }}
    .paged-tick, .paged-unit {{
      fill: #60708a;
      font: 12px Inter, ui-sans-serif, system-ui, sans-serif;
    }}
    .paged-value {{
      fill: #1f2937;
      font: 800 12px Inter, ui-sans-serif, system-ui, sans-serif;
    }}
    .paged-xlabel {{
      fill: #364152;
      font: 11px Inter, ui-sans-serif, system-ui, sans-serif;
    }}
    .paged-note {{
      margin-top: 8px;
      color: #60708a;
      font-size: 12px;
    }}
    .matrix-controls {{
      display: grid;
      gap: 8px;
      justify-items: end;
    }}
    .mobile-bars {{
      display: none;
    }}
    @media (max-width: 720px) {{
      header {{
        padding: 24px 16px 14px;
      }}
      main {{
        padding: 18px 10px 36px;
      }}
      footer {{
        padding: 0 10px 28px;
      }}
      h1 {{
        font-size: 30px;
      }}
      h2 {{
        font-size: 18px;
        line-height: 1.2;
      }}
      .chart, .abstract {{
        padding: 14px;
        margin-bottom: 16px;
        overflow: visible;
      }}
      .chart-head {{
        display: block;
      }}
      .stream-tab-stack {{
        justify-items: stretch;
        gap: 7px;
      }}
      .stream-tabs {{
        display: flex;
        flex-wrap: nowrap;
        gap: 5px;
        margin-top: 12px;
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
        scrollbar-width: thin;
      }}
      .stream-tab-stack .stream-tabs {{
        margin-top: 0;
      }}
      .stream-tabs button {{
        flex: 0 0 auto;
        min-width: auto;
        height: 32px;
        padding: 0 10px;
        font-size: 12px;
        white-space: nowrap;
      }}
      .matrix-controls {{
        justify-items: stretch;
      }}
      .stream-panel {{
        min-width: 0;
        grid-template-columns: minmax(0, 1fr);
        gap: 12px;
        margin-top: 14px;
      }}
      .stream-plot {{
        min-width: 0;
        padding: 12px;
      }}
      .stream-axis {{
        display: none;
      }}
      .stream-bars {{
        gap: 9px;
      }}
      .stream-row {{
        grid-template-columns: minmax(0, 1fr) auto;
        grid-template-areas: "name value" "bar bar";
        gap: 7px 10px;
        padding: 10px;
        border: 1px solid #e0e6ef;
        border-radius: 7px;
        background: #fbfcfe;
      }}
      .stream-name {{
        grid-area: name;
        text-align: left;
        font-size: 12px;
        line-height: 1.25;
        overflow-wrap: anywhere;
      }}
      .stream-track {{
        grid-area: bar;
        min-width: 0;
        height: 20px;
      }}
      .stream-value {{
        grid-area: value;
        align-self: start;
        max-width: 126px;
        font-size: 12px;
        line-height: 1.25;
        text-align: right;
        overflow-wrap: anywhere;
      }}
      .stream-meta {{
        padding: 12px;
      }}
      .stream-meta-title, .paged-title {{
        font-size: 18px;
      }}
      .paged-plot-wrap {{
        min-width: 0;
        padding: 12px;
        margin-top: 14px;
      }}
      .paged-plot {{
        overflow: visible;
      }}
      .paged-plot svg {{
        display: none;
      }}
      .mobile-bars {{
        display: grid;
        gap: 9px;
      }}
      .mobile-bar-row {{
        display: grid;
        grid-template-columns: minmax(0, 1fr) auto;
        grid-template-areas: "label value" "track track";
        gap: 7px 10px;
        padding: 10px;
        border: 1px solid #e0e6ef;
        border-radius: 7px;
        background: #fbfcfe;
      }}
      .mobile-bar-row.is-own .mobile-bar-fill {{
        outline: 2px solid #1f2937;
        outline-offset: 1px;
      }}
      .mobile-bar-label {{
        grid-area: label;
        color: #263244;
        font-size: 12px;
        font-weight: 700;
        line-height: 1.25;
        overflow-wrap: anywhere;
      }}
      .mobile-bar-value {{
        grid-area: value;
        max-width: 118px;
        color: #1f2937;
        font-size: 12px;
        font-weight: 800;
        line-height: 1.25;
        text-align: right;
        overflow-wrap: anywhere;
        font-variant-numeric: tabular-nums;
      }}
      .mobile-bar-track {{
        grid-area: track;
        height: 20px;
        border-left: 1px solid #8b9bb0;
        background: repeating-linear-gradient(to right, #eef2f7 0, #eef2f7 1px, transparent 1px, transparent 24px);
      }}
      .mobile-bar-fill {{
        height: 100%;
        border-radius: 0 4px 4px 0;
      }}
      .abstract-grid, .source-grid {{
        grid-template-columns: 1fr;
      }}
      .abstract-group, .source-grid section {{
        padding: 13px;
      }}
    }}
  </style>
</head>
<body>
  <header>
    <h1>Xeon Max 9470C Benchmark Charts</h1>
    <p>{esc(payload["metadata"]["system"])}. Data date: {esc(payload["metadata"]["date"])}; last updated: {esc(payload["metadata"]["last_updated"])}.</p>
  </header>
  <main>
{render_abstract(payload)}
{''.join(cards)}
  </main>
  <footer>
{render_sources(payload)}
  </footer>
{stream_interaction_script()}
{paged_grouped_script()}
{matrix_interaction_script()}
</body>
</html>'''


def main():
    payload = json.loads(DATA_FILE.read_text())
    CHART_DIR.mkdir(exist_ok=True)
    REPORT_DIR.mkdir(exist_ok=True)

    for chart in payload["charts"]:
        if chart.get("type") in {"stream_interactive", "metric_interactive", "paged_grouped_bar", "matrix_interactive"}:
            continue
        svg = render_bar_chart(chart)
        (CHART_DIR / f"{chart['id']}.svg").write_text(svg)

    (REPORT_DIR / "index.html").write_text(render_html(payload))
    print(f"Rendered {len(payload['charts'])} charts to {CHART_DIR}")
    print(f"Report: {REPORT_DIR / 'index.html'}")


if __name__ == "__main__":
    main()
