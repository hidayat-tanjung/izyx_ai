# ⚡ IZYX AI — Ultimate Project Merger

![Version](https://img.shields.io/badge/version-1.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen)
![Contributors](https://img.shields.io/github/contributors/hidayat-tanjung/izyx_ai)
![Issues](https://img.shields.io/github/issues/hidayat-tanjung/izyx_ai)
![Forks](https://img.shields.io/github/forks/hidayat-tanjung/izyx_ai)
![Stars](https://img.shields.io/github/stars/hidayat-tanjung/izyx_ai)

> 🔥 All-in-One Project Manager dengan AI Vibes — Live Preview, Search, Filter, Dark/Light Mode, Auto-Deploy.

---

## 📖 Apa Itu IZYX AI?

**IZYX AI Ultimate Project Merger** adalah script Python yang mengorganisir dan menampilkan semua proyek dalam satu portal web interaktif. Dengan satu perintah, Anda bisa:

- ✅ Menambahkan proyek web, backend, atau script
- ✅ Menampilkan semua proyek dalam satu halaman dengan Live Preview
- ✅ Mencari dan memfilter proyek berdasarkan kategori
- ✅ Mengaktifkan Dark/Light Mode
- ✅ Melakukan auto-deploy ke Vercel dan Netlify

---

## ✨ Fitur Utama

| Fitur | Deskripsi |
|-------|-----------|
| **Live Preview** | Lihat proyek langsung di modal |
| **Search Bar** | Cari proyek (Ctrl+K untuk fokus) |
| **Filter** | Kategori: Web, Backend, Script |
| **Dark/Light Mode** | Toggle tema dengan satu klik |
| **Auto-Deploy** | Vercel, Netlify, atau keduanya |
| **Responsive** | Optimal di HP, tablet, dan desktop |
| **Keyboard Shortcuts** | Ctrl+K (search), Escape (close) |

---

## 🚀 Quick Start

### 1. Instalasi
```bash
git clone https://github.com/hidayat-tanjung/izyx_ai.git
cd izyx_ai
python3 izyx_ai.py
```

### 2. Buka Portal
- Buka `index.html` di browser
- Portal otomatis menampilkan semua proyek

### 3. Navigasi
- **Search** — Ketik nama atau kategori
- **Filter** — Klik All, Web, Backend, atau Script
- **Preview** — Klik kartu proyek untuk Live Preview
- **Deploy** — Klik tombol Deploy untuk upload

---

## 📦 Menambahkan Proyek Baru

Edit file `izyx_ai.py` dan tambahkan proyek:

```python
merger.add_project(
    "nama-proyek",
    {
        "index.html": "<html>...</html>",
        "style.css": "body{...}",
        "script.js": "console.log('...');"
    },
    category="web"  # web, backend, atau script
)
```

Jalankan ulang script:
```bash
python3 izyx_ai.py
```

---

## 📁 Struktur Folder

```
izyx-all-projects/
├── projects/          # Semua proyek web
├── backend/           # File backend
├── scripts/           # File script
├── assets/            # Gambar, CSS, JS
├── docs/              # Dokumentasi
├── index.html         # Portal utama
├── README.md          # File ini
└── .gitignore
```

---

## 🧩 Proyek Contoh

Beberapa proyek yang sudah termasuk:

| Nama | Kategori | Deskripsi |
|------|----------|-----------|
| project-website-1 | Web | Website dasar dengan animasi |
| project-login-page | Web | Halaman login |
| project-portofolio | Web | Portofolio pribadi |
| server.py | Backend | Flask API |
| api.js | Backend | Express API |
| deploy.py | Script | Deploy simulator |
| scraper.js | Script | Web scraper |

---

## 💻 Penggunaan Portal

### Search & Filter
- Ketik di search bar untuk mencari proyek
- Klik filter kategori (All, Web, Backend, Script)

### Live Preview
- Klik kartu proyek untuk membuka modal
- Tab: Preview, HTML, CSS, JS
- Tekan Escape atau ✕ untuk menutup

### Auto-Deploy
- Klik tombol Deploy (Vercel/Netlify/Keduanya)
- Status deploy ditampilkan di bawah tombol

---

## ⚙️ Konfigurasi

### Ubah Nama Repository
```python
merger = IzyxMergerUltimate(repo_name="nama-baru")
```

### Ubah Tema Default
```html
<html lang="id" data-theme="light">  <!-- dark atau light -->
```

---

## 🧪 Testing Lokal

```bash
python3 -m http.server 8080
```

Buka: `http://localhost:8080`

---

## 🤝 Contributing

1. **Fork** repository ini
2. **Clone** ke lokal: `git clone https://github.com/username/izyx_ai.git`
3. **Buat branch**: `git checkout -b fitur-baru`
4. **Commit**: `git add . && git commit -m "Tambah fitur"`
5. **Push**: `git push origin fitur-baru`
6. **Pull Request** di GitHub

---

## 📝 Lisensi

MIT License — Bebas untuk penggunaan pribadi dan komersial.

---

**Made with 🔥 by IZYX AI — 2050**
