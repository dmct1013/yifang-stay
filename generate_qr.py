#!/usr/bin/env python3
"""
生成各導覽點的 QR code（品牌磚紅色）
用法：python3 generate_qr.py <網站網址>
範例：python3 generate_qr.py https://dmct1013.github.io/yifang-tour/
會在 qr/ 產生 home.png 與 stop1.png ~ stopN.png，每張對應 <網址>#編號。
"""
import json, os, sys
import qrcode

HERE = os.path.dirname(os.path.abspath(__file__))
BRICK = (186, 75, 47)     # 陳磚紅 #BA4B2F
PAPER = (247, 243, 236)   # 稻埕白 #F7F3EC

def make(url, path):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=14, border=3)
    qr.add_data(url); qr.make(fit=True)
    img = qr.make_image(fill_color=BRICK, back_color=PAPER)
    img.save(path)
    print(f"  {os.path.basename(path):14s} → {url}")

def main():
    if len(sys.argv) < 2:
        print("用法：python3 generate_qr.py <網站網址>\n例：python3 generate_qr.py https://dmct1013.github.io/yifang-tour/")
        sys.exit(1)
    base = sys.argv[1].rstrip("/") + "/"
    with open(os.path.join(HERE, "stops.json"), encoding="utf-8") as f:
        data = json.load(f)
    out = os.path.join(HERE, "qr"); os.makedirs(out, exist_ok=True)

    make(base, os.path.join(out, "home.png"))
    for s in data["stops"]:
        make(base + "#" + str(s["id"]), os.path.join(out, f"stop{s['id']}.png"))
    print("完成，共", len(data["stops"]) + 1, "張 QR。")

if __name__ == "__main__":
    main()
