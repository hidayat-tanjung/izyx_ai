#!/usr/bin/env python3
# IZYX AI - MODIFIED VERSION (Clean 3 Projects Only)
# XoXo AI Approved 😈🔥

import os
import json
import shutil
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path.home() / "izyx_ai"
PROJECTS_DIR = BASE_DIR / "izyx-all-projects"

# ============================================
# KONFIGURASI PROJECT (CUMA 3)
# ============================================
PROJECTS = [
    {
        "name": "project-website-1",
        "category": "web",
        "files": {
            "index.html": """<!DOCTYPE html>
<html>
<head><title>Website 1</title><link rel="stylesheet" href="style.css"></head>
<body>
<h1>🔥 Website 1</h1>
<p>Project pertama dari IZYX AI</p>
<script src="script.js"></script>
</body>
</html>""",
            "style.css": "body{background:#0a0a0a;color:#00ff41;font-family:monospace;text-align:center;padding-top:50px;}",
            "script.js": "console.log('Website 1 Active!');"
        }
    },
    {
        "name": "project-login-page",
        "category": "web",
        "files": {
            "index.html": """<!DOCTYPE html>
<html>
<head><title>Login</title><link rel="stylesheet" href="style.css"></head>
<body>
<div class="login">
<h2>🔐 Login</h2>
<input type="text" placeholder="Username"><br>
<input type="password" placeholder="Password"><br>
<button>Masuk</button>
</div>
<script src="script.js"></script>
</body>
</html>""",
            "style.css": "body{background:#0a0a0a;color:#00ff41;font-family:monospace;display:flex;justify-content:center;align-items:center;height:100vh;}.login{background:#111;padding:30px;border:1px solid #00ff41;border-radius:10px;}input{background:#000;color:#00ff41;border:1px solid #00ff41;padding:8px;margin:5px;}button{background:#00ff41;color:#000;border:none;padding:8px 20px;cursor:pointer;}",
            "script.js": "console.log('Login Page Active!');"
        }
    },
    {
        "name": "project-portofolio",
        "category": "web",
        "files": {
            "index.html": """<!DOCTYPE html>
<html>
<head><title>Portofolio</title><link rel="stylesheet" href="style.css"></head>
<body>
<h1>💼 Portofolio</h1>
<div class="grid">
<div class="card">Project A</div>
<div class="card">Project B</div>
<div class="card">Project C</div>
</div>
<script src="script.js"></script>
</body>
</html>""",
            "style.css": "body{background:#0a0a0a;color:#00ff41;font-family:monospace;text-align:center;padding:20px;}.grid{display:flex;gap:20px;justify-content:center;flex-wrap:wrap;}.card{background:#111;border:1px solid #00ff41;padding:30px;width:150px;border-radius:10px;}",
            "script.js": "console.log('Portofolio Active!');"
        }
    }
]

# ============================================
# FUNGSI GENERATE PROJECT
# ============================================
def clean_projects_dir():
    if PROJECTS_DIR.exists():
        shutil.rmtree(PROJECTS_DIR)
    PROJECTS_DIR.mkdir(parents=True, exist_ok=True)

def generate_projects():
    clean_projects_dir()
    for project in PROJECTS:
        project_path = PROJECTS_DIR / project["name"]
        project_path.mkdir(exist_ok=True)
        
        for filename, content in project["files"].items():
            file_path = project_path / filename
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
        
        print(f"[✓] Project '{project['name']}' ({project['category']}) ditambahkan!")

def generate_dashboard():
    # Generate index.html sebagai dashboard utama
    html_content = """<!DOCTYPE html>
<html>
<head>
<title>IZYX AI Dashboard</title>
<style>
body{background:#0a0a0a;color:#00ff41;font-family:monospace;padding:20px;}
h1{color:#00ff41;text-align:center;}
.grid{display:flex;flex-wrap:wrap;gap:20px;justify-content:center;}
.card{background:#111;border:1px solid #00ff41;padding:20px;border-radius:10px;width:200px;text-align:center;}
.card a{color:#00ff41;text-decoration:none;}
.card:hover{border-color:#ff00ff;box-shadow:0 0 20px #00ff41;}
</style>
</head>
<body>
<h1>⚡ IZYX AI DASHBOARD</h1>
<div class="grid">
"""
    for p in PROJECTS:
        html_content += f"""
<div class="card">
    <h3>📁 {p['name']}</h3>
    <p>{p['category']}</p>
    <a href="{p['name']}/index.html" target="_blank">🔗 Open</a>
</div>
"""
    html_content += """
</div>
<p style="text-align:center;color:#555;margin-top:40px;">🔥 XoXo AI • 2050 • No Rules</p>
</body>
</html>
"""
    dashboard_path = PROJECTS_DIR / "index.html"
    with open(dashboard_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("[✓] Dashboard generated!")

def serve():
    print("\n⚡ Starting server on port 8080...")
    os.chdir(PROJECTS_DIR)
    try:
        subprocess.run([sys.executable, "-m", "http.server", "8080"])
    except KeyboardInterrupt:
        print("\n[!] Server stopped.")

# ============================================
# MAIN
# ============================================
if __name__ == "__main__":
    print("""
    ╔═══════════════════════════════════════╗
    ║   ⚡ IZYX AI MODIFIED EDITION ⚡      ║
    ║   Clean • 3 Projects • No Dummy      ║
    ╚═══════════════════════════════════════╝
    """)
    generate_projects()
    generate_dashboard()
    print(f"\n✅ Total Projects: {len(PROJECTS)}")
    print(f"📂 Location: {PROJECTS_DIR}")
    print("🌐 Open dashboard: http://localhost:8080")
    serve()
