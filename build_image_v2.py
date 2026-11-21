#!/usr/bin/env python3
"""Build v2: same 4 verified stories, now with illustrated scenes."""
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter
import os

BASE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(BASE, "assets")
OUT = os.path.join(BASE, "image.png")

def font(name, size):
    return ImageFont.truetype(f"/usr/share/fonts/truetype/dejavu/{name}", size)

F_TITLE = font("DejaVuSans-Bold.ttf", 54)
F_DATE = font("DejaVuSans-Bold.ttf", 24)
F_KICK = font("DejaVuSans-Bold.ttf", 20)
F_HERO = font("DejaVuSans-Bold.ttf", 52)
F_HERO2 = font("DejaVuSans-Bold.ttf", 32)
F_BODY = font("DejaVuSans.ttf", 24)
F_HEAD = font("DejaVuSans-Bold.ttf", 29)
F_PBODY = font("DejaVuSans.ttf", 21)
F_FOOT = font("DejaVuSans-Bold.ttf", 19)
F_SMALL = font("DejaVuSans.ttf", 18)

def load(name):
    import glob
    f = glob.glob(os.path.join(ASSETS, f"media-generation-{name}-*.png"))[0]
    return Image.open(f).convert("RGB")

def crop_fill(im, w, h):
    return ImageOps.fit(im, (w, h), method=Image.LANCZOS, centering=(0.5, 0.45))

W, H = 1024, 1024
img = Image.new("RGB", (W, H), (248, 247, 242))
d = ImageDraw.Draw(img, "RGBA")

# Header
d.rectangle([0, 0, W, 118], fill=(15, 32, 64))
d.rectangle([0, 118, W, 126], fill=(214, 48, 49))
d.text((24, 18), "WORLD NEWS", font=F_TITLE, fill=(255, 255, 255))
d.text((24, 80), "SATURDAY  •  21 NOVEMBER 2026", font=F_DATE, fill=(255, 214, 90))
d.text((W-24, 22), "4 TOP STORIES", font=font("DejaVuSans-Bold.ttf", 26), fill=(255, 255, 255), anchor="ra")
d.text((W-24, 58), "21 NOV 2026", font=F_SMALL, fill=(180, 200, 230), anchor="ra")

# Hero GTA
hx0, hy0, hx1, hy1 = 24, 140, 1000, 500
hero = crop_fill(load("gta-vice-city-sunset"), hx1-hx0, hy1-hy0)
img.paste(hero, (hx0, hy0))
# dark gradient strips top/bottom for text
d.rectangle([hx0, hy0, hx1, hy0+92], fill=(15, 32, 64, 210))
d.rectangle([hx0, hy1-118, hx1, hy1], fill=(15, 32, 64, 225))
d.text((hx0+20, hy0+12), "GTA VI  •  VICE CITY", font=F_KICK, fill=(255, 214, 90))
d.text((hx0+20, hy0+38), "GTA VI BREAKS RECORDS", font=F_HERO, fill=(255, 255, 255))
d.text((hx0+20, hy1-106), "$3.79 BILLION IN ONE DAY", font=F_HERO2, fill=(255, 255, 255))
d.text((hx0+20, hy1-66), "Metacritic 99  •  32.5M pre-orders", font=F_BODY, fill=(230, 235, 245))
d.text((hx0+20, hy1-36), "Biggest entertainment launch ever", font=F_BODY, fill=(230, 235, 245))

def panel(x0, y0, x1, y1, asset, color, kicker, headline, body, footer):
    d.rectangle([x0, y0, x1, y1], fill=(255, 255, 255), outline=(200, 200, 195), width=2)
    scene = crop_fill(load(asset), x1-x0, 170)
    img.paste(scene, (x0, y0))
    d.rectangle([x0, y0+170, x1, y0+170+40], fill=color)
    d.text((x0+14, y0+178), kicker, font=F_KICK, fill=(255, 255, 255))
    y = y0 + 226
    for line in headline:
        d.text((x0+14, y), line, font=F_HEAD, fill=(15, 32, 64))
        y += 36
    y += 6
    for line in body:
        d.text((x0+14, y), line, font=F_PBODY, fill=(60, 60, 60))
        y += 28
    d.rectangle([x0, y1-48, x1, y1], fill=color)
    d.text((x0+14, y1-36), footer, font=F_FOOT, fill=(255, 255, 255))

py0, py1 = 516, 1000
pw = (1000-24-32)//3
x0 = 24
panel(x0, py0, x0+pw, py1, "poland-nato-sky", (178, 34, 34), "POLAND  •  NATO",
      ["Russia missiles", "strike Poland"],
      ["NATO responds as", "missiles cross into", "Polish airspace."],
      "NATO ON ALERT")
x0 += pw + 16
panel(x0, py0, x0+pw, py1, "icj-court-justice", (15, 32, 64), "MYANMAR  •  ICJ",
      ["World Court:", "Myanmar guilty"],
      ["of genocide against", "the Rohingya,", "in a 9–6 ruling."],
      "9–6 VERDICT")
x0 += pw + 16
panel(x0, py0, x0+pw, py1, "eu-ukraine-aid", (0, 90, 70), "UKRAINE  •  EU",
      ["EU approves", "€1bn aid"],
      ["for Ukraine — new", "weapons funding as", "Kyiv faces strikes."],
      "€1,000,000,000")

# Try PNG first; if >1MiB, save as JPEG bytes under .png name (allowed by RULES)
img.save(OUT, "PNG", optimize=True)
size = os.path.getsize(OUT)
print("PNG", img.size, size)
if size > 1048576:
    img.save(OUT, "JPEG", quality=88, optimize=True)
    print("JPEG-as-entry.png", os.path.getsize(OUT))
