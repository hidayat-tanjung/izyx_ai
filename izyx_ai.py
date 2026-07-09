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
    position: sticky; /* ✅ Perbaikan */
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
