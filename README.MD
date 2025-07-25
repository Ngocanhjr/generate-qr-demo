# 🔲 QR Code Generator

A simple Python application using Tkinter to generate QR codes from links.  
Users can input a link and a file name, and the app will create and display a PNG image of the QR code.

---

## 🚀 Download

👉 Go to the [Releases](https://github.com/Ngocanhjr/generate-qr-demo/releases) section and download the `.exe` file to use the app directly — no Python installation required.

---

## ⚙️ Installation

> If you want to run or modify the source code locally.

### 1. Clone the repository

```bash
git clone https://github.com/Ngocanhjr/generate-qr-demo.git
cd generate-qr-demo/test
```

### 2. Install dependencies

```bash
pip install customtkinter pyqrcode pillow
```
### 3. Run the app

```bash
python tt.py
```

## 📦 Packaging as `.exe` (Optional)

To generate a standalone `.exe` file using **PyInstaller**:

```bash
pyinstaller --noconsole --onefile tt.py
```
After building, the `.exe` file will be located in the dist/ directory.

© 2025 by Ngocanhjr
