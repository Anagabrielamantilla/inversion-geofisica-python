#!/usr/bin/env python3
"""Build the animated physics-guided inversion architecture used by README."""

from pathlib import Path
from math import sin, pi

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs/assets/architecture-ai-base.png"
OUTPUT = ROOT / "docs/assets/architecture-conceptual.gif"
W, H = 1200, 675
OUTPUT_W, OUTPUT_H = 1000, 563
FRAMES = 30

FONT = "/System/Library/Fonts/Supplemental/Arial.ttf"
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"


def font(size, bold=False):
    return ImageFont.truetype(FONT_BOLD if bold else FONT, size)


TITLE = font(37, True)
SUBTITLE = font(18)
NODE_TITLE = font(20, True)
NODE_BODY = font(14)
EQUATION = font(20, True)
CHIP = font(13, True)


def rounded_panel(layer, box, fill, outline, width=2, radius=18):
    layer.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def glow_dot(frame, xy, color, radius=7):
    glow = Image.new("RGBA", frame.size, (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    x, y = xy
    gd.ellipse((x-radius*3, y-radius*3, x+radius*3, y+radius*3), fill=(*color, 85))
    glow = glow.filter(ImageFilter.GaussianBlur(radius*1.8))
    frame.alpha_composite(glow)
    d = ImageDraw.Draw(frame)
    d.ellipse((x-radius, y-radius, x+radius, y+radius), fill=(*color, 255))
    d.ellipse((x-radius/2, y-radius/2, x+radius/2, y+radius/2), fill=(255, 255, 255, 255))


def point_on_polyline(points, t):
    lengths = []
    total = 0
    for a, b in zip(points, points[1:]):
        length = ((b[0]-a[0])**2 + (b[1]-a[1])**2) ** 0.5
        lengths.append(length)
        total += length
    distance = (t % 1.0) * total
    for (a, b), length in zip(zip(points, points[1:]), lengths):
        if distance <= length:
            u = distance / length if length else 0
            return (a[0] + (b[0]-a[0])*u, a[1] + (b[1]-a[1])*u)
        distance -= length
    return points[-1]


def main():
    source = Image.open(SOURCE).convert("RGB")
    # Crop to 16:9 and resize. Slightly mute it so overlays remain legible.
    crop_h = int(source.width * 9 / 16)
    top = max(0, (source.height - crop_h) // 2)
    base = source.crop((0, top, source.width, top + crop_h)).resize((W, H), Image.Resampling.LANCZOS)
    base = ImageEnhance.Brightness(base).enhance(0.72).convert("RGBA")

    nodes = [
        ((45, 155, 390, 245), "1  OBSERVAR", "datos, geometría, ruido e incertidumbre"),
        ((45, 270, 390, 360), "2  SIMULAR", "operador directo diferenciable  F(m)"),
        ((45, 385, 390, 475), "3  INVERTIR + IA", "misfit + regularización + physics-guided"),
        ((45, 500, 390, 590), "4  VALIDAR", "residuales, resolución e interpretación"),
    ]
    path = [(218, 245), (218, 270), (218, 360), (218, 385), (218, 475), (218, 500),
            (390, 545), (525, 545), (645, 500), (745, 410)]
    colors = [(30, 222, 255), (135, 116, 255), (255, 186, 62), (44, 236, 184)]
    out = []

    for idx in range(FRAMES):
        phase = idx / FRAMES
        frame = base.copy()
        overlay = Image.new("RGBA", frame.size, (0, 0, 0, 0))
        d = ImageDraw.Draw(overlay)

        # Gradient-like dark glass on the left.
        for x in range(0, 465, 5):
            alpha = int(205 * (1 - x / 500) + 30)
            d.rectangle((x, 0, x+5, H), fill=(2, 8, 31, max(30, alpha)))

        d.text((45, 34), "ARQUITECTURA DE INVERSIÓN", font=TITLE, fill=(255, 255, 255, 255))
        d.text((47, 82), "GEOFÍSICA + IA GUIADA POR FÍSICA", font=TITLE, fill=(58, 223, 255, 255))
        d.text((49, 127), "del dato observado al modelo confiable del subsuelo", font=SUBTITLE,
               fill=(195, 228, 255, 255))

        active = int(phase * 4) % 4
        for n, (box, heading, body) in enumerate(nodes):
            color = colors[n]
            pulse = (sin(phase * 2*pi*4 - n*pi/2) + 1) / 2
            is_active = n == active
            fill_alpha = 215 if is_active else 168
            outline = tuple(min(255, int(c + 55*pulse)) for c in color) + (255,)
            rounded_panel(d, box, (5, 18, 56, fill_alpha), outline, 4 if is_active else 2)
            x1, y1, _, _ = box
            d.ellipse((x1+15, y1+19, x1+47, y1+51), fill=(*color, 255))
            d.text((x1+58, y1+16), heading, font=NODE_TITLE, fill=(255, 255, 255, 255))
            d.text((x1+20, y1+57), body, font=NODE_BODY, fill=(205, 231, 249, 255))

        # Animated connecting backbone.
        d.line(path, fill=(42, 220, 255, 185), width=3, joint="curve")
        frame.alpha_composite(overlay)
        for offset in (0, 0.33, 0.66):
            glow_dot(frame, point_on_polyline(path, phase + offset), (43, 224, 255), 5)

        # Central physics-guided equation over the geological model.
        eq = Image.new("RGBA", frame.size, (0, 0, 0, 0))
        ed = ImageDraw.Draw(eq)
        glow_alpha = int(185 + 50 * (sin(phase * 2*pi) + 1) / 2)
        rounded_panel(ed, (505, 500, 1150, 610), (3, 13, 45, 205), (72, 225, 255, glow_alpha), 3, 22)
        ed.text((532, 518), "OBJETIVO GUIADO POR FÍSICA", font=CHIP, fill=(255, 199, 74, 255))
        ed.text((532, 545), "Φ(m) = DESAJUSTE DE DATOS + β · PRIOR FÍSICO", font=EQUATION,
                fill=(255, 255, 255, 255))
        ed.text((532, 577), "física directa  ↔  optimización  ↔  incertidumbre", font=SUBTITLE,
                fill=(118, 231, 255, 255))

        # Method chips.
        labels = ["GRAVIMETRÍA 3D", "MAGNETOMETRÍA 3D", "MT 1D", "FWI + DEEP LEARNING"]
        widths = [130, 155, 75, 195]
        x = 520
        for label, width in zip(labels, widths):
            rounded_panel(ed, (x, 625, x+width, 655), (9, 25, 72, 220), (76, 213, 255, 210), 2, 12)
            ed.text((x+10, 632), label, font=CHIP, fill=(235, 249, 255, 255))
            x += width + 12
        frame.alpha_composite(eq)

        # Small moving data particles across the subsurface.
        for j in range(10):
            px = 470 + ((j*89 + idx*13) % 700)
            py = 165 + int(45*sin(j*0.9 + phase*2*pi)) + (j % 4)*60
            glow_dot(frame, (px, py), (30, 194, 255), 2)

        out.append(frame.convert("RGB").resize((OUTPUT_W, OUTPUT_H), Image.Resampling.LANCZOS))

    out[0].save(
        OUTPUT,
        save_all=True,
        append_images=out[1:],
        duration=110,
        loop=0,
        optimize=True,
        disposal=2,
    )
    print(f"Created {OUTPUT} ({OUTPUT.stat().st_size / 1024 / 1024:.1f} MB)")


if __name__ == "__main__":
    main()
