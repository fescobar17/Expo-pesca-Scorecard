import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="Evaluador de Madurez de Automatización")

st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        [data-testid="stAppViewContainer"] { background-color: #faf9f7; }
        .block-container {
            padding-top: 0rem; padding-bottom: 0rem;
            padding-left: 0rem; padding-right: 0rem;
            max-width: 100%;
        }
        .stDeployButton { display:none; }
    </style>
""", unsafe_allow_html=True)

APPS_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbyz9dbdr_Y3wPQLr16sFhBBeTlhhYHwW_DT_4q3f-qKAgJnXCr4UPmYFdyvZ7TH9qBJ/exec"

codigo_html = f"""
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@300;400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<style>
*{{box-sizing:border-box;margin:0;padding:0;-webkit-tap-highlight-color:transparent}}
:root{{
  --orange:#ff5b00;
  --orange-light:#ff7a2e;
  --orange-dim:rgba(255,91,0,0.08);
  --orange-mid:rgba(255,91,0,0.15);
  --orange-border:rgba(255,91,0,0.25);
  --bg:#faf9f7;
  --card:#ffffff;
  --text:#111827;
  --text-2:#374151;
  --muted:#9ca3af;
  --border:#e8e3dc;
  --border-2:#f0ece6;
  --shadow:0 1px 3px rgba(0,0,0,0.06),0 4px 16px rgba(0,0,0,0.06);
  --shadow-hover:0 4px 20px rgba(255,91,0,0.15),0 8px 32px rgba(0,0,0,0.08);
}}
html,body{{height:100%;background:var(--bg)}}
#app{{
  font-family:'DM Sans',sans-serif;
  background:var(--bg);
  min-height:100vh;
  color:var(--text);
  position:relative;
  overflow-x:hidden;
}}

/* ── NOISE TEXTURE ── */
#app::before{{
  content:'';
  position:fixed;
  inset:0;
  background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.03'/%3E%3C/svg%3E");
  pointer-events:none;
  z-index:0;
  opacity:0.4;
}}

/* ── DECORATIVE BG SHAPES ── */
.bg-shape{{
  position:fixed;
  border-radius:50%;
  pointer-events:none;
  z-index:0;
}}
.bg-shape-1{{
  width:600px;height:600px;
  top:-200px;right:-200px;
  background:radial-gradient(circle,rgba(255,91,0,0.06) 0%,transparent 65%);
}}
.bg-shape-2{{
  width:400px;height:400px;
  bottom:-100px;left:-100px;
  background:radial-gradient(circle,rgba(255,91,0,0.04) 0%,transparent 65%);
}}

/* ── SCREENS ── */
.screen{{
  position:relative;
  z-index:1;
  min-height:100vh;
  padding:1.5rem 1rem;
  display:flex;
  flex-direction:column;
  align-items:center;
  justify-content:flex-start;
}}
@media(min-width:640px){{
  .screen{{padding:2.5rem 1.5rem;justify-content:center}}
}}

/* ── CARD ── */
.card{{
  background:var(--card);
  border:1px solid var(--border);
  border-radius:20px;
  box-shadow:var(--shadow);
  width:100%;
  max-width:520px;
}}
.card-lg{{max-width:600px}}

/* ──────────────────── INTRO ──────────────────── */
#intro-screen .card{{padding:0;overflow:hidden}}
.intro-image-wrap{{
  width:100%;
  height:200px;
  overflow:hidden;
  position:relative;
  background:#111827;
}}
@media(min-width:640px){{
  .intro-image-wrap{{height:240px}}
}}
.intro-image-wrap img{{
  width:100%;
  height:100%;
  object-fit:cover;
  object-position:center;
  display:block;
  opacity:0.92;
}}
.intro-image-overlay{{
  position:absolute;
  inset:0;
  background:linear-gradient(to bottom,rgba(0,0,0,0) 40%,rgba(255,255,255,1) 100%);
}}
.intro-brand{{
  display:flex;
  align-items:center;
  gap:8px;
  position:absolute;
  top:16px;
  left:20px;
  background:rgba(255,255,255,0.92);
  backdrop-filter:blur(8px);
  border-radius:50px;
  padding:6px 14px 6px 8px;
  border:1px solid rgba(255,91,0,0.2);
}}
.intro-brand-dot{{
  width:28px;height:28px;
  background:var(--orange);
  border-radius:50%;
  display:flex;align-items:center;justify-content:center;
  flex-shrink:0;
}}
.intro-brand-dot svg{{display:block}}
.intro-brand-name{{
  font-family:'Sora',sans-serif;
  font-size:0.72rem;
  font-weight:700;
  color:var(--text);
  letter-spacing:0.5px;
}}
.intro-body{{padding:0 1.5rem 2rem}}
@media(min-width:640px){{.intro-body{{padding:0 2rem 2.5rem}}}}
.intro-tag{{
  display:inline-flex;
  align-items:center;
  gap:6px;
  font-family:'Sora',sans-serif;
  font-size:0.68rem;
  font-weight:700;
  text-transform:uppercase;
  letter-spacing:1.5px;
  color:var(--orange);
  background:var(--orange-dim);
  border:1px solid var(--orange-border);
  border-radius:50px;
  padding:5px 12px;
  margin-bottom:1rem;
  margin-top:-1rem;
  position:relative;
  z-index:1;
}}
.intro-tag::before{{
  content:'';width:6px;height:6px;
  background:var(--orange);
  border-radius:50%;
  flex-shrink:0;
}}
h1.hero{{
  font-family:'Sora',sans-serif;
  font-size:clamp(1.7rem,6vw,2.4rem);
  font-weight:800;
  line-height:1.1;
  color:var(--text);
  margin-bottom:0.75rem;
}}
.hero-accent{{color:var(--orange)}}
.intro-desc{{
  font-size:0.95rem;
  line-height:1.65;
  color:#6b7280;
  margin-bottom:1.5rem;
  font-weight:300;
}}
.stats-strip{{
  display:flex;
  gap:0;
  margin-bottom:1.75rem;
  border:1px solid var(--border);
  border-radius:14px;
  overflow:hidden;
  background:var(--bg);
}}
.stat-cell{{
  flex:1;
  text-align:center;
  padding:12px 8px;
}}
.stat-cell+.stat-cell{{border-left:1px solid var(--border)}}
.stat-n{{
  font-family:'Sora',sans-serif;
  font-size:1.5rem;
  font-weight:800;
  color:var(--orange);
  line-height:1;
}}
.stat-l{{
  font-size:0.65rem;
  font-weight:500;
  color:var(--muted);
  text-transform:uppercase;
  letter-spacing:0.8px;
  margin-top:3px;
}}
.btn-primary{{
  width:100%;
  background:var(--orange);
  color:#fff;
  font-family:'Sora',sans-serif;
  font-weight:700;
  font-size:0.95rem;
  padding:16px 24px;
  border:none;
  border-radius:14px;
  cursor:pointer;
  letter-spacing:0.3px;
  display:flex;
  align-items:center;
  justify-content:center;
  gap:10px;
  transition:all 0.25s ease;
  -webkit-appearance:none;
  position:relative;
  overflow:hidden;
}}
.btn-primary::after{{
  content:'';
  position:absolute;
  inset:0;
  background:linear-gradient(135deg,rgba(255,255,255,0.1),transparent);
}}
.btn-primary:hover,.btn-primary:active{{
  background:#e05000;
  transform:translateY(-1px);
  box-shadow:0 6px 24px rgba(255,91,0,0.35);
}}
.btn-primary svg{{flex-shrink:0;transition:transform 0.25s}}
.btn-primary:hover svg{{transform:translateX(3px)}}
.intro-disclaimer{{
  margin-top:0.9rem;
  font-size:0.72rem;
  color:var(--muted);
  text-align:center;
  line-height:1.5;
}}

/* ──────────────────── QUIZ ──────────────────── */
#quiz-screen{{display:none}}
#quiz-screen .inner{{
  width:100%;
  max-width:520px;
  display:flex;
  flex-direction:column;
  gap:1rem;
}}
.prog-header{{
  display:flex;
  flex-direction:column;
  gap:8px;
}}
.prog-meta{{
  display:flex;
  justify-content:space-between;
  align-items:center;
}}
.prog-label{{
  font-family:'Sora',sans-serif;
  font-size:0.72rem;
  font-weight:700;
  text-transform:uppercase;
  letter-spacing:1px;
  color:var(--muted);
}}
.prog-counter{{
  font-family:'Sora',sans-serif;
  font-size:0.75rem;
  font-weight:700;
  color:var(--orange);
  background:var(--orange-dim);
  border:1px solid var(--orange-border);
  padding:3px 10px;
  border-radius:50px;
}}
.prog-track{{
  height:5px;
  background:var(--border-2);
  border-radius:10px;
  overflow:hidden;
}}
.prog-fill{{
  height:100%;
  background:linear-gradient(90deg,var(--orange),var(--orange-light));
  border-radius:10px;
  transition:width 0.5s cubic-bezier(0.4,0,0.2,1);
  width:0%;
}}
.dim-pills{{
  display:flex;
  gap:6px;
  flex-wrap:wrap;
}}
.dim-pill{{
  font-size:0.65rem;
  font-weight:600;
  letter-spacing:0.5px;
  padding:4px 10px;
  border-radius:50px;
  border:1px solid var(--border);
  color:var(--muted);
  background:var(--card);
  transition:all 0.25s;
}}
.dim-pill.active{{
  border-color:var(--orange-border);
  color:var(--orange);
  background:var(--orange-dim);
}}
.dim-pill.done{{
  border-color:var(--border-2);
  color:var(--border);
  background:transparent;
  text-decoration:line-through;
}}
.q-card{{
  background:var(--card);
  border:1px solid var(--border);
  border-radius:20px;
  padding:1.5rem;
  box-shadow:var(--shadow);
  transition:opacity 0.3s,transform 0.3s;
}}
@media(min-width:640px){{.q-card{{padding:2rem}}}}
.q-dim-tag{{
  display:inline-flex;
  align-items:center;
  gap:6px;
  font-size:0.68rem;
  font-weight:700;
  text-transform:uppercase;
  letter-spacing:1.2px;
  color:var(--orange);
  margin-bottom:0.9rem;
}}
.q-dim-tag::before{{
  content:'';
  width:18px;height:2px;
  background:var(--orange);
  border-radius:2px;
}}
.q-text{{
  font-family:'Sora',sans-serif;
  font-size:clamp(1rem,3.5vw,1.2rem);
  font-weight:700;
  line-height:1.45;
  color:var(--text);
  margin-bottom:1.5rem;
}}
.opts-list{{
  display:flex;
  flex-direction:column;
  gap:8px;
}}
.opt-btn{{
  background:#fafaf8;
  border:1.5px solid var(--border);
  border-radius:12px;
  padding:13px 16px;
  text-align:left;
  color:var(--text-2);
  font-family:'DM Sans',sans-serif;
  font-size:0.9rem;
  font-weight:400;
  cursor:pointer;
  transition:all 0.2s ease;
  display:flex;
  align-items:center;
  gap:12px;
  width:100%;
  -webkit-appearance:none;
  min-height:48px;
  line-height:1.4;
}}
.opt-btn:hover{{
  border-color:var(--orange-border);
  background:var(--orange-dim);
  transform:translateX(3px);
}}
.opt-btn:active{{
  transform:scale(0.99);
}}
.opt-btn.selected{{
  border-color:var(--orange);
  background:var(--orange-dim);
  transform:translateX(3px);
}}
.opt-letter{{
  width:28px;height:28px;
  border:1.5px solid var(--border);
  border-radius:50%;
  display:flex;align-items:center;justify-content:center;
  font-family:'Sora',sans-serif;
  font-size:0.72rem;
  font-weight:700;
  color:var(--muted);
  flex-shrink:0;
  transition:all 0.2s;
}}
.opt-btn:hover .opt-letter,
.opt-btn.selected .opt-letter{{
  border-color:var(--orange);
  color:var(--orange);
  background:rgba(255,91,0,0.1);
}}

/* ──────────────────── FORMULARIO ──────────────────── */
#form-screen{{display:none}}
#form-screen .card{{padding:1.75rem 1.5rem 2rem}}
@media(min-width:640px){{#form-screen .card{{padding:2.5rem 2.5rem 2rem}}}}
.form-badge{{
  display:inline-flex;
  align-items:center;
  gap:7px;
  font-family:'Sora',sans-serif;
  font-size:0.68rem;
  font-weight:700;
  text-transform:uppercase;
  letter-spacing:1.2px;
  color:var(--orange);
  background:var(--orange-dim);
  border:1px solid var(--orange-border);
  border-radius:50px;
  padding:5px 12px;
  margin-bottom:1rem;
}}
.form-title{{
  font-family:'Sora',sans-serif;
  font-size:clamp(1.3rem,5vw,1.8rem);
  font-weight:800;
  line-height:1.2;
  color:var(--text);
  margin-bottom:0.5rem;
}}
.form-subtitle{{
  font-size:0.88rem;
  color:#6b7280;
  line-height:1.5;
  margin-bottom:1.5rem;
}}
.form-fields{{
  display:flex;
  flex-direction:column;
  gap:12px;
}}
.form-row{{
  display:grid;
  grid-template-columns:1fr;
  gap:12px;
}}
@media(min-width:480px){{.form-row{{grid-template-columns:1fr 1fr}}}}
.field-group{{display:flex;flex-direction:column;gap:5px}}
.field-label{{
  font-family:'Sora',sans-serif;
  font-size:0.7rem;
  font-weight:700;
  text-transform:uppercase;
  letter-spacing:1px;
  color:#9ca3af;
}}
.field-input{{
  background:#f9f8f6;
  border:1.5px solid var(--border);
  border-radius:10px;
  padding:13px 14px;
  color:var(--text);
  font-family:'DM Sans',sans-serif;
  font-size:0.93rem;
  width:100%;
  outline:none;
  transition:all 0.2s;
  -webkit-appearance:none;
}}
.field-input:focus{{
  border-color:var(--orange);
  background:#fff;
  box-shadow:0 0 0 3px rgba(255,91,0,0.1);
}}
.field-input::placeholder{{color:#d1d5db}}
.form-error{{
  color:#dc2626;
  font-size:0.8rem;
  padding:8px 12px;
  background:#fef2f2;
  border:1px solid #fecaca;
  border-radius:8px;
  display:none;
  margin-top:4px;
}}
.saving-row{{
  display:flex;align-items:center;justify-content:center;
  gap:8px;font-size:0.78rem;color:var(--muted);
  margin-top:10px;display:none;
}}
.pulse-dot{{
  width:6px;height:6px;background:var(--orange);
  border-radius:50%;animation:pdot 1s ease-in-out infinite;
}}
@keyframes pdot{{0%,100%{{opacity:0.3;transform:scale(0.7)}}50%{{opacity:1;transform:scale(1.3)}}}}
.form-privacy{{
  text-align:center;
  font-size:0.72rem;
  color:var(--muted);
  margin-top:0.75rem;
  line-height:1.5;
}}

/* ──────────────────── RESULTADOS ──────────────────── */
#results-screen{{display:none}}
#results-screen .inner{{
  width:100%;
  max-width:560px;
  display:flex;
  flex-direction:column;
  gap:12px;
}}
.res-hero{{
  background:var(--card);
  border:1px solid var(--border);
  border-radius:20px;
  box-shadow:var(--shadow);
  padding:2rem 1.5rem;
  text-align:center;
  position:relative;
  overflow:hidden;
}}
.res-hero::before{{
  content:'';
  position:absolute;
  top:-80px;right:-80px;
  width:260px;height:260px;
  background:radial-gradient(circle,rgba(255,91,0,0.08),transparent 65%);
  pointer-events:none;
}}
.res-greeting{{
  font-family:'Sora',sans-serif;
  font-size:0.82rem;
  font-weight:600;
  color:var(--orange);
  margin-bottom:0.4rem;
}}
.res-label{{
  font-size:0.72rem;
  font-weight:600;
  text-transform:uppercase;
  letter-spacing:1.5px;
  color:var(--muted);
  margin-bottom:0.25rem;
}}
.score-num{{
  font-family:'Sora',sans-serif;
  font-size:clamp(5rem,18vw,8rem);
  font-weight:800;
  color:var(--orange);
  line-height:1;
  margin:0.2rem 0;
}}
.score-denom{{
  font-size:1rem;
  color:var(--muted);
  margin-bottom:1rem;
}}
.level-pill{{
  display:inline-block;
  padding:7px 20px;
  border-radius:50px;
  font-family:'Sora',sans-serif;
  font-size:0.82rem;
  font-weight:700;
  margin-bottom:1rem;
}}
.level-low{{background:#f0fdf4;border:1px solid #bbf7d0;color:#16a34a}}
.level-mid{{background:#fffbeb;border:1px solid #fde68a;color:#d97706}}
.level-high{{background:var(--orange-dim);border:1px solid var(--orange-border);color:var(--orange)}}
.res-msg{{
  font-size:0.9rem;
  color:#6b7280;
  line-height:1.65;
  max-width:420px;
  margin:0 auto;
}}
.res-msg strong{{color:var(--text);font-weight:600}}
.dim-grid{{
  display:grid;
  grid-template-columns:1fr 1fr;
  gap:10px;
}}
@media(max-width:400px){{.dim-grid{{grid-template-columns:1fr}}}}
.dim-card{{
  background:var(--card);
  border:1px solid var(--border);
  border-radius:14px;
  padding:1rem 1.1rem;
  box-shadow:0 1px 3px rgba(0,0,0,0.04);
}}
.dc-head{{display:flex;justify-content:space-between;align-items:center;margin-bottom:8px}}
.dc-name{{font-family:'Sora',sans-serif;font-size:0.7rem;font-weight:700;text-transform:uppercase;letter-spacing:0.5px;color:var(--muted)}}
.dc-pct{{font-family:'Sora',sans-serif;font-size:0.85rem;font-weight:800;color:var(--orange)}}
.dc-track{{height:4px;background:var(--border-2);border-radius:4px;overflow:hidden}}
.dc-fill{{height:100%;border-radius:4px;background:var(--orange);transition:width 1.2s cubic-bezier(0.4,0,0.2,1);width:0%}}
.cta-note{{
  background:#fff8f5;
  border:1px solid rgba(255,91,0,0.2);
  border-radius:14px;
  padding:1rem 1.2rem;
  text-align:center;
  font-size:0.82rem;
  color:#6b7280;
  line-height:1.55;
}}
.cta-note strong{{color:var(--text)}}
.btn-cta{{
  background:var(--orange);
  color:#fff;
  font-family:'Sora',sans-serif;
  font-weight:700;
  font-size:0.95rem;
  padding:16px;
  border:none;
  border-radius:14px;
  cursor:pointer;
  width:100%;
  letter-spacing:0.3px;
  transition:all 0.25s;
  -webkit-appearance:none;
}}
.btn-cta:hover{{background:#e05000;box-shadow:0 6px 24px rgba(255,91,0,0.3)}}
.btn-ghost{{
  background:transparent;
  border:1.5px solid var(--border);
  color:var(--muted);
  font-family:'DM Sans',sans-serif;
  font-size:0.85rem;
  padding:12px;
  border-radius:14px;
  cursor:pointer;
  width:100%;
  transition:all 0.2s;
  -webkit-appearance:none;
}}
.btn-ghost:hover{{border-color:#9ca3af;color:var(--text-2)}}

/* ── UTILITIES ── */
.fade-in{{animation:fadeIn 0.45s cubic-bezier(0.4,0,0.2,1) forwards}}
@keyframes fadeIn{{from{{opacity:0;transform:translateY(10px)}}to{{opacity:1;transform:translateY(0)}}}}
.sr-only{{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0,0,0,0)}}
</style>
</head>
<body>
<div id="app">
  <div class="bg-shape bg-shape-1"></div>
  <div class="bg-shape bg-shape-2"></div>

  <!-- ══════════════════════════════ INTRO ══════════════════════════════ -->
  <div class="screen" id="intro-screen">
    <div class="card card-lg" style="overflow:hidden">
      <!-- Hero image -->
      <div class="intro-image-wrap">
        <img src="https://res.cloudinary.com/dwcqgcl0m/image/upload/q_auto/f_auto/v1776720417/Labs_olcsss.png"
             alt="KrugerTech" loading="eager">
        <div class="intro-image-overlay"></div>
        <div class="intro-brand">
          <div class="intro-brand-dot">
            <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
              <rect x="2" y="2" width="10" height="10" rx="1.5" stroke="white" stroke-width="1.3"/>
              <rect x="4.5" y="4.5" width="5" height="5" rx="0.75" fill="rgba(255,255,255,0.35)"/>
              <circle cx="7" cy="7" r="1.2" fill="white"/>
            </svg>
          </div>
          <span class="intro-brand-name">KrugerTech Labs</span>
        </div>
      </div>
      <!-- Body -->
      <div class="intro-body">
        <div style="margin-top:1.25rem"></div>
        <div class="intro-tag">RPA Intelligence</div>
        <h1 class="hero" style="margin-top:0.6rem">
          Índice de Madurez de<br><span class="hero-accent">Automatización</span>
        </h1>
        <p class="intro-desc">
          Responde 4 preguntas y descubre en menos de 2 minutos dónde están los mayores cuellos de botella de tu operación y cuánto ROI hay disponible.
        </p>
        <div class="stats-strip">
          <div class="stat-cell">
            <div class="stat-n">4</div>
            <div class="stat-l">Preguntas</div>
          </div>
          <div class="stat-cell">
            <div class="stat-n">~1</div>
            <div class="stat-l">Minuto</div>
          </div>
          <div class="stat-cell">
            <div class="stat-n">4</div>
            <div class="stat-l">Dimensiones</div>
          </div>
        </div>
        <button class="btn-primary" onclick="startAssessment()">
          Iniciar diagnóstico
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
            <path d="M3 8h10M9 4l4 4-4 4" stroke="white" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </button>
        <p class="intro-disclaimer">Sin registro previo · Resultados inmediatos · 100% confidencial</p>
      </div>
    </div>
  </div>

  <!-- ══════════════════════════════ QUIZ ══════════════════════════════ -->
  <div class="screen" id="quiz-screen">
    <div class="inner">
      <div class="prog-header">
        <div class="prog-meta">
          <span class="prog-label">Diagnóstico de madurez</span>
          <span class="prog-counter" id="prog-text">1 / 4</span>
        </div>
        <div class="prog-track">
          <div class="prog-fill" id="prog-bar"></div>
        </div>
      </div>
      <div class="dim-pills" id="dim-pills"></div>
      <div class="q-card" id="q-card">
        <div class="q-dim-tag" id="q-cat"></div>
        <div class="q-text" id="q-text"></div>
        <div class="opts-list" id="q-opts"></div>
      </div>
    </div>
  </div>

  <!-- ══════════════════════════════ FORMULARIO ══════════════════════════════ -->
  <div class="screen" id="form-screen">
    <div class="card" style="padding:1.75rem 1.5rem 2rem;max-width:520px">
      <div class="form-badge">
        <svg width="12" height="12" viewBox="0 0 16 16" fill="none">
          <path d="M8 1l2 5h5l-4 3 1.5 5L8 11.5 3.5 14 5 9 1 6h5z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/>
        </svg>
        Diagnóstico completado
      </div>
      <h2 class="form-title">¿A quién enviamos tu <span class="hero-accent">Score</span>?</h2>
      <p class="form-subtitle">Completa tus datos para ver el análisis completo y recomendaciones personalizadas.</p>
      <div class="form-fields">
        <div class="field-group">
          <label class="field-label" for="f-nombre">Nombre completo</label>
          <input class="field-input" id="f-nombre" type="text" placeholder="Ej. María González" autocomplete="name">
        </div>
        <div class="form-row">
          <div class="field-group">
            <label class="field-label" for="f-celular">Celular / WhatsApp</label>
            <input class="field-input" id="f-celular" type="tel" placeholder="+593 99 999 9999" autocomplete="tel">
          </div>
          <div class="field-group">
            <label class="field-label" for="f-correo">Correo electrónico</label>
            <input class="field-input" id="f-correo" type="email" placeholder="tu@empresa.com" autocomplete="email">
          </div>
        </div>
        <div class="form-row">
          <div class="field-group">
            <label class="field-label" for="f-empresa">Empresa</label>
            <input class="field-input" id="f-empresa" type="text" placeholder="Nombre de tu empresa" autocomplete="organization">
          </div>
          <div class="field-group">
            <label class="field-label" for="f-cargo">Cargo</label>
            <input class="field-input" id="f-cargo" type="text" placeholder="Ej. Gerente de Ops" autocomplete="organization-title">
          </div>
        </div>
      </div>
      <div class="form-error" id="form-error">Por favor completa todos los campos correctamente.</div>
      <button class="btn-primary" id="submit-btn" style="margin-top:1.25rem" onclick="submitForm()">
        Ver mi Score de Madurez
        <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
          <path d="M3 8h10M9 4l4 4-4 4" stroke="white" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </button>
      <div class="saving-row" id="saving-ind">
        <div class="pulse-dot"></div>
        Guardando tu diagnóstico...
      </div>
      <p class="form-privacy">🔒 Tus datos no serán compartidos con terceros</p>
    </div>
  </div>

  <!-- ══════════════════════════════ RESULTADOS ══════════════════════════════ -->
  <div class="screen" id="results-screen">
    <div class="inner">
      <div class="res-hero">
        <div class="res-greeting" id="user-greeting"></div>
        <div class="res-label">Score de madurez RPA</div>
        <div class="score-num" id="score-display">0</div>
        <div class="score-denom">de 20 puntos posibles</div>
        <div class="level-pill" id="level-badge"></div>
        <p class="res-msg" id="result-msg"></p>
      </div>
      <div class="dim-grid" id="dim-grid"></div>
      <div class="cta-note">
        ✅ Tu diagnóstico fue guardado. <strong>Un especialista de KrugerTech</strong> se pondrá en contacto contigo con las oportunidades de automatización identificadas.
      </div>
      <button class="btn-cta" onclick="openContact()">Hablar con un especialista →</button>
      <button class="btn-ghost" onclick="restart()">↩ Reiniciar diagnóstico</button>
    </div>
  </div>
</div>

<script>
const APPS_URL = "{APPS_SCRIPT_URL}";

const DIMS = [
  {{name:"Dependencia manual",  qs:[0], max:5}},
  {{name:"Conocimiento crítico", qs:[1], max:5}},
  {{name:"Complejidad / volumen",qs:[2], max:5}},
  {{name:"Calidad y riesgo",    qs:[3], max:5}}
];

const QUESTIONS = [
  {{
    dim:0,
    cat:"Dependencia manual",
    q:"¿Cuántas veces tu equipo actúa como 'pegamento' copiando y pegando datos entre sistemas para que el proceso avance?",
    opts:[
      "Casi nunca, los sistemas están integrados",
      "Solo en un paso muy puntual",
      "Ocasionalmente en varios puntos",
      "Con alta frecuencia diaria",
      "Es la base del proceso (puente manual total)"
    ]
  }},
  {{
    dim:1,
    cat:"Conocimiento crítico",
    q:"Si la persona que domina este proceso no está mañana, ¿qué ocurre con la operación?",
    opts:[
      "Nada, el proceso es autónomo/documentado",
      "Avanza con lentitud pero sin riesgo",
      "Se vuelve difícil y propenso a errores",
      "Entra en riesgo crítico de cumplimiento",
      "El proceso se detiene por completo"
    ]
  }},
  {{
    dim:2,
    cat:"Complejidad y volumen",
    q:"¿Cuántas horas hombre al mes 'consume' esta tarea sumando a todos los involucrados?",
    opts:[
      "< 20 h (Bajo impacto)",
      "20–50 h",
      "50–100 h",
      "100–200 h",
      "> 200 h (Equivalente a +1 FTE dedicado)"
    ]
  }},
  {{
    dim:3,
    cat:"Calidad y riesgo",
    q:"¿Cuál es el impacto directo de un error de digitación o un retraso en este flujo?",
    opts:[
      "Ninguno, hay validaciones automáticas",
      "Molestia interna o retraso menor",
      "Re-trabajo considerable y pérdida de tiempo",
      "Impacto en ingresos o satisfacción del cliente",
      "Multas, pérdida de contratos o riesgo legal"
    ]
  }}
];

let idx=0, total=0, scores=[], userData={{}};

function startAssessment(){{
  const intro=document.getElementById('intro-screen');
  intro.style.opacity='0';
  intro.style.transform='scale(0.97)';
  intro.style.transition='all 0.35s ease';
  setTimeout(()=>{{
    intro.style.display='none';
    const quiz=document.getElementById('quiz-screen');
    quiz.style.display='flex';
    buildPills();
    renderQ();
  }},350);
}}

function buildPills(){{
  const el=document.getElementById('dim-pills');
  el.innerHTML=DIMS.map((d,i)=>`<span class="dim-pill" id="pill-${{i}}">${{d.name}}</span>`).join('');
}}

function renderQ(){{
  const cur=QUESTIONS[idx];
  document.getElementById('prog-text').textContent=`${{idx+1}} / ${{QUESTIONS.length}}`;
  document.getElementById('prog-bar').style.width=`${{(idx/QUESTIONS.length)*100}}%`;

  DIMS.forEach((d,di)=>{{
    const pill=document.getElementById('pill-'+di);
    if(!pill) return;
    if(d.qs.includes(idx)){{
      pill.className='dim-pill active';
    }} else if(d.qs.every(q=>q<idx)){{
      pill.className='dim-pill done';
    }} else {{
      pill.className='dim-pill';
    }}
  }});

  const card=document.getElementById('q-card');
  card.style.opacity='0';
  card.style.transform='translateY(6px)';

  setTimeout(()=>{{
    document.getElementById('q-cat').textContent=cur.cat;
    document.getElementById('q-text').textContent=cur.q;
    const opts=document.getElementById('q-opts');
    opts.innerHTML='';
    const letters=['A','B','C','D','E'];
    cur.opts.forEach((o,oi)=>{{
      const b=document.createElement('button');
      b.className='opt-btn';
      b.innerHTML=`<span class="opt-letter">${{letters[oi]}}</span><span>${{o}}</span>`;
      b.onclick=()=>pick(oi+1);
      opts.appendChild(b);
    }});
    card.style.transition='all 0.35s cubic-bezier(0.4,0,0.2,1)';
    card.style.opacity='1';
    card.style.transform='translateY(0)';
  }},180);
}}

function pick(pts){{
  scores.push({{dim:QUESTIONS[idx].dim, pts}});
  total+=pts; idx++;
  if(idx<QUESTIONS.length){{
    const card=document.getElementById('q-card');
    card.style.opacity='0';
    card.style.transform='translateY(-6px)';
    setTimeout(renderQ,180);
  }} else {{
    goToForm();
  }}
}}

function goToForm(){{
  const quiz=document.getElementById('quiz-screen');
  quiz.style.opacity='0';
  quiz.style.transition='opacity 0.35s';
  setTimeout(()=>{{
    quiz.style.display='none';
    const form=document.getElementById('form-screen');
    form.style.display='flex';
    form.classList.add('fade-in');
  }},350);
}}

function submitForm(){{
  const nombre  = document.getElementById('f-nombre').value.trim();
  const celular = document.getElementById('f-celular').value.trim();
  const correo  = document.getElementById('f-correo').value.trim();
  const empresa = document.getElementById('f-empresa').value.trim();
  const cargo   = document.getElementById('f-cargo').value.trim();
  const errEl   = document.getElementById('form-error');

  if(!nombre||!celular||!correo||!empresa||!cargo){{
    errEl.textContent='Por favor completa todos los campos.';
    errEl.style.display='block'; return;
  }}
  if(!/\S+@\S+\.\S+/.test(correo)){{
    errEl.textContent='Ingresa un correo electrónico válido.';
    errEl.style.display='block'; return;
  }}
  errEl.style.display='none';
  userData={{nombre,celular,correo,empresa,cargo}};

  const dimScores={{}};
  DIMS.forEach((_,di)=>{{dimScores[di]=0}});
  scores.forEach(s=>{{dimScores[s.dim]+=s.pts}});

  const payload={{
    timestamp:        new Date().toISOString(),
    nombre,celular,correo,empresa,cargo,
    score_total:      total,
    score_max:        20,
    score_pct:        Math.round((total/20)*100),
    nivel:            total>=15?'Alta dependencia manual':total>=9?'Punto de inflexión':'Procesos estructurados',
    dim_dependencia:  dimScores[0],
    dim_conocimiento: dimScores[1],
    dim_complejidad:  dimScores[2],
    dim_calidad:      dimScores[3],
    pct_dependencia:  Math.round((dimScores[0]/5)*100),
    pct_conocimiento: Math.round((dimScores[1]/5)*100),
    pct_complejidad:  Math.round((dimScores[2]/5)*100),
    pct_calidad:      Math.round((dimScores[3]/5)*100),
  }};

  const btn=document.getElementById('submit-btn');
  btn.disabled=true; btn.style.opacity='0.6';
  btn.innerHTML='Procesando... ⏳';
  document.getElementById('saving-ind').style.display='flex';

  fetch(APPS_URL,{{
    method:'POST', mode:'no-cors',
    headers:{{'Content-Type':'text/plain;charset=utf-8'}},
    body:JSON.stringify(payload)
  }}).catch(()=>{{}}).finally(()=>{{showResults()}});
}}

function showResults(){{
  const form=document.getElementById('form-screen');
  form.style.opacity='0'; form.style.transition='opacity 0.35s';
  setTimeout(()=>{{
    form.style.display='none';
    const res=document.getElementById('results-screen');
    res.style.display='flex'; res.classList.add('fade-in');

    const first=(userData.nombre||'').split(' ')[0];
    if(first) document.getElementById('user-greeting').textContent=`Hola ${{first}}, aquí está tu diagnóstico 👋`;

    animScore(total);

    const badge=document.getElementById('level-badge');
    const msg=document.getElementById('result-msg');
    if(total>=15){{
      badge.className='level-pill level-high'; badge.textContent='Alta dependencia manual';
      msg.innerHTML='Tus procesos tienen una <strong>oportunidad masiva de automatización</strong>. Reducir la carga manual liberará capacidad operativa y minimizará riesgos de forma significativa.';
    }} else if(total>=9){{
      badge.className='level-pill level-mid'; badge.textContent='Punto de inflexión';
      msg.innerHTML='Estás en un <strong>momento clave</strong>. Hay cuellos de botella claros donde la automatización generará ROI alto y rápido.';
    }} else {{
      badge.className='level-pill level-low'; badge.textContent='Procesos estructurados';
      msg.innerHTML='Tienes buenas bases. La <strong>optimización con IA avanzada</strong> te llevará al siguiente nivel de escalabilidad operativa.';
    }}
    buildDimGrid();
  }},350);
}}

function buildDimGrid(){{
  const dimScores={{}};
  DIMS.forEach((_,di)=>{{dimScores[di]=0}});
  scores.forEach(s=>{{dimScores[s.dim]+=s.pts}});
  const el=document.getElementById('dim-grid');
  el.innerHTML=DIMS.map((d,di)=>{{
    const pct=Math.round((dimScores[di]/d.max)*100);
    return `<div class="dim-card">
      <div class="dc-head">
        <span class="dc-name">${{d.name}}</span>
        <span class="dc-pct">${{pct}}%</span>
      </div>
      <div class="dc-track"><div class="dc-fill" data-target="${{pct}}"></div></div>
    </div>`;
  }}).join('');
  setTimeout(()=>{{
    document.querySelectorAll('.dc-fill').forEach(b=>{{b.style.width=b.dataset.target+'%'}});
  }},120);
}}

function animScore(target){{
  let cur=0; const dur=1400; const step=target/(dur/16);
  const el=document.getElementById('score-display');
  const t=setInterval(()=>{{
    cur+=step;
    if(cur>=target){{el.textContent=target;clearInterval(t)}}
    else el.textContent=Math.floor(cur);
  }},16);
}}

function openContact(){{
  window.open('mailto:contacto@krugertech.com?subject=Solicito%20asesoria%20RPA%20-%20Score%20'+total,'_blank');
}}

function restart(){{
  idx=0; total=0; scores=[]; userData={{}};
  ['results-screen','form-screen'].forEach(id=>{{
    const el=document.getElementById(id);
    el.style.display='none';
    el.classList.remove('fade-in');
  }});
  ['f-nombre','f-celular','f-correo','f-empresa','f-cargo'].forEach(id=>{{
    document.getElementById(id).value='';
  }});
  const btn=document.getElementById('submit-btn');
  btn.disabled=false; btn.style.opacity='1';
  btn.innerHTML='Ver mi Score de Madurez <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="white" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>';
  document.getElementById('saving-ind').style.display='none';
  document.getElementById('form-error').style.display='none';
  document.getElementById('prog-bar').style.width='0%';
  document.getElementById('intro-screen').style.cssText='';
  document.getElementById('quiz-screen').style.cssText='display:none';
}}
</script>
</body>
</html>
""".replace("{APPS_SCRIPT_URL}", APPS_SCRIPT_URL)

components.html(codigo_html, height=880, scrolling=True)
