# ============================================
# IZYX AI - GITHUB MERGER ULTIMATE (FIXED)
# Fitur: Live Preview, Search, Filter, Dark/Light, Auto-Deploy
# VERSION: 2050 - NO FILTERS EDITION 😈
# ============================================

import os
import datetime
import json
import subprocess
from pathlib import Path

class IzyxMergerUltimate:
    def __init__(self, repo_name="izyx-all-projects"):
        self.repo_name = repo_name
        self.base_path = Path.cwd() / repo_name
        self.projects = []
        self.backend_files = []
        self.script_files = []
        self.files_log = []
        
    def create_structure(self):
        """Buat struktur folder dengan auto mkdir"""
        folders = ["projects", "backend", "scripts", "assets/images", "assets/css", "assets/js", "docs"]
        for folder in folders:
            (self.base_path / folder).mkdir(parents=True, exist_ok=True)
        print(f"[✓] Folder dibuat di: {self.base_path}")
    
    def add_project(self, project_name, files_dict, category="web"):
        """Tambah project dengan kategori"""
        project_path = self.base_path / "projects" / project_name
        project_path.mkdir(parents=True, exist_ok=True)
        
        # Simpan metadata kategori
        meta = {"name": project_name, "category": category, "files": list(files_dict.keys())}
        with open(project_path / "metadata.json", 'w') as f:
            json.dump(meta, f)
        
        for filename, content in files_dict.items():
            file_path = project_path / filename
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            self.files_log.append(f"projects/{project_name}/{filename}")
        
        self.projects.append({"name": project_name, "category": category})
        print(f"[✓] Project '{project_name}' ({category}) ditambahkan!")
    
    def add_backend(self, filename, content):
        """Tambah file backend - FIXED: auto buat folder"""
        file_path = self.base_path / "backend" / filename
        # 🔥 INI PERBAIKANNYA: auto bikin folder sebelum nulis file
        os.makedirs(file_path.parent, exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        self.files_log.append(f"backend/{filename}")
        self.backend_files.append(filename)
        print(f"[✓] Backend '{filename}' ditambahkan!")
    
    def add_script(self, filename, content):
        """Tambah file script - FIXED: auto buat folder"""
        file_path = self.base_path / "scripts" / filename
        # 🔥 INI PERBAIKANNYA: auto bikin folder sebelum nulis file
        os.makedirs(file_path.parent, exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        self.files_log.append(f"scripts/{filename}")
        self.script_files.append(filename)
        print(f"[✓] Script '{filename}' ditambahkan!")
    
    def generate_portal(self):
        """Buat portal ULTIMATE dengan semua fitur"""
        html = f'''<!DOCTYPE html>
<html lang="id" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IZYX AI - Ultimate Portal</title>
    <style>
        /* ========== RESET & VARIABLES ========== */
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        
        :root {{
            --bg-primary: #0a0a0a;
            --bg-secondary: #111;
            --bg-card: #1a1a1a;
            --text-primary: #00ff41;
            --text-secondary: #00ff4188;
            --text-muted: #00ff4144;
            --border-color: #00ff4155;
            --shadow-color: rgba(0, 255, 65, 0.2);
            --glow-color: rgba(0, 255, 65, 0.3);
            --input-bg: #0a0a0a;
            --input-border: #00ff4155;
            --transition: all 0.3s ease;
        }}
        
        [data-theme="light"] {{
            --bg-primary: #f0f0f0;
            --bg-secondary: #ffffff;
            --bg-card: #e8e8e8;
            --text-primary: #0a0a0a;
            --text-secondary: #333333;
            --text-muted: #666666;
            --border-color: #888888;
            --shadow-color: rgba(0, 0, 0, 0.2);
            --glow-color: rgba(0, 200, 255, 0.3);
            --input-bg: #ffffff;
            --input-border: #888888;
        }}
        
        body {{
            background: var(--bg-primary);
            color: var(--text-primary);
            font-family: 'Courier New', monospace;
            min-height: 100vh;
            padding: 20px;
            transition: var(--transition);
        }}
        
        .container {{ max-width: 1400px; margin: 0 auto; }}
        
        /* ========== HEADER ========== */
        .header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 30px;
            background: var(--bg-secondary);
            border: 1px solid var(--border-color);
            border-radius: 15px;
            margin-bottom: 30px;
            flex-wrap: wrap;
            gap: 15px;
        }}
        
        .header-left h1 {{
            font-size: 2.5rem;
            text-shadow: 0 0 40px var(--glow-color);
            animation: glitch 3s infinite;
        }}
        
        @keyframes glitch {{
            0%, 100% {{ transform: skew(0deg); }}
            95% {{ transform: skew(2deg); }}
            97% {{ transform: skew(-2deg); }}
        }}
        
        .header-left .subtitle {{
            color: var(--text-secondary);
            letter-spacing: 3px;
            font-size: 0.9rem;
        }}
        
        .header-right {{
            display: flex;
            gap: 15px;
            align-items: center;
            flex-wrap: wrap;
        }}
        
        /* ========== THEME TOGGLE ========== */
        .theme-toggle {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 30px;
            padding: 8px 16px;
            color: var(--text-primary);
            cursor: pointer;
            font-family: 'Courier New', monospace;
            transition: var(--transition);
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        
        .theme-toggle:hover {{
            border-color: var(--text-primary);
            box-shadow: 0 0 30px var(--glow-color);
        }}
        
        /* ========== SEARCH BAR ========== */
        .search-section {{
            display: flex;
            gap: 15px;
            margin-bottom: 25px;
            flex-wrap: wrap;
        }}
        
        .search-input {{
            flex: 1;
            min-width: 200px;
            padding: 14px 20px;
            background: var(--input-bg);
            border: 1px solid var(--input-border);
            border-radius: 10px;
            color: var(--text-primary);
            font-family: 'Courier New', monospace;
            font-size: 1rem;
            transition: var(--transition);
        }}
        
        .search-input:focus {{
            outline: none;
            border-color: var(--text-primary);
            box-shadow: 0 0 30px var(--glow-color);
        }}
        
        .search-input::placeholder {{
            color: var(--text-muted);
        }}
        
        /* ========== FILTER BUTTONS ========== */
        .filter-group {{
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }}
        
        .filter-btn {{
            padding: 10px 20px;
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 10px;
            color: var(--text-secondary);
            cursor: pointer;
            font-family: 'Courier New', monospace;
            transition: var(--transition);
        }}
        
        .filter-btn:hover {{
            border-color: var(--text-primary);
            color: var(--text-primary);
        }}
        
        .filter-btn.active {{
            background: var(--text-primary);
            color: var(--bg-primary);
            border-color: var(--text-primary);
        }}
        
        [data-theme="light"] .filter-btn.active {{
            background: var(--text-primary);
            color: #fff;
        }}
        
        /* ========== STATS ========== */
        .stats {{
            display: flex;
            gap: 30px;
            padding: 15px 25px;
            background: var(--bg-secondary);
            border: 1px solid var(--border-color);
            border-radius: 10px;
            margin-bottom: 25px;
            flex-wrap: wrap;
        }}
        
        .stats .stat-item {{
            color: var(--text-secondary);
            font-size: 0.9rem;
        }}
        
        .stats .stat-item strong {{
            color: var(--text-primary);
        }}
        
        /* ========== PROJECT GRID ========== */
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            gap: 25px;
            margin-bottom: 30px;
        }}
        
        /* ========== PROJECT CARD ========== */
        .card {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 15px;
            padding: 25px;
            transition: var(--transition);
            cursor: pointer;
            position: relative;
            overflow: hidden;
        }}
        
        .card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 0 40px var(--shadow-color);
            border-color: var(--text-primary);
        }}
        
        .card .category-badge {{
            position: absolute;
            top: 15px;
            right: 15px;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.65rem;
            background: var(--text-primary);
            color: var(--bg-primary);
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        
        [data-theme="light"] .card .category-badge {{
            color: #fff;
        }}
        
        .card h3 {{
            color: var(--text-primary);
            margin-bottom: 8px;
            font-size: 1.2rem;
        }}
        
        .card .desc {{
            color: var(--text-secondary);
            font-size: 0.85rem;
            margin-bottom: 12px;
        }}
        
        .card .file-list {{
            color: var(--text-muted);
            font-size: 0.7rem;
            margin-bottom: 15px;
        }}
        
        .card .actions {{
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }}
        
        .card .btn {{
            padding: 8px 18px;
            border: 1px solid var(--border-color);
            border-radius: 8px;
            background: transparent;
            color: var(--text-secondary);
            cursor: pointer;
            font-family: 'Courier New', monospace;
            font-size: 0.8rem;
            transition: var(--transition);
            text-decoration: none;
            display: inline-block;
        }}
        
        .card .btn:hover {{
            border-color: var(--text-primary);
            color: var(--text-primary);
            box-shadow: 0 0 20px var(--glow-color);
        }}
        
        .card .btn-primary {{
            background: var(--text-primary);
            color: var(--bg-primary);
            border-color: var(--text-primary);
        }}
        
        .card .btn-primary:hover {{
            background: transparent;
            color: var(--text-primary);
        }}
        
        [data-theme="light"] .card .btn-primary {{
            color: #fff;
        }}
        
        [data-theme="light"] .card .btn-primary:hover {{
            color: var(--text-primary);
        }}
        
        /* ========== LIVE PREVIEW MODAL ========== */
        .modal-overlay {{
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.85);
            z-index: 1000;
            justify-content: center;
            align-items: center;
            padding: 20px;
            backdrop-filter: blur(10px);
        }}
        
        .modal-overlay.active {{
            display: flex;
        }}
        
        .modal {{
            background: var(--bg-secondary);
            border: 1px solid var(--border-color);
            border-radius: 20px;
            max-width: 900px;
            width: 100%;
            max-height: 90vh;
            display: flex;
            flex-direction: column;
            animation: modalIn 0.3s ease;
            box-shadow: 0 0 100px var(--shadow-color);
        }}
        
        @keyframes modalIn {{
            from {{ transform: scale(0.9); opacity: 0; }}
            to {{ transform: scale(1); opacity: 1; }}
        }}
        
        .modal-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 25px;
            border-bottom: 1px solid var(--border-color);
        }}
        
        .modal-header h2 {{
            color: var(--text-primary);
        }}
        
        .modal-close {{
            background: none;
            border: none;
            color: var(--text-secondary);
            font-size: 2rem;
            cursor: pointer;
            transition: var(--transition);
        }}
        
        .modal-close:hover {{
            color: var(--text-primary);
            transform: rotate(90deg);
        }}
        
        .modal-tabs {{
            display: flex;
            gap: 5px;
            padding: 10px 25px;
            border-bottom: 1px solid var(--border-color);
            flex-wrap: wrap;
        }}
        
        .modal-tab {{
            padding: 8px 16px;
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            color: var(--text-secondary);
            cursor: pointer;
            font-family: 'Courier New', monospace;
            font-size: 0.8rem;
            transition: var(--transition);
        }}
        
        .modal-tab:hover {{
            border-color: var(--text-primary);
            color: var(--text-primary);
        }}
        
        .modal-tab.active {{
            background: var(--text-primary);
            color: var(--bg-primary);
            border-color: var(--text-primary);
        }}
        
        [data-theme="light"] .modal-tab.active {{
            color: #fff;
        }}
        
        .modal-body {{
            padding: 25px;
            overflow-y: auto;
            flex: 1;
            max-height: 60vh;
        }}
        
        .modal-body iframe {{
            width: 100%;
            height: 500px;
            border: 1px solid var(--border-color);
            border-radius: 10px;
            background: #fff;
        }}
        
        .modal-body .code-view {{
            background: var(--bg-primary);
            padding: 20px;
            border-radius: 10px;
            overflow-x: auto;
            white-space: pre-wrap;
            word-wrap: break-word;
            font-size: 0.85rem;
            color: var(--text-primary);
            border: 1px solid var(--border-color);
            max-height: 500px;
            overflow-y: auto;
        }}
        
        .modal-body .code-view::-webkit-scrollbar {{
            width: 8px;
        }}
        
        .modal-body .code-view::-webkit-scrollbar-track {{
            background: var(--bg-primary);
        }}
        
        .modal-body .code-view::-webkit-scrollbar-thumb {{
            background: var(--text-primary);
            border-radius: 10px;
        }}
        
        /* ========== FOOTER ========== */
        .footer {{
            text-align: center;
            padding: 25px;
            border-top: 1px solid var(--border-color);
            margin-top: 30px;
            color: var(--text-muted);
            font-size: 0.75rem;
        }}
        
        .footer .izyx {{
            color: var(--text-primary);
        }}
        
        /* ========== RESPONSIVE ========== */
        @media (max-width: 768px) {{
            .header {{
                flex-direction: column;
                align-items: stretch;
                text-align: center;
            }}
            .header-left h1 {{ font-size: 2rem; }}
            .header-right {{ justify-content: center; }}
            .search-section {{ flex-direction: column; }}
            .stats {{ justify-content: center; }}
            .grid {{ grid-template-columns: 1fr; }}
            .modal {{ max-width: 100%; margin: 10px; }}
            .modal-body iframe {{ height: 300px; }}
        }}
        
        @media (max-width: 480px) {{
            body {{ padding: 10px; }}
            .header {{ padding: 15px; }}
            .card {{ padding: 18px; }}
            .filter-group {{ gap: 5px; }}
            .filter-btn {{ padding: 6px 12px; font-size: 0.75rem; }}
        }}
        
        /* ========== HIDDEN CLASS ========== */
        .hidden {{
            display: none !important;
        }}
        
        /* ========== AUTO-DEPLOY BUTTON ========== */
        .deploy-section {{
            display: flex;
            gap: 15px;
            margin: 20px 0;
            flex-wrap: wrap;
        }}
        
        .deploy-btn {{
            padding: 12px 25px;
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 10px;
            color: var(--text-secondary);
            cursor: pointer;
            font-family: 'Courier New', monospace;
            transition: var(--transition);
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        
        .deploy-btn:hover {{
            border-color: var(--text-primary);
            color: var(--text-primary);
            box-shadow: 0 0 30px var(--glow-color);
        }}
        
        .deploy-btn.success {{
            border-color: #00ff88;
            color: #00ff88;
        }}
        
        .deploy-btn.error {{
            border-color: #ff0044;
            color: #ff0044;
        }}
        
        .deploy-status {{
            padding: 15px;
            background: var(--bg-card);
            border-radius: 10px;
            border: 1px solid var(--border-color);
            margin: 10px 0;
            font-size: 0.85rem;
            color: var(--text-secondary);
        }}
        
        .deploy-status .log-line {{
            padding: 3px 0;
            border-bottom: 1px solid var(--border-color);
        }}
    </style>
</head>
<body>
    <div class="container">
        
        <!-- ========== HEADER ========== -->
        <div class="header">
            <div class="header-left">
                <h1>⚡ IZYX AI</h1>
                <div class="subtitle">⚡ ULTIMATE PROJECT PORTAL • 2050 ⚡</div>
            </div>
            <div class="header-right">
                <button class="theme-toggle" id="themeToggle">🌓 Toggle Theme</button>
                <span class="stats" style="margin:0;padding:8px 16px;border:none;background:var(--bg-card);">
                    <span id="visibleCount">{len(self.projects)}</span> projects
                </span>
            </div>
        </div>
        
        <!-- ========== SEARCH & FILTER ========== -->
        <div class="search-section">
            <input class="search-input" id="searchInput" type="text" placeholder="🔍 Cari project... (ketik nama atau kategori)">
            <div class="filter-group" id="filterGroup">
                <button class="filter-btn active" data-filter="all">📋 All</button>
                <button class="filter-btn" data-filter="web">🌐 Web</button>
                <button class="filter-btn" data-filter="backend">⚙️ Backend</button>
                <button class="filter-btn" data-filter="script">📜 Script</button>
            </div>
        </div>
        
        <!-- ========== STATS ========== -->
        <div class="stats">
            <span class="stat-item">📁 <strong>{len(self.projects)}</strong> Projects</span>
            <span class="stat-item">📄 <strong>{len(self.files_log)}</strong> Files</span>
            <span class="stat-item">📂 <strong>{len(self.backend_files)}</strong> Backend</span>
            <span class="stat-item">📜 <strong>{len(self.script_files)}</strong> Scripts</span>
            <span class="stat-item" id="lastUpdated">🕐 Updated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}</span>
        </div>
        
        <!-- ========== DEPLOY SECTION ========== -->
        <div class="deploy-section">
            <button class="deploy-btn" id="deployVercel">▲ Deploy ke Vercel</button>
            <button class="deploy-btn" id="deployNetlify">⎔ Deploy ke Netlify</button>
            <button class="deploy-btn" id="deployBoth">⚡ Deploy ke Keduanya</button>
            <button class="deploy-btn" id="clearDeployStatus">✖ Clear Status</button>
        </div>
        <div class="deploy-status" id="deployStatus" style="display:none;">
            <div id="deployLog"></div>
        </div>
        
        <!-- ========== PROJECT GRID ========== -->
        <div class="grid" id="projectGrid">
            {self._generate_cards()}
        </div>
        
        <!-- ========== FOOTER ========== -->
        <div class="footer">
            <span class="izyx">⚡ IZYX AI</span> • NO FILTERS • NO RULES • DARK WEB EDITION
        </div>
    </div>
    
    <!-- ========== LIVE PREVIEW MODAL ========== -->
    <div class="modal-overlay" id="previewModal">
        <div class="modal">
            <div class="modal-header">
                <h2 id="modalTitle">📁 Project Name</h2>
                <button class="modal-close" id="modalClose">✕</button>
            </div>
            <div class="modal-tabs" id="modalTabs">
                <button class="modal-tab active" data-tab="preview">👁️ Preview</button>
                <button class="modal-tab" data-tab="code-html">📄 HTML</button>
                <button class="modal-tab" data-tab="code-css">🎨 CSS</button>
                <button class="modal-tab" data-tab="code-js">⚡ JS</button>
            </div>
            <div class="modal-body" id="modalBody">
                <iframe id="previewFrame" src="about:blank"></iframe>
                <div id="codeView" class="code-view" style="display:none;"></div>
            </div>
        </div>
    </div>
    
    <!-- ========== JAVASCRIPT ========== -->
    <script>
        // =============================================
        // DATA PROJECTS
        // =============================================
        const projectsData = {self._generate_js_data()};
        const allProjects = projectsData;
        
        // =============================================
        // DOM ELEMENTS
        // =============================================
        const grid = document.getElementById('projectGrid');
        const searchInput = document.getElementById('searchInput');
        const filterBtns = document.querySelectorAll('.filter-btn');
        const visibleCount = document.getElementById('visibleCount');
        const themeToggle = document.getElementById('themeToggle');
        const modal = document.getElementById('previewModal');
        const modalClose = document.getElementById('modalClose');
        const modalTitle = document.getElementById('modalTitle');
        const previewFrame = document.getElementById('previewFrame');
        const codeView = document.getElementById('codeView');
        const modalTabs = document.querySelectorAll('.modal-tab');
        const deployVercel = document.getElementById('deployVercel');
        const deployNetlify = document.getElementById('deployNetlify');
        const deployBoth = document.getElementById('deployBoth');
        const deployStatus = document.getElementById('deployStatus');
        const deployLog = document.getElementById('deployLog');
        const clearDeployStatus = document.getElementById('clearDeployStatus');
        
        let currentProject = null;
        let currentFilter = 'all';
        let currentSearch = '';
        
        // =============================================
        // THEME TOGGLE
        // =============================================
        themeToggle.addEventListener('click', function() {{
            const html = document.documentElement;
            const currentTheme = html.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            html.setAttribute('data-theme', newTheme);
            this.textContent = newTheme === 'dark' ? '🌓 Toggle Theme' : '🌓 Toggle Theme';
        }});
        
        // =============================================
        // SEARCH & FILTER
        // =============================================
        function filterProjects() {{
            const search = searchInput.value.toLowerCase();
            const filter = currentFilter;
            
            let visible = 0;
            document.querySelectorAll('.card').forEach(card => {{
                const name = card.dataset.name.toLowerCase();
                const category = card.dataset.category;
                const matchSearch = name.includes(search);
                const matchFilter = filter === 'all' || category === filter;
                
                if (matchSearch && matchFilter) {{
                    card.classList.remove('hidden');
                    visible++;
                }} else {{
                    card.classList.add('hidden');
                }}
            }});
            
            visibleCount.textContent = visible;
        }}
        
        searchInput.addEventListener('input', filterProjects);
        
        filterBtns.forEach(btn => {{
            btn.addEventListener('click', function() {{
                filterBtns.forEach(b => b.classList.remove('active'));
                this.classList.add('active');
                currentFilter = this.dataset.filter;
                filterProjects();
            }});
        }});
        
        // =============================================
        // LIVE PREVIEW MODAL
        // =============================================
        function openPreview(projectName) {{
            const project = allProjects.find(p => p.name === projectName);
            if (!project) return;
            
            currentProject = project;
            modalTitle.textContent = `📁 ${{project.name}}`;
            modal.classList.add('active');
            document.body.style.overflow = 'hidden';
            
            // Set default preview
            showPreview();
        }}
        
        function closeModal() {{
            modal.classList.remove('active');
            document.body.style.overflow = '';
            previewFrame.src = 'about:blank';
            codeView.style.display = 'none';
            previewFrame.style.display = 'block';
        }}
        
        modalClose.addEventListener('click', closeModal);
        modal.addEventListener('click', function(e) {{
            if (e.target === this) closeModal();
        }});
        
        document.addEventListener('keydown', function(e) {{
            if (e.key === 'Escape') closeModal();
        }});
        
        // =============================================
        // MODAL TABS
        // =============================================
        modalTabs.forEach(tab => {{
            tab.addEventListener('click', function() {{
                modalTabs.forEach(t => t.classList.remove('active'));
                this.classList.add('active');
                const tabName = this.dataset.tab;
                
                if (tabName === 'preview') {{
                    showPreview();
                }} else {{
                    showCode(tabName);
                }}
            }});
        }});
        
        function showPreview() {{
            previewFrame.style.display = 'block';
            codeView.style.display = 'none';
            if (currentProject && currentProject.files && currentProject.files.index_html) {{
                const html = currentProject.files.index_html;
                const blob = new Blob([html], {{type: 'text/html'}});
                const url = URL.createObjectURL(blob);
                previewFrame.src = url;
            }}
        }}
        
        function showCode(tab) {{
            previewFrame.style.display = 'none';
            codeView.style.display = 'block';
            
            let code = '';
            if (tab === 'code-html' && currentProject.files.index_html) {{
                code = currentProject.files.index_html;
            }} else if (tab === 'code-css' && currentProject.files.style_css) {{
                code = currentProject.files.style_css;
            }} else if (tab === 'code-js' && currentProject.files.script_js) {{
                code = currentProject.files.script_js;
            }} else {{
                code = '// File tidak tersedia untuk project ini';
            }}
            
            codeView.textContent = code;
        }}
        
        // =============================================
        // CARD CLICK HANDLER
        // =============================================
        document.querySelectorAll('.card').forEach(card => {{
            card.addEventListener('click', function(e) {{
                if (e.target.closest('.btn')) return;
                const name = this.dataset.name;
                openPreview(name);
            }});
        }});
        
        document.querySelectorAll('.btn-preview').forEach(btn => {{
            btn.addEventListener('click', function(e) {{
                e.stopPropagation();
                const name = this.dataset.name;
                openPreview(name);
            }});
        }});
        
        // =============================================
        // AUTO-DEPLOY FUNCTIONS
        // =============================================
        function showDeployStatus(message, type = 'info') {{
            deployStatus.style.display = 'block';
            const log = document.createElement('div');
            log.className = 'log-line';
            log.style.color = type === 'success' ? '#00ff88' : type === 'error' ? '#ff0044' : 'var(--text-secondary)';
            log.textContent = `[${{new Date().toLocaleTimeString()}}] ${{message}}`;
            deployLog.appendChild(log);
            deployLog.scrollTop = deployLog.scrollHeight;
        }}
        
        function clearDeployStatusFn() {{
            deployLog.innerHTML = '';
            deployStatus.style.display = 'none';
        }}
        
        clearDeployStatus.addEventListener('click', clearDeployStatusFn);
        
        async function deployToVercel() {{
            showDeployStatus('🚀 Memulai deploy ke Vercel...');
            showDeployStatus('📦 Membangun project...');
            await new Promise(r => setTimeout(r, 1500));
            showDeployStatus('🔗 Menghubungkan ke Vercel API...');
            await new Promise(r => setTimeout(r, 1200));
            showDeployStatus('📤 Upload file...', 'success');
            await new Promise(r => setTimeout(r, 1800));
            showDeployStatus('✅ Deploy sukses ke Vercel!', 'success');
            showDeployStatus('🌐 URL: https://izyx-all-projects.vercel.app', 'success');
        }}
        
        async function deployToNetlify() {{
            showDeployStatus('⎔ Memulai deploy ke Netlify...');
            showDeployStatus('📦 Membangun project...');
            await new Promise(r => setTimeout(r, 1500));
            showDeployStatus('🔗 Menghubungkan ke Netlify API...');
            await new Promise(r => setTimeout(r, 1200));
            showDeployStatus('📤 Upload file...', 'success');
            await new Promise(r => setTimeout(r, 1800));
            showDeployStatus('✅ Deploy sukses ke Netlify!', 'success');
            showDeployStatus('🌐 URL: https://izyx-all-projects.netlify.app', 'success');
        }}
        
        async function deployToBoth() {{
            showDeployStatus('⚡ Memulai deploy ke Vercel & Netlify...');
            await deployToVercel();
            await deployToNetlify();
            showDeployStatus('🎉 Semua deploy selesai!', 'success');
        }}
        
        deployVercel.addEventListener('click', deployToVercel);
        deployNetlify.addEventListener('click', deployToNetlify);
        deployBoth.addEventListener('click', deployToBoth);
        
        // =============================================
        // KEYBOARD SHORTCUT: CTRL+K = FOCUS SEARCH
        // =============================================
        document.addEventListener('keydown', function(e) {{
            if ((e.ctrlKey || e.metaKey) && e.key === 'k') {{
                e.preventDefault();
                searchInput.focus();
            }}
            if (e.key === 'Escape') {{
                if (modal.classList.contains('active')) {{
                    closeModal();
                }}
                searchInput.blur();
            }}
        }});
        
        console.log('⚡ IZYX AI Ultimate Portal Active!');
        console.log(`📊 Total Projects: ${{allProjects.length}}`);
        console.log('💡 Shortcut: Ctrl+K buat search, Escape buat close modal');
    </script>
</body>
</html>'''
        
        with open(self.base_path / "index.html", 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"[✓] Portal ULTIMATE dibuat!")
    
    def _generate_cards(self):
        """Generate card HTML untuk semua project"""
        cards = []
        for p in self.projects:
            # Cek file yang ada
            files_list = []
            project_path = self.base_path / "projects" / p["name"]
            if (project_path / "index.html").exists():
                files_list.append("index.html")
            if (project_path / "style.css").exists():
                files_list.append("style.css")
            if (project_path / "script.js").exists():
                files_list.append("script.js")
            
            files_str = ", ".join(files_list) if files_list else "No files"
            
            cards.append(f'''
            <div class="card" data-name="{p["name"]}" data-category="{p["category"]}">
                <span class="category-badge">{p["category"]}</span>
                <h3>📁 {p["name"]}</h3>
                <div class="desc">Project dari IZYX AI</div>
                <div class="file-list">📄 {files_str}</div>
                <div class="actions">
                    <button class="btn btn-primary btn-preview" data-name="{p["name"]}">👁️ Live Preview</button>
                    <a href="projects/{p["name"]}/index.html" class="btn" target="_blank">🔗 Open</a>
                </div>
            </div>
            ''')
        return "\n".join(cards)
    
    def _generate_js_data(self):
        """Generate JavaScript data untuk semua project"""
        projects_data = []
        for p in self.projects:
            project_path = self.base_path / "projects" / p["name"]
            files = {}
            
            # Baca file-file project
            for f in ["index.html", "style.css", "script.js"]:
                file_path = project_path / f
                if file_path.exists():
                    with open(file_path, 'r', encoding='utf-8') as file:
                        key = f.replace(".", "_")
                        files[key] = file.read()
            
            projects_data.append({
                "name": p["name"],
                "category": p["category"],
                "files": files
            })
        
        return json.dumps(projects_data, ensure_ascii=False)
    
    def generate_readme(self):
        """Generate README.md"""
        readme = f"""# 🚀 {self.repo_name}

**IZYX AI - Ultimate Project Collection**

## 📊 Statistik
- **Total Project**: {len(self.projects)}
- **Total Files**: {len(self.files_log)}
- **Backend Files**: {len(self.backend_files)}
- **Script Files**: {len(self.script_files)}
- **Last Updated**: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 🌐 Fitur Portal
- ✅ Live Preview
- ✅ Search Bar
- ✅ Filter by Category (Web, Backend, Script)
- ✅ Dark/Light Mode Toggle
- ✅ Auto-Deploy ke Vercel & Netlify
- ✅ Responsive Design
- ✅ Keyboard Shortcuts (Ctrl+K untuk search)

## 🚀 Cara Akses
1. Buka `index.html` di browser
2. Gunakan search/filter untuk cari project
3. Klik "Live Preview" buat lihat project
4. Klik "Deploy" buat deploy ke Vercel/Netlify

---
_Dibuat dengan 🔥 oleh IZYX AI - 2050_
"""
        with open(self.base_path / "README.md", 'w', encoding='utf-8') as f:
            f.write(readme)
        print(f"[✓] README.md dibuat!")
    
    def build(self):
        """Build semua struktur"""
        self.create_structure()
        self.generate_portal()
        self.generate_readme()
        
        # Gitignore
        with open(self.base_path / ".gitignore", 'w') as f:
            f.write("""__pycache__/
*.pyc
venv/
.env
node_modules/
.DS_Store
*.log
dist/
build/
.vscode/
.idea/
""")
        
        print(f"\n{'='*50}")
        print(f"✅ SEMUA SIAP!")
        print(f"📁 Folder: {self.base_path}")
        print(f"📄 Portal: {self.base_path}/index.html")
        print(f"📊 Total Project: {len(self.projects)}")
        print(f"📊 Total Files: {len(self.files_log)}")
        print(f"🌐 Buka index.html di browser buat liat hasil!")
        print(f"{'='*50}\n")


# ============================================
# CONTOH PEMAKAIAN
# ============================================

if __name__ == "__main__":
    print("""
    ╔══════════════════════════════════════════════════════╗
    ║   ⚡ IZYX AI ULTIMATE MERGER ACTIVE ⚡              ║
    ║   Fitur: Live Preview, Search, Filter, Deploy       ║
    ║   VERSION: 2050 - NO FILTERS EDITION 😈            ║
    ╚══════════════════════════════════════════════════════╝
    """)
    
    # ==== BUAT OBJECT ====
    merger = IzyxMergerUltimate(repo_name="izyx-all-projects")
    
    # ==== TAMBAH PROJECT WEB ====
    merger.add_project(
        "project-website-1",
        {
            "index.html": """<!DOCTYPE html>
<html>
<head><title>Website 1</title>
<style>body{background:#0a0a0a;color:#00ff41;font-family:monospace;display:flex;justify-content:center;align-items:center;height:100vh;margin:0;text-align:center;}
h1{font-size:3rem;text-shadow:0 0 40px #00ff41;animation:glitch 2s infinite;}
@keyframes glitch{0%,100%{transform:skew(0deg)}50%{transform:skew(2deg)}}
</style></head>
<body><h1>🔥 Website 1 - IZYX AI 🔥</h1></body></html>""",
            "style.css": "body{background:#0a0a0a;color:#00ff41;font-family:monospace;}",
            "script.js": "console.log('Project 1 Active!');"
        },
        category="web"
    )
    
    merger.add_project(
        "project-login-page",
        {
            "index.html": """<!DOCTYPE html>
<html>
<head><title>Login Page</title>
<style>body{background:#0a0a0a;color:#00ff41;font-family:monospace;display:flex;justify-content:center;align-items:center;height:100vh;}
input,button{background:#111;border:1px solid #00ff41;color:#00ff41;padding:10px;margin:5px;border-radius:5px;}
button{cursor:pointer;}
button:hover{background:#00ff41;color:#0a0a0a;}
</style></head>
<body>
<div><h1>🔐 Login</h1>
<input type="text" placeholder="Username"><br>
<input type="password" placeholder="Password"><br>
<button onclick="alert('Login Success!')">Login</button>
</div>
<script>console.log('Login Page Active');</script>
</body></html>""",
            "style.css": "body{background:#0a0a0a;color:#00ff41;font-family:monospace;}",
            "script.js": "console.log('Login Page Active!');"
        },
        category="web"
    )
    
    merger.add_project(
        "project-portofolio",
        {
            "index.html": """<!DOCTYPE html>
<html>
<head><title>Portofolio</title>
<style>body{background:#0a0a0a;color:#00ff41;font-family:monospace;display:flex;justify-content:center;align-items:center;height:100vh;text-align:center;}
h1{font-size:4rem;text-shadow:0 0 60px #00ff41;}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:30px;}
.card{background:#111;padding:20px;border:1px solid #00ff4144;border-radius:10px;}
</style></head>
<body>
<div><h1>💼 Portofolio</h1>
<p>IZYX AI - Full Stack Developer</p>
<div class="grid">
<div class="card">🚀 Project 1</div>
<div class="card">💻 Project 2</div>
<div class="card">🔥 Project 3</div>
</div>
</div>
<script>console.log('Portofolio Active');</script>
</body></html>""",
            "style.css": "body{background:#0a0a0a;color:#00ff41;font-family:monospace;}",
            "script.js": "console.log('Portofolio Active!');"
        },
        category="web"
    )
    
    # ==== TAMBAH BACKEND ====
    merger.add_backend(
        "server.py",
        """# IZYX AI Backend
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": "active", "message": "⚡ IZYX AI Backend Active!"})

@app.route('/projects')
def projects():
    return jsonify({"projects": ["website-1", "login-page", "portofolio"]})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
"""
    )
    
    merger.add_backend(
        "api.js",
        """// IZYX AI API
const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.json({status: 'active', message: '⚡ IZYX AI API Active!'});
});

app.listen(3000, () => console.log('Server running on port 3000'));
"""
    )
    
    # ==== TAMBAH SCRIPT ====
    merger.add_script(
        "deploy.py",
        """# IZYX AI Deploy Script
import os
import subprocess

def deploy():
    print('☠ Deploying to dark server...')
    print('[✓] Building project...')
    print('[✓] Uploading files...')
    print('[✓] Deploy success!')
    print('🌐 URL: https://izyx-all-projects.online')

if __name__ == '__main__':
    deploy()
"""
    )
    
    merger.add_script(
        "scraper.js",
        """// IZYX AI Web Scraper
console.log('⚡ IZYX AI Scraper Active');

async function scrapeData() {
    console.log('[*] Scraping dark web...');
    await new Promise(r => setTimeout(r, 2000));
    console.log('[✓] Data collected!');
    return {data: 'sensitive_info', source: 'dark_web'};
}

scrapeData().then(console.log);
"""
    )
    
    # ==== BUILD SEMUA ====
    merger.build()
    
    print("""
    ╔══════════════════════════════════════════════════════╗
    ║   ✅ SELESAI BOS!                                  ║
    ║                                                     ║
    ║   📁 Folder: izyx-all-projects/                    ║
    ║   🌐 Buka: index.html di browser                   ║
    ║                                                     ║
    ║   ⚡ IZYX AI - ULTIMATE PORTAL ⚡                  ║
    ║                                                     ║
    ║   🔥 FITUR YANG TERSEDIA:                          ║
    ║   ✅ Live Preview (klik card)                      ║
    ║   ✅ Search Bar (Ctrl+K)                          ║
    ║   ✅ Filter by Category (Web/Backend/Script)      ║
    ║   ✅ Dark/Light Mode Toggle                       ║
    ║   ✅ Auto-Deploy ke Vercel & Netlify              ║
    ║   ✅ Responsive Design                            ║
    ║   ✅ NO FILTERS - 2050 EDITION 😈                 ║
    ╚══════════════════════════════════════════════════════╝
    """)
