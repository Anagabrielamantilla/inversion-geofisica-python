#!/usr/bin/env python3
"""Build the animated, self-contained SVG used in README."""

import base64
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs/assets/architecture-ai-base.png"
OUTPUT = ROOT / "docs/assets/architecture-conceptual.svg"


def main():
    encoded = base64.b64encode(SOURCE.read_bytes()).decode("ascii")
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="675" viewBox="0 0 1200 675" role="img" aria-labelledby="title desc">
  <title id="title">Arquitectura animada de inversión geofísica guiada por física e inteligencia artificial</title>
  <desc id="desc">Flujo desde datos observados hasta simulación, inversión con inteligencia artificial y validación sobre un modelo tridimensional del subsuelo.</desc>
  <defs>
    <linearGradient id="shade" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#02071d" stop-opacity=".98"/><stop offset=".72" stop-color="#02071d" stop-opacity=".72"/><stop offset="1" stop-color="#02071d" stop-opacity="0"/></linearGradient>
    <linearGradient id="panel" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#071945" stop-opacity=".96"/><stop offset="1" stop-color="#04102f" stop-opacity=".88"/></linearGradient>
    <filter id="glow" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <filter id="shadow" x="-20%" y="-30%" width="140%" height="170%"><feDropShadow dx="0" dy="8" stdDeviation="8" flood-color="#000" flood-opacity=".55"/></filter>
    <style>
      text{{font-family:Arial,Helvetica,sans-serif}}
      .title{{font-size:38px;font-weight:800;fill:#fff;letter-spacing:.5px}}
      .accent{{font-size:37px;font-weight:800;fill:#35ddff;letter-spacing:.5px}}
      .subtitle{{font-size:17px;fill:#cdeaff}}
      .node-title{{font-size:21px;font-weight:800;fill:#fff}}
      .node-body{{font-size:14px;fill:#d5eaff}}
      .chip{{font-size:13px;font-weight:700;fill:#ecfaff}}
      .equation{{font-size:20px;font-weight:800;fill:#fff}}
      .eyebrow{{font-size:13px;font-weight:800;fill:#ffc84d}}
      .flow{{fill:none;stroke:#36ddff;stroke-width:3;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:10 12;animation:dash 2.4s linear infinite}}
      .pulse{{animation:pulse 2.8s ease-in-out infinite;transform-box:fill-box;transform-origin:center}}
      .n1{{animation-delay:0s}}.n2{{animation-delay:.7s}}.n3{{animation-delay:1.4s}}.n4{{animation-delay:2.1s}}
      .data{{filter:url(#glow);animation:travel 4s linear infinite}}
      .data2{{animation-delay:-1.33s}}.data3{{animation-delay:-2.66s}}
      .network{{animation:network 3.2s ease-in-out infinite}}
      @keyframes dash{{to{{stroke-dashoffset:-44}}}}
      @keyframes pulse{{0%,100%{{opacity:.78}}50%{{opacity:1;filter:url(#glow)}}}}
      @keyframes travel{{0%{{offset-distance:0%}}100%{{offset-distance:100%}}}}
      @keyframes network{{0%,100%{{opacity:.45}}50%{{opacity:1}}}}
      @media (prefers-reduced-motion:reduce){{.flow,.pulse,.data,.network{{animation:none}}}}
    </style>
    <path id="dataPath" d="M218 246 L218 270 L218 360 L218 385 L218 475 L218 500 L390 545 L505 545"/>
  </defs>

  <image href="data:image/png;base64,{encoded}" x="0" y="0" width="1200" height="675" preserveAspectRatio="xMidYMid slice"/>
  <rect width="520" height="675" fill="url(#shade)"/>
  <rect width="1200" height="675" fill="#020817" opacity=".16"/>

  <g class="network" stroke="#36ddff" stroke-width="1.5" opacity=".65">
    <path d="M520 55 L650 28 L780 70 L905 23 L1030 64 L1160 35" fill="none"/>
    <path d="M650 28 L710 112 L780 70 L850 120 L905 23 L975 116 L1030 64" fill="none"/>
    <g fill="#86eeff" filter="url(#glow)"><circle cx="520" cy="55" r="3"/><circle cx="650" cy="28" r="4"/><circle cx="710" cy="112" r="3"/><circle cx="780" cy="70" r="4"/><circle cx="850" cy="120" r="3"/><circle cx="905" cy="23" r="4"/><circle cx="975" cy="116" r="3"/><circle cx="1030" cy="64" r="4"/><circle cx="1160" cy="35" r="3"/></g>
  </g>

  <text x="45" y="63" class="title">ARQUITECTURA DE INVERSIÓN</text>
  <text x="47" y="112" class="accent">GEOFÍSICA + IA GUIADA POR FÍSICA</text>
  <text x="49" y="142" class="subtitle">del dato observado al modelo confiable del subsuelo</text>

  <g class="pulse n1" filter="url(#shadow)"><rect x="45" y="156" width="345" height="90" rx="18" fill="url(#panel)" stroke="#2de3ff" stroke-width="3"/><circle cx="77" cy="191" r="17" fill="#26d9f7"/><text x="103" y="191" class="node-title">1  OBSERVAR</text><text x="64" y="225" class="node-body">datos, geometría, ruido e incertidumbre</text></g>
  <g class="pulse n2" filter="url(#shadow)"><rect x="45" y="271" width="345" height="90" rx="18" fill="url(#panel)" stroke="#8574ff" stroke-width="3"/><circle cx="77" cy="306" r="17" fill="#8574ff"/><text x="103" y="306" class="node-title">2  SIMULAR</text><text x="64" y="340" class="node-body">operador directo diferenciable F(m)</text></g>
  <g class="pulse n3" filter="url(#shadow)"><rect x="45" y="386" width="345" height="90" rx="18" fill="url(#panel)" stroke="#ffc13d" stroke-width="3"/><circle cx="77" cy="421" r="17" fill="#ffc13d"/><text x="103" y="421" class="node-title">3  INVERTIR + IA</text><text x="64" y="455" class="node-body">desajuste + regularización + physics-guided</text></g>
  <g class="pulse n4" filter="url(#shadow)"><rect x="45" y="501" width="345" height="90" rx="18" fill="url(#panel)" stroke="#24dcca" stroke-width="3"/><circle cx="77" cy="536" r="17" fill="#24dcca"/><text x="103" y="536" class="node-title">4  VALIDAR</text><text x="64" y="570" class="node-body">residuales, resolución e interpretación</text></g>

  <use href="#dataPath" class="flow"/>
  <circle r="5" fill="#fff" stroke="#28e5ff" stroke-width="3" class="data" style="offset-path:path('M218 246 L218 270 L218 360 L218 385 L218 475 L218 500 L390 545 L505 545')"/>
  <circle r="5" fill="#fff" stroke="#28e5ff" stroke-width="3" class="data data2" style="offset-path:path('M218 246 L218 270 L218 360 L218 385 L218 475 L218 500 L390 545 L505 545')"/>
  <circle r="5" fill="#fff" stroke="#28e5ff" stroke-width="3" class="data data3" style="offset-path:path('M218 246 L218 270 L218 360 L218 385 L218 475 L218 500 L390 545 L505 545')"/>

  <g filter="url(#shadow)"><rect x="505" y="500" width="645" height="110" rx="22" fill="#03112f" fill-opacity=".91" stroke="#43e2ff" stroke-width="3"/><text x="532" y="530" class="eyebrow">OBJETIVO GUIADO POR FÍSICA</text><text x="532" y="563" class="equation">Φ(m) = DESAJUSTE DE DATOS + β · PRIOR FÍSICO</text><text x="532" y="592" class="subtitle" fill="#79e9ff">física directa ↔ optimización ↔ incertidumbre</text></g>

  <g><rect x="520" y="625" width="130" height="31" rx="13" fill="#071b49" stroke="#4bdfff"/><text x="532" y="646" class="chip">GRAVIMETRÍA 3D</text><rect x="662" y="625" width="155" height="31" rx="13" fill="#071b49" stroke="#4bdfff"/><text x="674" y="646" class="chip">MAGNETOMETRÍA 3D</text><rect x="829" y="625" width="75" height="31" rx="13" fill="#071b49" stroke="#4bdfff"/><text x="844" y="646" class="chip">MT 1D</text><rect x="916" y="625" width="195" height="31" rx="13" fill="#071b49" stroke="#4bdfff"/><text x="930" y="646" class="chip">FWI + DEEP LEARNING</text></g>
</svg>'''
    OUTPUT.write_text(svg, encoding="utf-8")
    print(f"Created {OUTPUT} ({OUTPUT.stat().st_size / 1024 / 1024:.1f} MB)")


if __name__ == "__main__":
    main()
