# 陳宅歷史導覽（立架 + QR）

百年合院「古坑東和陳宅」的現地導覽。採「立架 + QR」二合一：立架放精華簡介（長輩也看得懂），QR 掃進手機網頁聽國語語音導覽、看老照片、讀完整故事。全部本機免費製作，丟 GitHub Pages 託管。

## 檔案

| 路徑 | 內容 |
|------|------|
| `stops.json` | **唯一內容源頭**——6 站的標題、精華、故事文字、圖檔/音檔名。改故事只改這裡 |
| `index.html` | 手機版導覽網頁（讀 stops.json，`#1`~`#6` 各站，hash 路由） |
| `audio/stopN.mp3` | 國語語音導覽（macOS 美佳語音生成） |
| `img/stopN.jpg` | 各站照片（**待補**：拍好後丟進來，檔名對齊 stops.json） |
| `qr/*.png` | 各站 QR（磚紅色，貼到立架用） |
| `generate_audio.py` | 重生語音：`python3 generate_audio.py` |
| `generate_qr.py` | 重生 QR：`python3 generate_qr.py <網址>` |
| `立架文案.md` | 立架印製用文案與版面建議 |

## 改內容後重生

```bash
# 改完 stops.json 的故事文字後：
python3 generate_audio.py                              # 重生語音
python3 generate_qr.py https://你的網址/               # 站數有變才需要重生 QR
```

## 本機預覽

```bash
python3 -m http.server 8765      # 在 tour/ 資料夾執行
# 瀏覽器開 http://localhost:8765/
```
（直接雙擊 index.html 用 file:// 開會載入不到 stops.json，要走 http。）

## 部署到 GitHub Pages

比照採購系統做法（推到獨立公開 repo）。建議建一個公開 repo 例如 `yifang-tour`：

```bash
# 把 tour/ 整包內容（含 audio/、img/、stops.json、index.html）放進公開 repo 根目錄
# repo 設定 → Pages → 來源選 main branch / root
# 上線網址：https://<帳號>.github.io/<repo>/
```

上線後用真實網址重跑 `generate_qr.py`，把 `qr/` 的 QR 重印到立架。

## 待辦

- [ ] 拍 6 站照片，存成 `img/stop1.jpg`~`stop6.jpg`（4:3 最佳）
- [ ] 建公開 repo、設定 GitHub Pages、取得正式網址
- [ ] 用正式網址重跑 `generate_qr.py`
- [ ] 立架印製（文案見 `立架文案.md`）
- [ ] （選配）台語語音版：找在地長輩錄音，或補做台語 TTS
