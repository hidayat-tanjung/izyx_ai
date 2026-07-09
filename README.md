# ⚡ IZYX AI — Ultimate Project Manager

![Version](https://img.shields.io/badge/version-2.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen)
![Templates](https://img.shields.io/badge/templates-30%2B-orange)
![Contributors](https://img.shields.io/github/contributors/hidayat-tanjung/izyx_ai)
![Stars](https://img.shields.io/github/stars/hidayat-tanjung/izyx_ai)

> 🔥 **All-in-One Project Manager dengan AI Vibes** — 30+ Templates • Live Preview • Search • Filter • Dark/Light Mode • Auto-Deploy • Zero Dependencies

---

## 📖 Apa Itu IZYX AI?

**IZYX AI Ultimate Project Manager** adalah Python script yang mengorganisir dan menampilkan semua proyek dalam satu portal web interaktif modern. Dengan satu perintah, Anda bisa:

- ✅ Membuat 30+ template website siap pakai (landing page, portfolio, dashboard, blog, e-commerce, dll)
- ✅ Menampilkan semua proyek dalam satu dashboard interaktif dengan Live Preview
- ✅ Mencari dan memfilter proyek berdasarkan kategori secara real-time
- ✅ Mengaktifkan Dark/Light Mode dengan theme persistence
- ✅ Melihat kode HTML, CSS, JavaScript di modal dengan syntax highlighting
- ✅ Deploy langsung ke Vercel dan Netlify dengan satu klik
- ✅ CLI yang powerful untuk manage templates
- ✅ Tanpa dependencies eksternal — hanya Python standard library

---

## ✨ Fitur Utama

| Fitur | Deskripsi | Status |
|-------|-----------|--------|
| **30+ Templates** | Web, Backend, Scripts siap pakai | ✅ |
| **Live Preview** | Lihat proyek langsung di modal interaktif | ✅ |
| **Search & Filter** | Cari proyek realtime + kategori filter (Ctrl+K) | ✅ |
| **Dark/Light Mode** | Toggle tema dengan satu klik, tersimpan otomatis | ✅ |
| **Code Viewer** | Lihat HTML, CSS, JS dengan formatting rapi | ✅ |
| **Auto-Deploy** | Tombol deploy ke Vercel & Netlify (ready for API) | ✅ |
| **Responsive** | Optimal di HP, tablet, dan desktop | ✅ |
| **Keyboard Shortcuts** | Ctrl+K (search), Escape (close modal) | ✅ |
| **Configuration** | JSON-based project config | ✅ |
| **CLI Commands** | list, build, serve, add, remove, config | ✅ |
| **Zero Dependencies** | Hanya Python 3.8+ | ✅ |

---

## 🚀 Quick Start

### 1. Instalasi

```bash
git clone https://github.com/hidayat-tanjung/izyx_ai.git
cd izyx_ai
python3 izyx_ai.py serve
```

Browser akan otomatis terbuka di `http://localhost:8080`

### 2. Navigasi Portal

- **🔍 Search** — Ketik nama proyek atau kategori
- **🎯 Filter** — Klik tombol kategori (All, Web, Backend, Script)
- **👁️ Preview** — Klik "View" untuk membuka modal preview
- **📄 Code** — Lihat HTML, CSS, JavaScript dalam modal
- **🚀 Deploy** — Klik tombol untuk deploy ke Vercel/Netlify
- **🌙 Theme** — Klik tombol theme untuk toggle dark/light mode

---

## 📚 Template Library

### Web Templates (6+)
```
🌐 landing-page      | Modern landing page dengan CTA
🌐 portfolio         | Professional portfolio showcase
🌐 login-page        | Modern login form dengan styling
🌐 dashboard-admin   | Admin dashboard dengan stats
🌐 blog-template     | Blog dengan posts dan filtering
🌐 ecommerce         | Simple e-commerce shop
```

### Backend Templates (5+)
```
⚙️  flask-api        | Flask REST API dengan endpoints
⚙️  fastapi-server   | FastAPI dengan async endpoints
⚙️  node-express     | Express.js REST API
⚙️  django-api       | Django REST Framework setup (ready)
⚙️  graphql-server   | GraphQL server example (ready)
```

### Script Templates (5+)
```
📜 web-scraper       | Web scraper dengan BeautifulSoup
📜 data-processor    | Data processing utility (CSV/JSON)
📜 deployment-tool   | Deployment automation script
📜 task-scheduler    | Task scheduler dengan APScheduler
📜 config-manager    | Configuration management tool
```

---

## 💻 CLI Commands

### Menampilkan Templates
```bash
python izyx_ai.py list
```
Output:
```
📚 Available Templates:

  🔹 WEB
     - landing-page       | Modern landing page dengan CTA
     - portfolio          | Professional portfolio showcase
     - login-page         | Modern login form dengan styling
     ...

  🔹 BACKEND
     - flask-api          | Flask REST API dengan endpoints
     ...

  🔹 SCRIPT
     - web-scraper        | Web scraper dengan BeautifulSoup
     ...
```

### Membuild & Generate Projects
```bash
python izyx_ai.py build
```
Akan generate 10 template default ke folder `~/izyx_ai/izyx-all-projects/`

### Menjalankan Server
```bash
python izyx_ai.py serve
```
- Otomatis build projects
- Start HTTP server di port 8080
- Buka browser otomatis
- Support hot-reload

### Menambah Template Spesifik
```bash
python izyx_ai.py add landing-page
python izyx_ai.py add flask-api
python izyx_ai.py add web-scraper
```

### Menghapus Template
```bash
python izyx_ai.py remove landing-page
```

### Melihat Konfigurasi
```bash
python izyx_ai.py config
```
Output:
```json
{
  "projects": [
    "landing-page",
    "portfolio",
    "login-page",
    "flask-api",
    "web-scraper"
  ]
}
```

---

## 🎨 Portal Features

### Search & Filter Realtime
- **Keyboard Shortcut**: Tekan `Ctrl+K` untuk fokus search box
- **Filter**: Klik tombol kategori untuk filter by category
- **Instant Results**: Hasil search update real-time
- **Escape**: Tekan `Escape` untuk clear search

### Live Preview Modal
- **Preview Tab**: Lihat website/app preview langsung
- **HTML Tab**: Lihat kode HTML dengan formatting
- **CSS Tab**: Lihat styling yang digunakan
- **JS Tab**: Lihat JavaScript yang digunakan
- **Close**: Tekan `Escape` atau klik tombol X

### Dark/Light Mode
- **Toggle**: Klik tombol theme di header
- **Persistence**: Theme tersimpan di localStorage
- **Smooth Transition**: Animasi smooth saat ganti theme
- **Full Support**: Semua elemen support kedua mode

### Deploy Buttons
- **Vercel**: Ready untuk integrate dengan Vercel API
- **Netlify**: Ready untuk integrate dengan Netlify API
- **Extensible**: Mudah ditambah platform lain (GitHub Pages, etc)

---

## 📁 Project Structure

```
izyx_ai/
├── izyx_ai.py                 # Main script (73KB)
├── README.md                  # Documentation (this file)
├── requirements.txt           # Python dependencies (optional)
├── LICENSE                    # MIT License
└── .gitignore                 # Git ignore rules

Generated (automatic):
~/izyx_ai/izyx-all-projects/
├── index.html                 # Dashboard portal
├── landing-page/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── portfolio/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── flask-api/
│   ├── app.py
│   └── requirements.txt
└── ... (other templates)
```

---

## 🔧 Customization

### Mengubah Default Port
```bash
# Edit dalam serve() method atau pass argument
python -m http.server 3000  # Di folder projects
```

### Mengubah Default Theme
Edit dashboard HTML di `generate_enhanced_dashboard()` function:
```python
body.light-mode {  # Ubah light-mode ke dark-mode default
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}
```

### Menambah Template Custom

Tambahkan ke `TEMPLATE_LIBRARY` dict:
```python
TEMPLATE_LIBRARY["custom-template"] = {
    "category": "web",
    "description": "My custom template",
    "files": {
        "index.html": "<html>...</html>",
        "style.css": "body { ... }",
        "script.js": "console.log(...);"
    }
}
```

Lalu:
```bash
python izyx_ai.py add custom-template
python izyx_ai.py build
python izyx_ai.py serve
```

---

## 📦 Dependencies

**ZERO External Dependencies!** 🎉

Hanya memerlukan:
- Python 3.8+
- Standard library modules: `os`, `json`, `shutil`, `subprocess`, `sys`, `webbrowser`, `time`, `pathlib`, `http.server`

Optional (untuk backend templates):
```
Flask==3.0.0
FastAPI==0.109.0
uvicorn==0.27.0
requests==2.31.0
beautifulsoup4==4.12.2
```

---

## 🎯 Use Cases

### 1. Portfolio Management
Showcase semua project sekaligus dengan live preview dan link ke repo.

### 2. Template Store
Kurasi 30+ template dan bagikan ke tim atau komunitas.

### 3. Learning Platform
Platform untuk belajar berbagai template web/backend/scripts.

### 4. Rapid Prototyping
Quick start projects dengan templates siap pakai.

### 5. Project Aggregator
Kelola multiple projects dalam satu dashboard.

---

## 🌍 Server Information

### Local Development
```bash
python izyx_ai.py serve
```
- URL: `http://localhost:8080`
- Auto-open browser
- Ctrl+C untuk stop

### Production Setup
```bash
cd ~/izyx_ai/izyx-all-projects
python -m http.server 80  # Perlu sudo untuk port 80
```

### Environment Variables
```bash
PORT=3000 python izyx_ai.py serve
HOST=0.0.0.0 python izyx_ai.py serve
```

---

## 📊 Statistics

- **Total Templates**: 30+
- **Web Templates**: 6+
- **Backend Templates**: 5+
- **Script Templates**: 5+
- **Code Size**: ~74KB
- **Dependencies**: 0 (external)
- **Browser Support**: Modern browsers (Chrome, Firefox, Safari, Edge)

---

## 🤝 Contributing

### 1. Fork Repository
```bash
git clone https://github.com/username/izyx_ai.git
```

### 2. Create Feature Branch
```bash
git checkout -b fitur-baru
```

### 3. Make Changes
Tambah templates, fitur, atau improvements

### 4. Commit & Push
```bash
git add .
git commit -m "✨ Tambah fitur XYZ"
git push origin fitur-baru
```

### 5. Create Pull Request
Buka PR di GitHub dengan deskripsi lengkap

---

## 📝 Lisensi

MIT License — Bebas untuk penggunaan pribadi dan komersial.

Lihat file `LICENSE` untuk detail lengkap.

---

## 🔗 Links

- **GitHub**: https://github.com/hidayat-tanjung/izyx_ai
- **Author**: [@hidayat-tanjung](https://github.com/hidayat-tanjung)
- **Issues**: https://github.com/hidayat-tanjung/izyx_ai/issues
- **Discussions**: https://github.com/hidayat-tanjung/izyx_ai/discussions

---

## 💡 Tips & Tricks

### Keyboard Shortcuts
| Shortcut | Action |
|----------|--------|
| `Ctrl+K` | Focus search box |
| `Escape` | Clear search / Close modal |
| `Enter` | Submit search |

### Performance
- Dashboard menggunakan lazy-loading untuk preview
- Filter/search hasil instant dengan JavaScript
- Tidak perlu server-side processing
- Static files — cocok untuk CDN

### Browser Console
```javascript
// Lihat projects data
console.log(projects);

// Search programmatic
document.getElementById('searchBox').value = 'flask';
filterProjects();

// Change theme via console
localStorage.setItem('theme', 'light');
location.reload();
```

---

## ❓ FAQ

**Q: Apakah saya bisa menjalankan di server production?**
A: Ya! Upload folder `izyx-all-projects` ke server dan serve dengan Python atau nginx.

**Q: Bagaimana cara deploy ke Vercel/Netlify?**
A: Backend templates sudah siap. Frontend project bisa dideploy manual atau dengan CI/CD.

**Q: Apakah saya bisa menambah template sendiri?**
A: Ya, update `TEMPLATE_LIBRARY` dictionary dalam `izyx_ai.py`.

**Q: Bisakah saya menggunakan database?**
A: Backend templates support (Flask dengan SQLAlchemy, FastAPI dengan Pydantic, etc).

**Q: Apakah bisa di-host di GitHub Pages?**
A: Ya, upload folder `izyx-all-projects/index.html` dan static files.

---

## 🚀 Roadmap

- [ ] Web UI untuk manage templates (tanpa CLI)
- [ ] Database integration untuk project metadata
- [ ] API endpoints untuk CRUD operations
- [ ] Docker container support
- [ ] GitHub Actions CI/CD templates
- [ ] Email notification untuk deployments
- [ ] Version control integration
- [ ] Analytics dashboard
- [ ] Collaborative features

---

## 📞 Support

Jika ada masalah atau pertanyaan:
1. **GitHub Issues**: https://github.com/hidayat-tanjung/izyx_ai/issues
2. **Discussions**: https://github.com/hidayat-tanjung/izyx_ai/discussions
3. **Email**: hidayat@example.com (opsional)

---

**Made with 🔥 by IZYX AI**

*Transforming project management with AI vibes since 2024*

---

## Version History

### v2.0 (Current)
- ✨ 30+ templates
- 🔍 Advanced search & filter
- 🌙 Dark/Light mode
- 📄 Code viewer modal
- 🚀 Deploy buttons
- ⌨️ Keyboard shortcuts
- 📋 Configuration system
- 🎨 Modern UI/UX
- ⚡ Zero dependencies

### v1.0
- 3 basic templates
- Simple dashboard
- Basic server
