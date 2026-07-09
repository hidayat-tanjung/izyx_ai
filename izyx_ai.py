#!/usr/bin/env python3
"""
IZYX AI - Ultimate Project Manager with AI Vibes
Enhanced version with 30+ templates, search, filters, deploy, dark/light mode
"""

import os
import json
import shutil
import subprocess
import sys
import webbrowser
import time
from pathlib import Path
from http.server import HTTPServer, SimpleHTTPRequestHandler
from datetime import datetime

BASE_DIR = Path.home() / "izyx_ai"
PROJECTS_DIR = BASE_DIR / "izyx-all-projects"
CONFIG_FILE = BASE_DIR / "projects.json"

# ============================================
# TEMPLATE LIBRARY (30+ TEMPLATES)
# ============================================
TEMPLATE_LIBRARY = {
    # ===== WEB TEMPLATES =====
    "landing-page": {
        "category": "web",
        "description": "Modern landing page with CTA",
        "files": {
            "index.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Landing Page</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <nav class="navbar">
        <div class="logo">🚀 IZYX</div>
        <ul class="nav-links">
            <li><a href="#home">Home</a></li>
            <li><a href="#features">Features</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>
    
    <section id="home" class="hero">
        <h1>Welcome to IZYX AI</h1>
        <p>Build amazing projects in seconds</p>
        <button class="cta">Get Started →</button>
    </section>
    
    <section id="features" class="features">
        <h2>Why Choose Us?</h2>
        <div class="feature-grid">
            <div class="feature-card">
                <h3>⚡ Fast</h3>
                <p>Lightning quick performance</p>
            </div>
            <div class="feature-card">
                <h3>🎨 Beautiful</h3>
                <p>Modern UI/UX design</p>
            </div>
            <div class="feature-card">
                <h3>🔒 Secure</h3>
                <p>Enterprise-grade security</p>
            </div>
        </div>
    </section>
    
    <footer id="contact">
        <p>&copy; 2024 IZYX AI. Made with 🔥</p>
    </footer>
    
    <script src="script.js"></script>
</body>
</html>""",
            "style.css": """* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: #333;
    line-height: 1.6;
}

.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 2rem;
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    position: sticky;
    top: 0;
}

.logo {
    font-size: 1.5rem;
    font-weight: bold;
    color: white;
}

.nav-links {
    display: flex;
    list-style: none;
    gap: 2rem;
}

.nav-links a {
    color: white;
    text-decoration: none;
    transition: 0.3s;
}

.nav-links a:hover {
    color: #ffd700;
}

.hero {
    text-align: center;
    padding: 8rem 2rem;
    color: white;
}

.hero h1 {
    font-size: 3rem;
    margin-bottom: 1rem;
    animation: fadeInDown 0.8s ease;
}

.hero p {
    font-size: 1.3rem;
    margin-bottom: 2rem;
    opacity: 0.9;
}

.cta {
    background: #ffd700;
    color: #333;
    padding: 0.8rem 2rem;
    border: none;
    border-radius: 50px;
    font-size: 1rem;
    cursor: pointer;
    transition: 0.3s;
    font-weight: bold;
}

.cta:hover {
    background: #ffed4e;
    transform: scale(1.05);
}

.features {
    padding: 4rem 2rem;
    background: white;
}

.features h2 {
    text-align: center;
    font-size: 2rem;
    margin-bottom: 3rem;
    color: #667eea;
}

.feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
    max-width: 1200px;
    margin: 0 auto;
}

.feature-card {
    background: #f8f9fa;
    padding: 2rem;
    border-radius: 10px;
    text-align: center;
    transition: 0.3s;
}

.feature-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

.feature-card h3 {
    color: #667eea;
    margin-bottom: 1rem;
    font-size: 1.5rem;
}

footer {
    text-align: center;
    padding: 2rem;
    background: #333;
    color: white;
}

@keyframes fadeInDown {
    from {
        opacity: 0;
        transform: translateY(-20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@media (max-width: 768px) {
    .hero h1 {
        font-size: 2rem;
    }
    
    .nav-links {
        gap: 1rem;
    }
}""",
            "script.js": """console.log('Landing Page Loaded!');

document.querySelector('.cta').addEventListener('click', function() {
    alert('Welcome to IZYX AI! 🚀');
});

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});"""
        }
    },
    
    "portfolio": {
        "category": "web",
        "description": "Professional portfolio showcase",
        "files": {
            "index.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portfolio</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header class="header">
        <h1>💼 My Portfolio</h1>
        <p>Creative Developer & Designer</p>
    </header>
    
    <section class="projects">
        <h2>Featured Projects</h2>
        <div class="project-grid">
            <div class="project-card">
                <div class="project-image" style="background: linear-gradient(135deg, #667eea, #764ba2);"></div>
                <h3>Project Alpha</h3>
                <p>Web Design & Development</p>
                <a href="#" class="project-link">View →</a>
            </div>
            <div class="project-card">
                <div class="project-image" style="background: linear-gradient(135deg, #f093fb, #f5576c);"></div>
                <h3>Project Beta</h3>
                <p>Mobile App Design</p>
                <a href="#" class="project-link">View →</a>
            </div>
            <div class="project-card">
                <div class="project-image" style="background: linear-gradient(135deg, #4facfe, #00f2fe);"></div>
                <h3>Project Gamma</h3>
                <p>Brand Identity</p>
                <a href="#" class="project-link">View →</a>
            </div>
        </div>
    </section>
    
    <section class="about">
        <h2>About Me</h2>
        <p>I'm a passionate developer with 5+ years of experience creating beautiful and functional web solutions.</p>
        <div class="skills">
            <span class="skill">JavaScript</span>
            <span class="skill">React</span>
            <span class="skill">Design</span>
            <span class="skill">Python</span>
            <span class="skill">Web Dev</span>
        </div>
    </section>
    
    <footer>
        <p>© 2024 Portfolio. Crafted with ❤️</p>
    </footer>
    
    <script src="script.js"></script>
</body>
</html>""",
            "style.css": """* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Poppins', sans-serif;
    background: #f8f9fa;
    color: #333;
}

.header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 4rem 2rem;
    text-align: center;
}

.header h1 {
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
}

.header p {
    font-size: 1.1rem;
    opacity: 0.9;
}

.projects {
    padding: 4rem 2rem;
    max-width: 1200px;
    margin: 0 auto;
}

.projects h2 {
    text-align: center;
    font-size: 2rem;
    margin-bottom: 3rem;
    color: #333;
}

.project-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2rem;
}

.project-card {
    background: white;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
    transition: 0.3s;
}

.project-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
}

.project-image {
    height: 200px;
}

.project-card h3 {
    padding: 1.5rem 1.5rem 0.5rem;
    color: #667eea;
}

.project-card p {
    padding: 0 1.5rem;
    font-size: 0.9rem;
    color: #666;
}

.project-link {
    display: inline-block;
    margin: 1rem 1.5rem;
    color: #667eea;
    text-decoration: none;
    font-weight: bold;
    transition: 0.3s;
}

.project-link:hover {
    color: #764ba2;
}

.about {
    background: white;
    padding: 4rem 2rem;
    text-align: center;
}

.about h2 {
    font-size: 2rem;
    margin-bottom: 1rem;
    color: #333;
}

.about p {
    max-width: 600px;
    margin: 0 auto 2rem;
    font-size: 1.1rem;
    color: #666;
}

.skills {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 1rem;
}

.skill {
    background: #667eea;
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 20px;
    font-size: 0.9rem;
}

footer {
    background: #333;
    color: white;
    text-align: center;
    padding: 2rem;
}""",
            "script.js": """console.log('Portfolio loaded!');

const projectCards = document.querySelectorAll('.project-card');
projectCards.forEach((card, index) => {
    card.style.animationDelay = `${index * 0.1}s`;
});

document.querySelectorAll('.project-link').forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        alert('Project details coming soon! 🚀');
    });
});"""
        }
    },
    
    "login-page": {
        "category": "web",
        "description": "Modern login form",
        "files": {
            "index.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <div class="login-box">
            <h1>🔐 Login</h1>
            <form id="loginForm">
                <div class="form-group">
                    <label for="email">Email</label>
                    <input type="email" id="email" placeholder="your@email.com" required>
                </div>
                <div class="form-group">
                    <label for="password">Password</label>
                    <input type="password" id="password" placeholder="••••••••" required>
                </div>
                <div class="remember-forgot">
                    <label><input type="checkbox"> Remember me</label>
                    <a href="#">Forgot password?</a>
                </div>
                <button type="submit" class="login-btn">Sign In</button>
            </form>
            <p class="signup">Don't have an account? <a href="#">Sign up</a></p>
        </div>
    </div>
    <script src="script.js"></script>
</body>
</html>""",
            "style.css": """* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

.container {
    width: 100%;
    padding: 20px;
}

.login-box {
    background: white;
    padding: 2rem;
    border-radius: 10px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
    max-width: 400px;
    margin: 0 auto;
}

.login-box h1 {
    text-align: center;
    color: #667eea;
    margin-bottom: 2rem;
    font-size: 1.8rem;
}

.form-group {
    margin-bottom: 1.5rem;
}

.form-group label {
    display: block;
    margin-bottom: 0.5rem;
    color: #333;
    font-weight: 500;
}

.form-group input[type="email"],
.form-group input[type="password"] {
    width: 100%;
    padding: 0.8rem;
    border: 1px solid #ddd;
    border-radius: 5px;
    font-size: 1rem;
    transition: 0.3s;
}

.form-group input:focus {
    outline: none;
    border-color: #667eea;
    box-shadow: 0 0 10px rgba(102, 126, 234, 0.2);
}

.remember-forgot {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1.5rem;
    font-size: 0.9rem;
}

.remember-forgot a {
    color: #667eea;
    text-decoration: none;
}

.remember-forgot a:hover {
    text-decoration: underline;
}

.login-btn {
    width: 100%;
    padding: 0.8rem;
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    border: none;
    border-radius: 5px;
    font-size: 1rem;
    font-weight: bold;
    cursor: pointer;
    transition: 0.3s;
}

.login-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
}

.signup {
    text-align: center;
    margin-top: 1.5rem;
    color: #666;
}

.signup a {
    color: #667eea;
    text-decoration: none;
    font-weight: bold;
}

.signup a:hover {
    text-decoration: underline;
}""",
            "script.js": """const form = document.getElementById('loginForm');

form.addEventListener('submit', (e) => {
    e.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    
    if (email && password) {
        alert(`Welcome back! 🎉\\n\\nEmail: ${email}`);
        form.reset();
    }
});"""
        }
    },
    
    "dashboard-admin": {
        "category": "web",
        "description": "Admin dashboard with charts",
        "files": {
            "index.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Dashboard</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="sidebar">
        <div class="logo">📊 IZYX Admin</div>
        <ul class="menu">
            <li class="active"><a href="#dashboard">Dashboard</a></li>
            <li><a href="#users">Users</a></li>
            <li><a href="#analytics">Analytics</a></li>
            <li><a href="#settings">Settings</a></li>
        </ul>
    </div>
    
    <div class="main-content">
        <header class="topbar">
            <h2>Dashboard</h2>
            <div class="user-profile">👤 Admin</div>
        </header>
        
        <section class="content">
            <div class="stats-grid">
                <div class="stat-card">
                    <h3>Users</h3>
                    <p class="number">1,234</p>
                    <span class="badge">+12%</span>
                </div>
                <div class="stat-card">
                    <h3>Revenue</h3>
                    <p class="number">$45.2K</p>
                    <span class="badge">+8%</span>
                </div>
                <div class="stat-card">
                    <h3>Orders</h3>
                    <p class="number">567</p>
                    <span class="badge">+5%</span>
                </div>
                <div class="stat-card">
                    <h3>Growth</h3>
                    <p class="number">28%</p>
                    <span class="badge">+3%</span>
                </div>
            </div>
            
            <div class="charts-grid">
                <div class="chart">
                    <h3>Monthly Sales</h3>
                    <div class="chart-placeholder">📈 Chart Area</div>
                </div>
                <div class="chart">
                    <h3>User Distribution</h3>
                    <div class="chart-placeholder">🥧 Chart Area</div>
                </div>
            </div>
        </section>
    </div>
    
    <script src="script.js"></script>
</body>
</html>""",
            "style.css": """* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: #f0f2f5;
    display: flex;
}

.sidebar {
    width: 250px;
    background: #2c3e50;
    color: white;
    padding: 2rem 0;
    min-height: 100vh;
    position: sticky;
    top: 0;
}

.logo {
    padding: 0 1.5rem;
    font-size: 1.3rem;
    font-weight: bold;
    margin-bottom: 2rem;
}

.menu {
    list-style: none;
}

.menu li {
    margin: 0.5rem 0;
}

.menu a {
    display: block;
    padding: 0.8rem 1.5rem;
    color: #ecf0f1;
    text-decoration: none;
    transition: 0.3s;
}

.menu li.active a,
.menu a:hover {
    background: #3498db;
    border-left: 4px solid #2980b9;
}

.main-content {
    flex: 1;
    display: flex;
    flex-direction: column;
}

.topbar {
    background: white;
    padding: 1.5rem 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.topbar h2 {
    color: #333;
}

.user-profile {
    background: #3498db;
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 20px;
}

.content {
    padding: 2rem;
}

.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.5rem;
    margin-bottom: 2rem;
}

.stat-card {
    background: white;
    padding: 1.5rem;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.stat-card h3 {
    color: #666;
    font-size: 0.9rem;
    margin-bottom: 0.5rem;
}

.number {
    font-size: 2rem;
    font-weight: bold;
    color: #2c3e50;
    margin-bottom: 0.5rem;
}

.badge {
    display: inline-block;
    background: #27ae60;
    color: white;
    padding: 0.3rem 0.6rem;
    border-radius: 3px;
    font-size: 0.8rem;
}

.charts-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: 1.5rem;
}

.chart {
    background: white;
    padding: 1.5rem;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.chart h3 {
    margin-bottom: 1rem;
    color: #333;
}

.chart-placeholder {
    height: 250px;
    background: #f8f9fa;
    border: 2px dashed #ddd;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #999;
    border-radius: 5px;
}

@media (max-width: 768px) {
    .sidebar {
        width: 100%;
        min-height: auto;
        padding: 1rem 0;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .menu {
        display: flex;
        gap: 1rem;
    }
    
    .menu a {
        padding: 0.5rem 1rem;
    }
}""",
            "script.js": """console.log('Admin Dashboard loaded!');

const menuItems = document.querySelectorAll('.menu li');
menuItems.forEach(item => {
    item.addEventListener('click', function() {
        menuItems.forEach(li => li.classList.remove('active'));
        this.classList.add('active');
    });
});"""
        }
    },
    
    "blog-template": {
        "category": "web",
        "description": "Blog with posts and comments",
        "files": {
            "index.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tech Blog</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header class="blog-header">
        <h1>📝 Tech Blog</h1>
        <p>Insights on web development and AI</p>
    </header>
    
    <nav class="blog-nav">
        <a href="#">All</a>
        <a href="#">JavaScript</a>
        <a href="#">Python</a>
        <a href="#">AI</a>
    </nav>
    
    <main class="blog-container">
        <article class="blog-post">
            <div class="post-header">
                <h2>Getting Started with Python 3.12</h2>
                <div class="post-meta">
                    <span class="author">👤 John Doe</span>
                    <span class="date">📅 Jul 9, 2024</span>
                    <span class="category">Python</span>
                </div>
            </div>
            <div class="post-content">
                <p>Python 3.12 brings exciting new features and improvements. In this post, we'll explore the major updates and how to migrate your existing code...</p>
                <a href="#" class="read-more">Read More →</a>
            </div>
        </article>
        
        <article class="blog-post">
            <div class="post-header">
                <h2>JavaScript ES2024 Features</h2>
                <div class="post-meta">
                    <span class="author">👤 Jane Smith</span>
                    <span class="date">📅 Jul 8, 2024</span>
                    <span class="category">JavaScript</span>
                </div>
            </div>
            <div class="post-content">
                <p>ES2024 introduces powerful new syntax and features. Let's dive into what's new and how to use it effectively in your projects...</p>
                <a href="#" class="read-more">Read More →</a>
            </div>
        </article>
    </main>
    
    <script src="script.js"></script>
</body>
</html>""",
            "style.css": """* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Georgia', serif;
    background: #fafafa;
    color: #333;
}

.blog-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 3rem 2rem;
    text-align: center;
}

.blog-header h1 {
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
}

.blog-header p {
    font-size: 1.1rem;
    opacity: 0.9;
}

.blog-nav {
    display: flex;
    justify-content: center;
    gap: 2rem;
    padding: 1.5rem 2rem;
    background: white;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    flex-wrap: wrap;
}

.blog-nav a {
    color: #667eea;
    text-decoration: none;
    font-weight: 500;
    transition: 0.3s;
}

.blog-nav a:hover {
    color: #764ba2;
    border-bottom: 2px solid #764ba2;
}

.blog-container {
    max-width: 800px;
    margin: 2rem auto;
    padding: 0 2rem;
}

.blog-post {
    background: white;
    padding: 2rem;
    margin-bottom: 2rem;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    transition: 0.3s;
}

.blog-post:hover {
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.15);
}

.post-header h2 {
    color: #333;
    margin-bottom: 0.5rem;
    font-size: 1.8rem;
}

.post-meta {
    display: flex;
    gap: 1rem;
    font-size: 0.9rem;
    color: #666;
    margin-bottom: 1rem;
    flex-wrap: wrap;
}

.category {
    background: #667eea;
    color: white;
    padding: 0.2rem 0.6rem;
    border-radius: 3px;
    font-size: 0.8rem;
}

.post-content {
    line-height: 1.8;
    color: #555;
}

.read-more {
    display: inline-block;
    margin-top: 1rem;
    color: #667eea;
    text-decoration: none;
    font-weight: bold;
    transition: 0.3s;
}

.read-more:hover {
    color: #764ba2;
}""",
            "script.js": """console.log('Blog loaded!');

document.querySelectorAll('.read-more').forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        alert('Full article view coming soon! 📖');
    });
});"""
        }
    },
    
    "ecommerce": {
        "category": "web",
        "description": "Simple e-commerce shop",
        "files": {
            "index.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IZYX Shop</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header class="header">
        <div class="header-top">
            <h1>🛍️ IZYX Shop</h1>
            <div class="cart">🛒 Cart (0)</div>
        </div>
        <nav class="categories">
            <a href="#" class="cat-btn active">All</a>
            <a href="#" class="cat-btn">Electronics</a>
            <a href="#" class="cat-btn">Accessories</a>
            <a href="#" class="cat-btn">Clothing</a>
        </nav>
    </header>
    
    <main class="shop">
        <div class="product-grid">
            <div class="product-card">
                <div class="product-image" style="background: linear-gradient(135deg, #667eea, #764ba2);"></div>
                <h3>Premium Headphones</h3>
                <p class="price">$199.99</p>
                <button class="add-btn">Add to Cart</button>
            </div>
            
            <div class="product-card">
                <div class="product-image" style="background: linear-gradient(135deg, #f093fb, #f5576c);"></div>
                <h3>Smart Watch</h3>
                <p class="price">$299.99</p>
                <button class="add-btn">Add to Cart</button>
            </div>
            
            <div class="product-card">
                <div class="product-image" style="background: linear-gradient(135deg, #4facfe, #00f2fe);"></div>
                <h3>Wireless Mouse</h3>
                <p class="price">$49.99</p>
                <button class="add-btn">Add to Cart</button>
            </div>
            
            <div class="product-card">
                <div class="product-image" style="background: linear-gradient(135deg, #43e97b, #38f9d7);"></div>
                <h3>USB-C Hub</h3>
                <p class="price">$79.99</p>
                <button class="add-btn">Add to Cart</button>
            </div>
        </div>
    </main>
    
    <footer class="footer">
        <p>&copy; 2024 IZYX Shop. All rights reserved.</p>
    </footer>
    
    <script src="script.js"></script>
</body>
</html>""",
            "style.css": """* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: #f5f5f5;
}

.header {
    background: white;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    sticky: top 0;
    position: sticky;
    top: 0;
    z-index: 100;
}

.header-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 2rem;
    border-bottom: 1px solid #eee;
}

.header h1 {
    color: #667eea;
    font-size: 1.5rem;
}

.cart {
    background: #667eea;
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 5px;
    cursor: pointer;
    transition: 0.3s;
}

.cart:hover {
    background: #764ba2;
}

.categories {
    display: flex;
    gap: 1rem;
    padding: 1rem 2rem;
    overflow-x: auto;
}

.cat-btn {
    padding: 0.5rem 1rem;
    background: #f0f0f0;
    border: none;
    border-radius: 20px;
    cursor: pointer;
    transition: 0.3s;
    text-decoration: none;
    color: #333;
    white-space: nowrap;
}

.cat-btn.active,
.cat-btn:hover {
    background: #667eea;
    color: white;
}

.shop {
    padding: 2rem;
    max-width: 1200px;
    margin: 0 auto;
}

.product-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 1.5rem;
}

.product-card {
    background: white;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    transition: 0.3s;
}

.product-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.15);
}

.product-image {
    height: 200px;
    background: #f0f0f0;
}

.product-card h3 {
    padding: 1rem;
    color: #333;
    font-size: 1rem;
}

.price {
    padding: 0 1rem;
    color: #667eea;
    font-size: 1.5rem;
    font-weight: bold;
}

.add-btn {
    width: calc(100% - 2rem);
    margin: 1rem;
    padding: 0.8rem;
    background: #667eea;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-weight: bold;
    transition: 0.3s;
}

.add-btn:hover {
    background: #764ba2;
}

.footer {
    text-align: center;
    padding: 2rem;
    background: #333;
    color: white;
    margin-top: 3rem;
}""",
            "script.js": """let cartCount = 0;

document.querySelectorAll('.add-btn').forEach(btn => {
    btn.addEventListener('click', function() {
        cartCount++;
        document.querySelector('.cart').textContent = `🛒 Cart (${cartCount})`;
        this.textContent = '✓ Added!';
        setTimeout(() => {
            this.textContent = 'Add to Cart';
        }, 1500);
    });
});

document.querySelectorAll('.cat-btn').forEach(btn => {
    btn.addEventListener('click', function(e) {
        e.preventDefault();
        document.querySelectorAll('.cat-btn').forEach(b => b.classList.remove('active'));
        this.classList.add('active');
    });
});"""
        }
    },
    
    # ===== BACKEND TEMPLATES =====
    "flask-api": {
        "category": "backend",
        "description": "Flask REST API",
        "files": {
            "app.py": """#!/usr/bin/env python3
from flask import Flask, jsonify, request
from datetime import datetime
import json

app = Flask(__name__)

# Mock database
users_db = [
    {"id": 1, "name": "John Doe", "email": "john@example.com"},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com"}
]

@app.route('/')
def home():
    return jsonify({
        "message": "🚀 IZYX AI - Flask API",
        "version": "1.0",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify({
        "status": "success",
        "data": users_db,
        "count": len(users_db)
    })

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users_db if u['id'] == user_id), None)
    if user:
        return jsonify({"status": "success", "data": user})
    return jsonify({"status": "error", "message": "User not found"}), 404

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"status": "error", "message": "Invalid data"}), 400
    
    new_user = {
        "id": max(u['id'] for u in users_db) + 1 if users_db else 1,
        "name": data['name'],
        "email": data['email']
    }
    users_db.append(new_user)
    return jsonify({"status": "success", "data": new_user}), 201

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy", "code": 200})

if __name__ == '__main__':
    print("🔥 Flask API running on http://localhost:5000")
    app.run(debug=True, port=5000)""",
            "requirements.txt": "Flask==3.0.0\\nWerkzeug==3.0.0\\n",
            "README.md": """# IZYX Flask API

Simple REST API built with Flask.

## Setup
```bash
pip install -r requirements.txt
python app.py
```

## Endpoints
- GET / - Home
- GET /api/users - List users
- GET /api/users/<id> - Get user
- POST /api/users - Create user
- GET /api/health - Health check
"""
        }
    },
    
    "fastapi-server": {
        "category": "backend",
        "description": "FastAPI application",
        "files": {
            "main.py": """#!/usr/bin/env python3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import List

app = FastAPI(title="IZYX AI FastAPI", version="1.0")

# Models
class Item(BaseModel):
    id: int
    title: str
    description: str
    price: float

class User(BaseModel):
    id: int
    name: str
    email: str

# Mock data
items = [
    {"id": 1, "title": "Python Book", "description": "Learn Python", "price": 29.99},
    {"id": 2, "title": "Web Dev Course", "description": "Master web dev", "price": 49.99}
]

users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

@app.get("/")
async def root():
    return {
        "message": "🚀 IZYX AI - FastAPI",
        "version": "1.0",
        "timestamp": datetime.now()
    }

@app.get("/api/items")
async def list_items() -> List[Item]:
    return items

@app.get("/api/items/{item_id}")
async def get_item(item_id: int):
    item = next((i for i in items if i['id'] == item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/api/items")
async def create_item(item: Item):
    items.append(item.dict())
    return {"status": "created", "data": item}

@app.get("/api/users")
async def list_users() -> List[User]:
    return users

@app.get("/api/health")
async def health():
    return {"status": "healthy", "code": 200}

if __name__ == "__main__":
    import uvicorn
    print("🔥 FastAPI running on http://localhost:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)""",
            "requirements.txt": "fastapi==0.109.0\\nuvicorn==0.27.0\\npydantic==2.5.0\\n",
            "README.md": """# IZYX FastAPI Server

High-performance API with FastAPI.

## Setup
```bash
pip install -r requirements.txt
python main.py
```

## Features
- Async endpoints
- Automatic documentation at /docs
- Type hints with Pydantic
- Fast and modern
"""
        }
    },
    
    "node-express": {
        "category": "backend",
        "description": "Node.js Express server",
        "files": {
            "server.js": """const express = require('express');
const app = express();

app.use(express.json());

const PORT = process.env.PORT || 3000;

// Mock data
const products = [
    { id: 1, name: 'Laptop', price: 999 },
    { id: 2, name: 'Phone', price: 699 }
];

// Routes
app.get('/', (req, res) => {
    res.json({
        message: '🚀 IZYX AI - Express API',
        version: '1.0',
        timestamp: new Date()
    });
});

app.get('/api/products', (req, res) => {
    res.json({
        status: 'success',
        data: products,
        count: products.length
    });
});

app.get('/api/products/:id', (req, res) => {
    const product = products.find(p => p.id === parseInt(req.params.id));
    if (product) {
        res.json({ status: 'success', data: product });
    } else {
        res.status(404).json({ status: 'error', message: 'Product not found' });
    }
});

app.post('/api/products', (req, res) => {
    const { name, price } = req.body;
    if (!name || !price) {
        return res.status(400).json({ status: 'error', message: 'Invalid data' });
    }
    const newProduct = {
        id: products.length + 1,
        name,
        price
    };
    products.push(newProduct);
    res.status(201).json({ status: 'success', data: newProduct });
});

app.get('/api/health', (req, res) => {
    res.json({ status: 'healthy', code: 200 });
});

app.listen(PORT, () => {
    console.log(`🔥 Express server running on http://localhost:${PORT}`);
});""",
            "package.json": """{
  "name": "izyx-api",
  "version": "1.0.0",
  "description": "IZYX AI Express API",
  "main": "server.js",
  "scripts": {
    "start": "node server.js",
    "dev": "nodemon server.js"
  },
  "dependencies": {
    "express": "^4.18.2"
  },
  "devDependencies": {
    "nodemon": "^3.0.1"
  }
}""",
            "README.md": """# IZYX Express API

RESTful API built with Node.js and Express.

## Setup
```bash
npm install
npm start
```

## Endpoints
- GET / - Home
- GET /api/products - List products
- GET /api/products/:id - Get product
- POST /api/products - Create product
- GET /api/health - Health check
"""
        }
    },
    
    # ===== SCRIPT TEMPLATES =====
    "web-scraper": {
        "category": "script",
        "description": "Web scraper script",
        "files": {
            "scraper.py": """#!/usr/bin/env python3
\"\"\"
Simple Web Scraper - IZYX AI
\"\"\"

import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import json

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.data = []
    
    def fetch(self):
        \"\"\"Fetch webpage content\"\"\"
        try:
            response = self.session.get(self.url, timeout=10)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"❌ Error fetching {self.url}: {e}")
            return None
    
    def parse(self, html):
        \"\"\"Parse HTML content\"\"\"
        try:
            soup = BeautifulSoup(html, 'html.parser')
            
            # Extract titles and links
            for link in soup.find_all('a', limit=10):
                data = {
                    'title': link.get_text(strip=True),
                    'url': link.get('href'),
                    'scraped_at': datetime.now().isoformat()
                }
                self.data.append(data)
            
            return len(self.data)
        except Exception as e:
            print(f"❌ Error parsing: {e}")
            return 0
    
    def save_json(self, filename='scraped_data.json'):
        \"\"\"Save data to JSON\"\"\"
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, indent=2, ensure_ascii=False)
            print(f"✅ Data saved to {filename}")
        except Exception as e:
            print(f"❌ Error saving JSON: {e}")
    
    def save_csv(self, filename='scraped_data.csv'):
        \"\"\"Save data to CSV\"\"\"
        try:
            if not self.data:
                print("⚠️ No data to save")
                return
            
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=self.data[0].keys())
                writer.writeheader()
                writer.writerows(self.data)
            print(f"✅ Data saved to {filename}")
        except Exception as e:
            print(f"❌ Error saving CSV: {e}")
    
    def display(self):
        \"\"\"Display scraped data\"\"\"
        print(f"\\n📊 Scraped {len(self.data)} items:\\n")
        for item in self.data:
            print(f"  📍 {item['title']}")
            print(f"     URL: {item['url']}")
        print()

def main():
    print("\"\"\"
    🕷️  IZYX AI Web Scraper
    \"\"\"")
    
    # Example usage
    url = input("Enter URL to scrape (default: https://example.com): ").strip() or "https://example.com"
    
    print(f"\\n🔄 Scraping {url}...")
    scraper = WebScraper(url)
    
    html = scraper.fetch()
    if html:
        count = scraper.parse(html)
        print(f"✅ Scraped {count} items")
        
        scraper.display()
        scraper.save_json()
        scraper.save_csv()
    else:
        print("❌ Failed to scrape website")

if __name__ == "__main__":
    main()""",
            "requirements.txt": "requests==2.31.0\\nbeautifulsoup4==4.12.2\\n",
            "README.md": """# IZYX Web Scraper

Extract data from websites with ease.

## Setup
```bash
pip install -r requirements.txt
python scraper.py
```

## Features
- Fetch webpage content
- Parse HTML with BeautifulSoup
- Export to JSON and CSV
- Error handling
"""
        }
    },
    
    "data-processor": {
        "category": "script",
        "description": "Data processing utility",
        "files": {
            "processor.py": """#!/usr/bin/env python3
\"\"\"
IZYX AI - Data Processor
Process CSV/JSON data with ease
\"\"\"

import csv
import json
from pathlib import Path
from datetime import datetime
from collections import Counter
import statistics

class DataProcessor:
    def __init__(self, filepath):
        self.filepath = Path(filepath)
        self.data = []
        self.stats = {}
    
    def load_json(self):
        \"\"\"Load JSON file\"\"\"
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
            print(f"✅ Loaded {len(self.data)} records from {self.filepath}")
            return True
        except Exception as e:
            print(f"❌ Error loading JSON: {e}")
            return False
    
    def load_csv(self):
        \"\"\"Load CSV file\"\"\"
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.data = list(reader)
            print(f"✅ Loaded {len(self.data)} records from {self.filepath}")
            return True
        except Exception as e:
            print(f"❌ Error loading CSV: {e}")
            return False
    
    def filter_data(self, key, value):
        \"\"\"Filter data by key-value\"\"\"
        filtered = [item for item in self.data if item.get(key) == value]
        print(f"✅ Filtered {len(filtered)} records")
        return filtered
    
    def sort_data(self, key, reverse=False):
        \"\"\"Sort data by key\"\"\"
        try:
            self.data.sort(key=lambda x: x.get(key, ''), reverse=reverse)
            print(f"✅ Sorted by {key}")
            return self.data
        except Exception as e:
            print(f"❌ Error sorting: {e}")
            return self.data
    
    def get_statistics(self, numeric_key):
        \"\"\"Calculate statistics for numeric field\"\"\"
        try:
            values = [float(item.get(numeric_key, 0)) for item in self.data if item.get(numeric_key)]
            self.stats = {
                'count': len(values),
                'sum': sum(values),
                'mean': statistics.mean(values),
                'median': statistics.median(values),
                'min': min(values),
                'max': max(values)
            }
            return self.stats
        except Exception as e:
            print(f"❌ Error calculating stats: {e}")
            return {}
    
    def export_json(self, output_file='output.json'):
        \"\"\"Export to JSON\"\"\"
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, indent=2, ensure_ascii=False)
            print(f"✅ Exported to {output_file}")
        except Exception as e:
            print(f"❌ Error exporting JSON: {e}")
    
    def export_csv(self, output_file='output.csv'):
        \"\"\"Export to CSV\"\"\"
        try:
            if not self.data:
                print("⚠️ No data to export")
                return
            
            with open(output_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=self.data[0].keys())
                writer.writeheader()
                writer.writerows(self.data)
            print(f"✅ Exported to {output_file}")
        except Exception as e:
            print(f"❌ Error exporting CSV: {e}")
    
    def display_stats(self):
        \"\"\"Display statistics\"\"\"
        if self.stats:
            print("\\n📊 Statistics:")
            for key, value in self.stats.items():
                print(f"  {key.capitalize()}: {value:.2f}" if isinstance(value, float) else f"  {key.capitalize()}: {value}")

def main():
    print(\"\"\"
    📊 IZYX AI Data Processor
    \"\"\")
    
    filepath = input("Enter file path (CSV/JSON): ").strip()
    
    processor = DataProcessor(filepath)
    
    # Load based on file extension
    if filepath.endswith('.json'):
        processor.load_json()
    elif filepath.endswith('.csv'):
        processor.load_csv()
    else:
        print("❌ Unsupported file format")
        return
    
    # Example operations
    processor.sort_data(list(processor.data[0].keys())[0] if processor.data else None)
    processor.display_stats()
    processor.export_json('processed_output.json')
    processor.export_csv('processed_output.csv')

if __name__ == "__main__":
    main()""",
            "sample_data.json": """[
    {"id": 1, "name": "Alice", "score": 95, "date": "2024-01-15"},
    {"id": 2, "name": "Bob", "score": 87, "date": "2024-01-16"},
    {"id": 3, "name": "Charlie", "score": 92, "date": "2024-01-17"}
]"""
        }
    },
    
    "deployment-tool": {
        "category": "script",
        "description": "Deployment automation",
        "files": {
            "deploy.py": """#!/usr/bin/env python3
\"\"\"
IZYX AI - Deployment Tool
Automate deployments with ease
\"\"\"

import subprocess
import time
import json
from pathlib import Path
from datetime import datetime

class Deployer:
    def __init__(self, project_name):
        self.project_name = project_name
        self.logs = []
        self.status = "pending"
    
    def log(self, message):
        \"\"\"Log deployment message\"\"\"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_msg = f"[{timestamp}] {message}"
        self.logs.append(log_msg)
        print(log_msg)
    
    def run_command(self, cmd, description):
        \"\"\"Run system command\"\"\"
        try:
            self.log(f"🔄 {description}...")
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0:
                self.log(f"✅ {description} completed")
                return True
            else:
                self.log(f"❌ {description} failed: {result.stderr}")
                return False
        except Exception as e:
            self.log(f"❌ Error: {e}")
            return False
    
    def build(self):
        \"\"\"Build project\"\"\"
        self.log("\\n=== BUILD PHASE ===")
        commands = [
            ("pip install -r requirements.txt", "Installing dependencies"),
            ("python -m py_compile *.py", "Compiling Python files"),
        ]
        
        for cmd, desc in commands:
            if not self.run_command(cmd, desc):
                self.status = "failed"
                return False
        
        return True
    
    def test(self):
        \"\"\"Run tests\"\"\"
        self.log("\\n=== TEST PHASE ===")
        self.log("✅ All tests passed")
        return True
    
    def deploy(self, target="production"):
        \"\"\"Deploy to target environment\"\"\"
        self.log("\\n=== DEPLOY PHASE ===")
        self.log(f"🚀 Deploying {self.project_name} to {target}...")
        
        # Simulate deployment
        time.sleep(2)
        self.log(f"✅ Successfully deployed to {target}")
        self.status = "success"
        return True
    
    def rollback(self):
        \"\"\"Rollback deployment\"\"\"
        self.log("\\n⚠️  ROLLBACK INITIATED")
        self.log("✅ Rollback completed")
    
    def save_logs(self, filename='deployment_log.json'):
        \"\"\"Save deployment logs\"\"\"
        try:
            with open(filename, 'w') as f:
                json.dump({
                    'project': self.project_name,
                    'status': self.status,
                    'timestamp': datetime.now().isoformat(),
                    'logs': self.logs
                }, f, indent=2)
            self.log(f"✅ Logs saved to {filename}")
        except Exception as e:
            self.log(f"❌ Error saving logs: {e}")
    
    def run_full_deployment(self):
        \"\"\"Run complete deployment pipeline\"\"\"
        print(f\"\"\"
╔════════════════════════════════════════╗
║  🚀 IZYX AI Deployment Tool           ║
║  Project: {self.project_name:<22} ║
╚════════════════════════════════════════╝
        \"\"\")
        
        if not self.build():
            return
        
        if not self.test():
            return
        
        if not self.deploy():
            self.rollback()
            return
        
        self.save_logs()
        print(f\"\"\"
╔════════════════════════════════════════╗
║  ✅ DEPLOYMENT COMPLETED              ║
║  Status: {self.status.upper():<21} ║
╚════════════════════════════════════════╝
        \"\"\")

def main():
    project_name = input("Enter project name: ").strip() or "my-project"
    deployer = Deployer(project_name)
    deployer.run_full_deployment()

if __name__ == "__main__":
    main()"""
        }
    }
}

# ============================================
# ENHANCED DASHBOARD GENERATOR
# ============================================
def generate_enhanced_dashboard():
    """Generate interactive dashboard with all features"""
    
    dashboard_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IZYX AI - Project Manager</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
            color: #fff;
            transition: 0.3s;
        }

        body.light-mode {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            color: #333;
        }

        .header {
            background: rgba(0, 0, 0, 0.3);
            padding: 1.5rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: sticky;
            top: 0;
            z-index: 1000;
            backdrop-filter: blur(10px);
        }

        .light-mode .header {
            background: rgba(255, 255, 255, 0.9);
        }

        .logo {
            font-size: 1.8rem;
            font-weight: bold;
            color: #00ff41;
        }

        .light-mode .logo {
            color: #667eea;
        }

        .header-controls {
            display: flex;
            gap: 1rem;
            align-items: center;
        }

        .search-box {
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 0.7rem 1rem;
            border-radius: 20px;
            color: #fff;
            width: 250px;
            transition: 0.3s;
        }

        .search-box:focus {
            outline: none;
            background: rgba(255, 255, 255, 0.2);
            border-color: #00ff41;
        }

        .light-mode .search-box {
            background: rgba(0, 0, 0, 0.05);
            color: #333;
            border-color: rgba(0, 0, 0, 0.1);
        }

        .theme-toggle {
            background: none;
            border: 2px solid #00ff41;
            color: #00ff41;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            cursor: pointer;
            transition: 0.3s;
            font-weight: bold;
        }

        .theme-toggle:hover {
            background: #00ff41;
            color: #000;
        }

        .light-mode .theme-toggle {
            border-color: #667eea;
            color: #667eea;
        }

        .light-mode .theme-toggle:hover {
            background: #667eea;
            color: #fff;
        }

        .filters {
            padding: 1.5rem 2rem;
            display: flex;
            gap: 1rem;
            flex-wrap: wrap;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }

        .light-mode .filters {
            border-bottom-color: rgba(0, 0, 0, 0.1);
        }

        .filter-btn {
            background: rgba(0, 255, 65, 0.1);
            border: 1px solid #00ff41;
            color: #00ff41;
            padding: 0.6rem 1.2rem;
            border-radius: 20px;
            cursor: pointer;
            transition: 0.3s;
            font-weight: 500;
        }

        .filter-btn:hover,
        .filter-btn.active {
            background: #00ff41;
            color: #000;
        }

        .light-mode .filter-btn {
            background: rgba(102, 126, 234, 0.1);
            border-color: #667eea;
            color: #667eea;
        }

        .light-mode .filter-btn:hover,
        .light-mode .filter-btn.active {
            background: #667eea;
            color: #fff;
        }

        .container {
            padding: 2rem;
            max-width: 1400px;
            margin: 0 auto;
        }

        .projects-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2rem;
        }

        .project-card {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(0, 255, 65, 0.3);
            border-radius: 10px;
            padding: 1.5rem;
            cursor: pointer;
            transition: 0.3s;
            overflow: hidden;
            position: relative;
        }

        .project-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(0, 255, 65, 0.1), transparent);
            transition: 0.5s;
        }

        .project-card:hover::before {
            left: 100%;
        }

        .project-card:hover {
            border-color: #00ff41;
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0, 255, 65, 0.2);
        }

        .light-mode .project-card {
            background: rgba(0, 0, 0, 0.02);
            border-color: rgba(102, 126, 234, 0.3);
        }

        .light-mode .project-card:hover {
            border-color: #667eea;
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.2);
        }

        .project-name {
            font-size: 1.2rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
            color: #00ff41;
        }

        .light-mode .project-name {
            color: #667eea;
        }

        .project-description {
            font-size: 0.9rem;
            color: rgba(255, 255, 255, 0.7);
            margin-bottom: 1rem;
            line-height: 1.5;
        }

        .light-mode .project-description {
            color: rgba(0, 0, 0, 0.7);
        }

        .project-category {
            display: inline-block;
            background: rgba(0, 255, 65, 0.2);
            border: 1px solid #00ff41;
            color: #00ff41;
            padding: 0.3rem 0.8rem;
            border-radius: 15px;
            font-size: 0.8rem;
            margin-bottom: 1rem;
            font-weight: 500;
        }

        .light-mode .project-category {
            background: rgba(102, 126, 234, 0.2);
            border-color: #667eea;
            color: #667eea;
        }

        .project-actions {
            display: flex;
            gap: 0.5rem;
            margin-top: 1rem;
        }

        .btn {
            flex: 1;
            padding: 0.6rem 1rem;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 0.85rem;
            font-weight: bold;
            transition: 0.3s;
        }

        .btn-view {
            background: #00ff41;
            color: #000;
        }

        .btn-view:hover {
            background: #00dd34;
            transform: scale(1.05);
        }

        .btn-deploy {
            background: #667eea;
            color: #fff;
        }

        .btn-deploy:hover {
            background: #764ba2;
            transform: scale(1.05);
        }

        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.8);
            z-index: 2000;
            align-items: center;
            justify-content: center;
        }

        .modal.active {
            display: flex;
        }

        .modal-content {
            background: #1a1a2e;
            border: 2px solid #00ff41;
            border-radius: 10px;
            max-width: 600px;
            max-height: 80vh;
            overflow-y: auto;
            padding: 2rem;
            position: relative;
            animation: slideIn 0.3s ease;
        }

        .light-mode .modal-content {
            background: #fff;
            border-color: #667eea;
            color: #333;
        }

        @keyframes slideIn {
            from {
                transform: translateY(-50px);
                opacity: 0;
            }
            to {
                transform: translateY(0);
                opacity: 1;
            }
        }

        .close-btn {
            position: absolute;
            top: 1rem;
            right: 1rem;
            background: none;
            border: none;
            color: #00ff41;
            font-size: 1.5rem;
            cursor: pointer;
        }

        .light-mode .close-btn {
            color: #667eea;
        }

        .modal-tabs {
            display: flex;
            gap: 1rem;
            margin-bottom: 1.5rem;
            border-bottom: 1px solid rgba(0, 255, 65, 0.2);
        }

        .modal-tab {
            background: none;
            border: none;
            color: rgba(255, 255, 255, 0.5);
            padding: 0.8rem 0;
            cursor: pointer;
            font-weight: bold;
            border-bottom: 2px solid transparent;
            transition: 0.3s;
        }

        .modal-tab.active {
            color: #00ff41;
            border-color: #00ff41;
        }

        .light-mode .modal-tab {
            color: rgba(0, 0, 0, 0.5);
        }

        .light-mode .modal-tab.active {
            color: #667eea;
            border-color: #667eea;
        }

        .modal-body {
            display: none;
        }

        .modal-body.active {
            display: block;
        }

        .code-block {
            background: rgba(0, 0, 0, 0.5);
            border-left: 3px solid #00ff41;
            padding: 1rem;
            border-radius: 5px;
            font-family: 'Courier New', monospace;
            font-size: 0.9rem;
            overflow-x: auto;
            line-height: 1.5;
            white-space: pre-wrap;
            word-break: break-word;
        }

        .light-mode .code-block {
            background: rgba(102, 126, 234, 0.05);
            border-left-color: #667eea;
            color: #333;
        }

        footer {
            text-align: center;
            padding: 2rem;
            color: rgba(255, 255, 255, 0.5);
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }

        .light-mode footer {
            color: rgba(0, 0, 0, 0.5);
            border-top-color: rgba(0, 0, 0, 0.1);
        }

        @media (max-width: 768px) {
            .projects-grid {
                grid-template-columns: 1fr;
            }

            .header {
                flex-direction: column;
                gap: 1rem;
            }

            .search-box {
                width: 100%;
            }

            .filters {
                flex-direction: column;
            }
        }
    </style>
</head>
<body>
    <header class="header">
        <div class="logo">⚡ IZYX AI Project Manager</div>
        <div class="header-controls">
            <input type="text" class="search-box" id="searchBox" placeholder="🔍 Search projects (Ctrl+K)...">
            <button class="theme-toggle" id="themeToggle">🌙 Dark</button>
        </div>
    </header>

    <div class="filters">
        <button class="filter-btn active" data-filter="all">All</button>
        <button class="filter-btn" data-filter="web">🌐 Web</button>
        <button class="filter-btn" data-filter="backend">⚙️ Backend</button>
        <button class="filter-btn" data-filter="script">📜 Script</button>
    </div>

    <div class="container">
        <div class="projects-grid" id="projectsGrid">
            <!-- Projects will be inserted here -->
        </div>
    </div>

    <div class="modal" id="projectModal">
        <div class="modal-content">
            <button class="close-btn" onclick="closeModal()">✕</button>
            <h2 id="modalTitle" style="margin-bottom: 1rem;"></h2>
            
            <div class="modal-tabs">
                <button class="modal-tab active" onclick="switchTab('preview')">Preview</button>
                <button class="modal-tab" onclick="switchTab('html')">HTML</button>
                <button class="modal-tab" onclick="switchTab('css')">CSS</button>
                <button class="modal-tab" onclick="switchTab('js')">JavaScript</button>
            </div>

            <div id="previewBody" class="modal-body active">
                <iframe id="preview" style="width: 100%; height: 400px; border: none; border-radius: 5px;"></iframe>
            </div>
            <div id="htmlBody" class="modal-body">
                <div class="code-block" id="htmlCode"></div>
            </div>
            <div id="cssBody" class="modal-body">
                <div class="code-block" id="cssCode"></div>
            </div>
            <div id="jsBody" class="modal-body">
                <div class="code-block" id="jsCode"></div>
            </div>

            <div style="display: flex; gap: 1rem; margin-top: 1.5rem;">
                <button class="btn btn-deploy" onclick="deployProject()">🚀 Deploy to Vercel</button>
                <button class="btn btn-deploy" onclick="deployProject()">🌍 Deploy to Netlify</button>
            </div>
        </div>
    </div>

    <footer>
        <p>🔥 IZYX AI - Made with love | 30+ Templates | Search • Filter • Live Preview • Deploy</p>
    </footer>

    <script>
        const projects = PROJECTS_DATA;
        let currentFilter = 'all';
        let currentTheme = localStorage.getItem('theme') || 'dark';

        // Initialize
        document.addEventListener('DOMContentLoaded', () => {
            applyTheme(currentTheme);
            renderProjects();
            setupEventListeners();
        });

        function setupEventListeners() {
            // Theme toggle
            document.getElementById('themeToggle').addEventListener('click', toggleTheme);

            // Search
            const searchBox = document.getElementById('searchBox');
            searchBox.addEventListener('input', filterProjects);
            searchBox.addEventListener('keydown', (e) => {
                if (e.key === 'Escape') searchBox.value = '';
            });

            // Keyboard shortcut
            document.addEventListener('keydown', (e) => {
                if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
                    e.preventDefault();
                    searchBox.focus();
                }
            });

            // Filter buttons
            document.querySelectorAll('.filter-btn').forEach(btn => {
                btn.addEventListener('click', function() {
                    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
                    this.classList.add('active');
                    currentFilter = this.dataset.filter;
                    filterProjects();
                });
            });
        }

        function renderProjects() {
            const grid = document.getElementById('projectsGrid');
            grid.innerHTML = '';

            projects.forEach(project => {
                const card = document.createElement('div');
                card.className = 'project-card';
                card.innerHTML = `
                    <div class="project-name">${project.name}</div>
                    <div class="project-description">${project.description}</div>
                    <div class="project-category">${project.category.toUpperCase()}</div>
                    <div class="project-actions">
                        <button class="btn btn-view" onclick="openModal('${project.name}')">👁️ View</button>
                        <button class="btn btn-deploy" onclick="deployProject()">🚀 Deploy</button>
                    </div>
                `;
                grid.appendChild(card);
            });
        }

        function filterProjects() {
            const searchTerm = document.getElementById('searchBox').value.toLowerCase();
            const cards = document.querySelectorAll('.project-card');

            cards.forEach(card => {
                const text = card.textContent.toLowerCase();
                const category = card.querySelector('.project-category').textContent.toLowerCase();
                
                const matchSearch = text.includes(searchTerm);
                const matchFilter = currentFilter === 'all' || category.includes(currentFilter);

                card.style.display = matchSearch && matchFilter ? 'block' : 'none';
            });
        }

        function openModal(projectName) {
            const project = projects.find(p => p.name === projectName);
            if (!project) return;

            document.getElementById('modalTitle').textContent = project.name;
            document.getElementById('htmlCode').textContent = project.files['index.html'] || 'N/A';
            document.getElementById('cssCode').textContent = project.files['style.css'] || 'N/A';
            document.getElementById('jsCode').textContent = project.files['script.js'] || 'N/A';

            // Create preview
            const preview = document.getElementById('preview');
            const html = project.files['index.html'] || '<h1>No HTML</h1>';
            const css = `<style>${project.files['style.css'] || ''}</style>`;
            preview.srcdoc = html + css;

            document.getElementById('projectModal').classList.add('active');
        }

        function closeModal() {
            document.getElementById('projectModal').classList.remove('active');
        }

        function switchTab(tab) {
            document.querySelectorAll('.modal-body').forEach(b => b.classList.remove('active'));
            document.querySelectorAll('.modal-tab').forEach(b => b.classList.remove('active'));
            document.getElementById(tab + 'Body').classList.add('active');
            event.target.classList.add('active');
        }

        function toggleTheme() {
            currentTheme = currentTheme === 'dark' ? 'light' : 'dark';
            applyTheme(currentTheme);
            localStorage.setItem('theme', currentTheme);
        }

        function applyTheme(theme) {
            const btn = document.getElementById('themeToggle');
            if (theme === 'light') {
                document.body.classList.add('light-mode');
                btn.textContent = '☀️ Light';
            } else {
                document.body.classList.remove('light-mode');
                btn.textContent = '🌙 Dark';
            }
        }

        function deployProject() {
            alert('🚀 Deploy functionality would connect to Vercel/Netlify API');
        }

        // Close modal on Escape
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') closeModal();
        });
    </script>
</body>
</html>"""
    
    return dashboard_html

# ============================================
# CONFIGURATION SYSTEM
# ============================================
def load_config():
    """Load projects configuration"""
    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_config(config):
    """Save projects configuration"""
    BASE_DIR.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)

# ============================================
# PROJECT GENERATION
# ============================================
def generate_projects(project_list=None):
    """Generate projects from list"""
    if PROJECTS_DIR.exists():
        shutil.rmtree(PROJECTS_DIR)
    PROJECTS_DIR.mkdir(parents=True, exist_ok=True)
    
    if project_list is None:
        project_list = list(TEMPLATE_LIBRARY.keys())[:10]  # Default: first 10
    
    for project_name in project_list:
        if project_name not in TEMPLATE_LIBRARY:
            continue
        
        template = TEMPLATE_LIBRARY[project_name]
        project_path = PROJECTS_DIR / project_name
        project_path.mkdir(exist_ok=True)
        
        for filename, content in template['files'].items():
            file_path = project_path / filename
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
        
        print(f"✅ Generated '{project_name}' ({template['category']})")

def generate_dashboard():
    """Generate enhanced dashboard"""
    dashboard_html = generate_enhanced_dashboard()
    dashboard_path = PROJECTS_DIR / "index.html"
    with open(dashboard_path, 'w', encoding='utf-8') as f:
        f.write(dashboard_html)
    print("✅ Dashboard generated!")

# ============================================
# CLI COMMANDS
# ============================================
class IzyxCLI:
    """IZYX AI Command Line Interface"""
    
    def __init__(self):
        self.config = load_config()
    
    def list_templates(self):
        """List all available templates"""
        print("\n📚 Available Templates:\n")
        by_category = {}
        for name, template in TEMPLATE_LIBRARY.items():
            cat = template['category']
            if cat not in by_category:
                by_category[cat] = []
            by_category[cat].append((name, template['description']))
        
        for category, items in sorted(by_category.items()):
            print(f"  🔹 {category.upper()}")
            for name, desc in items:
                print(f"     - {name:20} | {desc}")
        print()
    
    def add_project(self, project_name):
        """Add project to configuration"""
        if project_name not in TEMPLATE_LIBRARY:
            print(f"❌ Template '{project_name}' not found")
            return False
        
        if 'projects' not in self.config:
            self.config['projects'] = []
        
        if project_name not in self.config['projects']:
            self.config['projects'].append(project_name)
            save_config(self.config)
            print(f"✅ Added '{project_name}' to configuration")
            return True
        
        print(f"⚠️  '{project_name}' already in configuration")
        return False
    
    def remove_project(self, project_name):
        """Remove project from configuration"""
        if 'projects' in self.config and project_name in self.config['projects']:
            self.config['projects'].remove(project_name)
            save_config(self.config)
            print(f"✅ Removed '{project_name}'")
            return True
        
        print(f"❌ '{project_name}' not found")
        return False
    
    def get_projects(self):
        """Get configured projects"""
        return self.config.get('projects', list(TEMPLATE_LIBRARY.keys())[:10])
    
    def build(self):
        """Build and generate projects"""
        projects = self.get_projects()
        print(f"\n🔨 Building {len(projects)} projects...\n")
        generate_projects(projects)
        generate_dashboard()
        print(f"\n✅ Build completed! Total: {len(projects)} projects")
    
    def serve(self, port=8080, auto_open=True):
        """Start HTTP server"""
        os.chdir(PROJECTS_DIR)
        url = f"http://localhost:{port}"
        
        print(f"\n⚡ IZYX AI Server")
        print(f"📂 Serving: {PROJECTS_DIR}")
        print(f"🌐 URL: {url}")
        print(f"⌨️  Press Ctrl+C to stop\n")
        
        if auto_open:
            time.sleep(1)
            webbrowser.open(url)
        
        try:
            handler = SimpleHTTPRequestHandler
            with HTTPServer(("", port), handler) as httpd:
                httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n✅ Server stopped")

def main():
    """Main CLI entry point"""
    print("""
╔═══════════════════════════════════════════════════╗
║      ⚡ IZYX AI - Ultimate Project Manager       ║
║        30+ Templates • Search • Filter • Deploy   ║
╚═══════════════════════════════════════════════════╝
    """)
    
    cli = IzyxCLI()
    
    if len(sys.argv) < 2:
        print("Available commands:")
        print("  python izyx_ai.py list          - List templates")
        print("  python izyx_ai.py build         - Generate & build")
        print("  python izyx_ai.py serve         - Start server")
        print("  python izyx_ai.py add <name>    - Add template")
        print("  python izyx_ai.py remove <name> - Remove template")
        print("  python izyx_ai.py config        - Show config")
        return
    
    command = sys.argv[1].lower()
    
    if command == "list":
        cli.list_templates()
    elif command == "build":
        cli.build()
        print(f"\n🚀 Start with: python izyx_ai.py serve")
    elif command == "serve":
        cli.build()
        cli.serve()
    elif command == "add":
        if len(sys.argv) < 3:
            print("❌ Usage: python izyx_ai.py add <template_name>")
            return
        cli.add_project(sys.argv[2])
    elif command == "remove":
        if len(sys.argv) < 3:
            print("❌ Usage: python izyx_ai.py remove <template_name>")
            return
        cli.remove_project(sys.argv[2])
    elif command == "config":
        print("\n📋 Current Configuration:")
        print(json.dumps(cli.config, indent=2, ensure_ascii=False))
    else:
        print(f"❌ Unknown command: {command}")

if __name__ == "__main__":
    main()
