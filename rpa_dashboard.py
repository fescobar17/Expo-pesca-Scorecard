import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import time

# ────────────────────────── CONFIG ──────────────────────────
st.set_page_config(
    layout="wide",
    page_title="Dashboard · Madurez de Automatización",
    page_icon="📊",
)

SHEET_ID = "1yMGQE4HZzpn2UmaZxN3m9IjB6YJA4hZRV_-zmAf-oeo"
CSV_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv"

# Paleta (alineada al formulario)
ORANGE = "#ff5b00"
ORANGE_LIGHT = "#ff7a2e"
ORANGE_DIM = "rgba(255,91,0,0.08)"
ORANGE_MID = "rgba(255,91,0,0.15)"
BG = "#faf9f7"
CARD = "#ffffff"
TEXT = "#111827"
MUTED = "#9ca3af"
BORDER = "#e8e3dc"

LEVEL_COLORS = {
    "Procesos estructurados": "#16a34a",
    "Punto de inflexión": "#d97706",
    "Alta dependencia manual": ORANGE,
}

# ────────────────────────── ESTILOS GLOBALES ──────────────────────────
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    .stDeployButton {{display:none;}}

    [data-testid="stAppViewContainer"] {{
        background-color: {BG};
        font-family: 'DM Sans', sans-serif;
    }}
    [data-testid="stSidebar"] {{
        background-color: {CARD};
        border-right: 1px solid {BORDER};
    }}
    .block-container {{
        padding-top: 1.2rem !important;
        padding-bottom: 2rem !important;
        max-width: 1400px;
    }}
    h1, h2, h3, h4 {{
        font-family: 'Sora', sans-serif !important;
        color: {TEXT};
    }}

    /* Header banner */
    .dash-header {{
        background: {CARD};
        border: 1px solid {BORDER};
        border-radius: 20px;
        padding: 1.5rem 1.75rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.06), 0 4px 16px rgba(0,0,0,0.06);
        margin-bottom: 1.25rem;
        position: relative;
        overflow: hidden;
    }}
    .dash-header::before {{
        content:'';
        position:absolute;
        top:-100px; right:-100px;
        width:280px; height:280px;
        background: radial-gradient(circle, rgba(255,91,0,0.10), transparent 65%);
        pointer-events:none;
    }}
    .dash-tag {{
        display: inline-flex;
        align-items: center;
        gap: 6px;
        font-family: 'Sora', sans-serif;
        font-size: 0.7rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        color: {ORANGE};
        background: {ORANGE_DIM};
        border: 1px solid rgba(255,91,0,0.25);
        border-radius: 50px;
        padding: 5px 12px;
        margin-bottom: 0.75rem;
    }}
    .dash-tag::before {{
        content:'';
        width:6px;height:6px;
        background:{ORANGE};
        border-radius:50%;
    }}
    .dash-title {{
        font-family: 'Sora', sans-serif;
        font-size: clamp(1.6rem, 3vw, 2.2rem);
        font-weight: 800;
        color: {TEXT};
        margin: 0 0 0.35rem 0;
        line-height: 1.15;
    }}
    .dash-title .accent {{ color: {ORANGE}; }}
    .dash-sub {{
        font-size: 0.95rem;
        color: #6b7280;
        font-weight: 300;
        line-height: 1.55;
        max-width: 700px;
    }}
    .live-dot {{
        display: inline-flex;
        align-items: center;
        gap: 6px;
        font-family: 'Sora', sans-serif;
        font-size: 0.7rem;
        font-weight: 700;
        color: #16a34a;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-left: 8px;
    }}
    .live-dot::before {{
        content:'';
        width:8px;height:8px;
        background:#16a34a;
        border-radius:50%;
        animation: pulse 1.4s infinite;
    }}
    @keyframes pulse {{
        0%,100% {{opacity:0.4; transform:scale(0.8);}}
        50% {{opacity:1; transform:scale(1.2);}}
    }}

    /* KPI cards */
    .kpi-card {{
        background: {CARD};
        border: 1px solid {BORDER};
        border-radius: 16px;
        padding: 1.1rem 1.25rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        height: 100%;
        transition: all 0.25s ease;
    }}
    .kpi-card:hover {{
        border-color: rgba(255,91,0,0.25);
        box-shadow: 0 4px 20px rgba(255,91,0,0.10);
        transform: translateY(-2px);
    }}
    .kpi-label {{
        font-family: 'Sora', sans-serif;
        font-size: 0.68rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        color: {MUTED};
        margin-bottom: 0.4rem;
    }}
    .kpi-value {{
        font-family: 'Sora', sans-serif;
        font-size: 2rem;
        font-weight: 800;
        color: {TEXT};
        line-height: 1;
    }}
    .kpi-value.accent {{ color: {ORANGE}; }}
    .kpi-sub {{
        font-size: 0.78rem;
        color: {MUTED};
        margin-top: 0.4rem;
    }}

    /* Section card wrapper */
    .section-card {{
        background: {CARD};
        border: 1px solid {BORDER};
        border-radius: 18px;
        padding: 1.4rem 1.5rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        margin-bottom: 1rem;
    }}
    .section-title {{
        font-family: 'Sora', sans-serif;
        font-size: 1.05rem;
        font-weight: 700;
        color: {TEXT};
        margin: 0 0 0.25rem 0;
        display: flex;
        align-items: center;
        gap: 8px;
    }}
    .section-title::before {{
        content:'';
        width: 18px; height: 2px;
        background: {ORANGE};
        border-radius: 2px;
    }}
    .section-sub {{
        font-size: 0.82rem;
        color: {MUTED};
        margin-bottom: 1rem;
    }}

    /* Level pills */
    .lvl-pill {{
        display:inline-block;
        padding:5px 14px;
        border-radius:50px;
        font-family:'Sora',sans-serif;
        font-size:0.72rem;
        font-weight:700;
    }}
    .lvl-low {{background:#f0fdf4;border:1px solid #bbf7d0;color:#16a34a;}}
    .lvl-mid {{background:#fffbeb;border:1px solid #fde68a;color:#d97706;}}
    .lvl-high {{background:{ORANGE_DIM};border:1px solid rgba(255,91,0,0.25);color:{ORANGE};}}

    /* Tabla */
    .stDataFrame {{
        border: 1px solid {BORDER};
        border-radius: 12px;
        overflow: hidden;
    }}

    /* Sidebar */
    [data-testid="stSidebar"] .block-container {{
        padding-top: 2rem;
    }}
    .side-brand {{
        font-family: 'Sora', sans-serif;
        font-weight: 800;
        font-size: 1rem;
        color: {TEXT};
        display: flex;
        align-items: center;
        gap: 8px;
        margin-bottom: 1.2rem;
    }}
    .side-brand-dot {{
        width: 24px; height: 24px;
        background: {ORANGE};
        border-radius: 50%;
        display:flex; align-items:center; justify-content:center;
        color: white; font-size: 12px; font-weight: 800;
    }}
    .side-section {{
        font-family: 'Sora', sans-serif;
        font-size: 0.65rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        color: {MUTED};
        margin: 1rem 0 0.5rem 0;
    }}

    /* Empty state */
    .empty-state {{
        text-align:center;
        padding: 4rem 2rem;
        background: {CARD};
        border: 1px dashed {BORDER};
        border-radius: 18px;
    }}
    .empty-state h3 {{
        font-family:'Sora',sans-serif;
        color: {TEXT};
        margin-bottom: 0.5rem;
    }}
    .empty-state p {{
        color: {MUTED};
        font-size: 0.9rem;
    }}
</style>
""", unsafe_allow_html=True)


# ────────────────────────── CARGA DE DATOS ──────────────────────────
@st.cache_data(ttl=60, show_spinner=False)
def load_data():
    df = pd.read_csv(CSV_URL)
    df.columns = [c.strip() for c in df.columns]

    rename = {
        "Fecha y hora": "timestamp",
        "Nombre": "nombre",
        "Celular": "celular",
        "Correo": "correo",
        "Empresa": "empresa",
        "Cargo": "cargo",
        "Score Total": "score_total",
        "Score Máx": "score_max",
        "Score %": "score_pct",
        "Nivel": "nivel",
        "Dependencia manual (pts)": "dim_dependencia",
        "Conocimiento crítico (pts)": "dim_conocimiento",
        "Complejidad y volumen (pts)": "dim_complejidad",
        "Calidad y riesgo (pts)": "dim_calidad",
        "Dependencia manual (%)": "pct_dependencia",
        "Conocimiento crítico (%)": "pct_conocimiento",
        "Complejidad y volumen (%)": "pct_complejidad",
        "Calidad y riesgo (%)": "pct_calidad",
    }
    df = df.rename(columns=rename)

    num_cols = [
        "score_total", "score_max", "score_pct",
        "dim_dependencia", "dim_conocimiento", "dim_complejidad", "dim_calidad",
        "pct_dependencia", "pct_conocimiento", "pct_complejidad", "pct_calidad",
    ]
    for c in num_cols:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")

    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce", dayfirst=True)

    df = df.drop_duplicates(subset=["timestamp", "correo", "score_total"], keep="first")
    df = df.dropna(subset=["score_total"]).reset_index(drop=True)
    return df


# ────────────────────────── SIDEBAR ──────────────────────────
with st.sidebar:
    st.markdown(f"""
    <div class="side-brand">
        <div class="side-brand-dot">K</div>
        KrugerTech Labs
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="side-section">Controles</div>', unsafe_allow_html=True)

    auto_refresh = st.toggle("🔴 Auto-actualizar (60s)", value=True)
    if st.button("↻ Recargar ahora", use_container_width=True):
        st.cache_data.clear()
        st.rerun()

    st.markdown('<div class="side-section">Filtros</div>', unsafe_allow_html=True)

    # Cargar datos para poblar filtros
    try:
        df_raw = load_data()
    except Exception as e:
        st.error(f"No se pudo leer el sheet: {e}")
        st.stop()

    if df_raw.empty:
        nivel_filter = []
        empresa_filter = []
        date_range = None
    else:
        niveles_disponibles = sorted(df_raw["nivel"].dropna().unique().tolist())
        nivel_filter = st.multiselect(
            "Nivel de madurez",
            options=niveles_disponibles,
            default=niveles_disponibles,
        )

        empresas_disponibles = sorted(df_raw["empresa"].dropna().unique().tolist())
        empresa_filter = st.multiselect(
            "Empresa",
            options=empresas_disponibles,
            default=[],
            help="Vacío = todas",
        )

        if df_raw["timestamp"].notna().any():
            min_d = df_raw["timestamp"].min().date()
            max_d = df_raw["timestamp"].max().date()
            date_range = st.date_input(
                "Rango de fechas",
                value=(min_d, max_d),
                min_value=min_d,
                max_value=max_d,
            )
        else:
            date_range = None

    st.markdown('<div class="side-section">Acerca de</div>', unsafe_allow_html=True)
    st.markdown(
        f"""<div style='font-size:0.78rem;color:{MUTED};line-height:1.55;'>
        Dashboard en tiempo real del Índice de Madurez de Automatización.
        Los datos provienen directamente del formulario público y se actualizan automáticamente.
        </div>""",
        unsafe_allow_html=True,
    )


# ────────────────────────── APLICAR FILTROS ──────────────────────────
df = df_raw.copy()
if not df.empty:
    if nivel_filter:
        df = df[df["nivel"].isin(nivel_filter)]
    if empresa_filter:
        df = df[df["empresa"].isin(empresa_filter)]
    if date_range and isinstance(date_range, tuple) and len(date_range) == 2:
        start, end = date_range
        mask = (df["timestamp"].dt.date >= start) & (df["timestamp"].dt.date <= end)
        df = df[mask]


# ────────────────────────── HEADER ──────────────────────────
st.markdown(f"""
<div class="dash-header">
    <div class="dash-tag">RPA Intelligence Dashboard</div>
    <h1 class="dash-title">Madurez de <span class="accent">Automatización</span> en tiempo real
        <span class="live-dot">EN VIVO</span>
    </h1>
    <p class="dash-sub">
        Visualización agregada de los diagnósticos completados. Cada respuesta nueva
        que llega al formulario se refleja aquí automáticamente.
    </p>
</div>
""", unsafe_allow_html=True)


# ────────────────────────── EMPTY STATE ──────────────────────────
if df.empty:
    st.markdown(f"""
    <div class="empty-state">
        <h3>Aún no hay respuestas</h3>
        <p>Cuando se completen diagnósticos en el formulario, aparecerán aquí en tiempo real.</p>
    </div>
    """, unsafe_allow_html=True)
    st.stop()


# ────────────────────────── KPIs ──────────────────────────
total_resp = len(df)
score_avg = df["score_total"].mean()
score_pct_avg = df["score_pct"].mean()
n_alta = (df["nivel"] == "Alta dependencia manual").sum()
n_inflex = (df["nivel"] == "Punto de inflexión").sum()
n_estr = (df["nivel"] == "Procesos estructurados").sum()
pct_alta = (n_alta / total_resp * 100) if total_resp else 0
empresas_unicas = df["empresa"].nunique()

# Dimensión más crítica (mayor promedio de pts → mayor dolor)
dim_means = {
    "Dependencia manual": df["dim_dependencia"].mean(),
    "Conocimiento crítico": df["dim_conocimiento"].mean(),
    "Complejidad / volumen": df["dim_complejidad"].mean(),
    "Calidad y riesgo": df["dim_calidad"].mean(),
}
dim_critica = max(dim_means, key=dim_means.get)

k1, k2, k3, k4, k5 = st.columns(5)

with k1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Respuestas totales</div>
        <div class="kpi-value accent">{total_resp}</div>
        <div class="kpi-sub">{empresas_unicas} empresa{'s' if empresas_unicas != 1 else ''}</div>
    </div>
    """, unsafe_allow_html=True)

with k2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Score promedio</div>
        <div class="kpi-value">{score_avg:.1f}<span style="font-size:0.9rem;color:{MUTED};font-weight:400;"> / 20</span></div>
        <div class="kpi-sub">{score_pct_avg:.0f}% de madurez agregada</div>
    </div>
    """, unsafe_allow_html=True)

with k3:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Alta dependencia</div>
        <div class="kpi-value accent">{pct_alta:.0f}%</div>
        <div class="kpi-sub">{n_alta} de {total_resp} respuestas</div>
    </div>
    """, unsafe_allow_html=True)

with k4:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Punto de inflexión</div>
        <div class="kpi-value">{n_inflex}</div>
        <div class="kpi-sub">{(n_inflex/total_resp*100):.0f}% del total</div>
    </div>
    """, unsafe_allow_html=True)

with k5:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Dimensión más crítica</div>
        <div class="kpi-value" style="font-size:1.15rem;line-height:1.2;padding-top:0.4rem;">{dim_critica}</div>
        <div class="kpi-sub">Mayor dolor agregado</div>
    </div>
    """, unsafe_allow_html=True)


st.markdown("<div style='height:0.75rem;'></div>", unsafe_allow_html=True)

# ────────────────────────── RADAR + DISTRIBUCIÓN ──────────────────────────
col_radar, col_levels = st.columns([1.4, 1])

with col_radar:
    st.markdown(f"""
    <div class="section-card">
        <div class="section-title">Mapa de dolor agregado · Gráfico de red</div>
        <div class="section-sub">Promedio por dimensión sobre todas las respuestas. Mayor área = mayor oportunidad de automatización.</div>
    </div>
    """, unsafe_allow_html=True)

    categorias = ["Dependencia manual", "Conocimiento crítico", "Complejidad / volumen", "Calidad y riesgo"]
    valores_pct = [
        df["pct_dependencia"].mean(),
        df["pct_conocimiento"].mean(),
        df["pct_complejidad"].mean(),
        df["pct_calidad"].mean(),
    ]
    valores_pct_closed = valores_pct + [valores_pct[0]]
    categorias_closed = categorias + [categorias[0]]

    radar = go.Figure()

    # Capa promedio (relleno principal)
    radar.add_trace(go.Scatterpolar(
        r=valores_pct_closed,
        theta=categorias_closed,
        fill="toself",
        fillcolor="rgba(255,91,0,0.25)",
        line=dict(color=ORANGE, width=3),
        marker=dict(size=10, color=ORANGE, line=dict(color="white", width=2)),
        name="Promedio",
        hovertemplate="<b>%{theta}</b><br>%{r:.0f}% de dolor<extra></extra>",
    ))

    # Capa máxima (referencia)
    radar.add_trace(go.Scatterpolar(
        r=[100] * 5,
        theta=categorias_closed,
        line=dict(color="rgba(255,91,0,0.15)", width=1, dash="dot"),
        showlegend=False,
        hoverinfo="skip",
    ))

    # Capa máxima del dataset (peor caso)
    valores_max = [
        df["pct_dependencia"].max(),
        df["pct_conocimiento"].max(),
        df["pct_complejidad"].max(),
        df["pct_calidad"].max(),
    ]
    valores_max_closed = valores_max + [valores_max[0]]
    radar.add_trace(go.Scatterpolar(
        r=valores_max_closed,
        theta=categorias_closed,
        line=dict(color=ORANGE_LIGHT, width=1.5, dash="dash"),
        marker=dict(size=6, color=ORANGE_LIGHT),
        name="Peor caso observado",
        hovertemplate="<b>%{theta}</b><br>Peor: %{r:.0f}%<extra></extra>",
    ))

    radar.update_layout(
        polar=dict(
            bgcolor=BG,
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                showline=False,
                gridcolor="rgba(0,0,0,0.06)",
                tickfont=dict(family="DM Sans", size=10, color=MUTED),
                ticksuffix="%",
                tickvals=[20, 40, 60, 80, 100],
            ),
            angularaxis=dict(
                tickfont=dict(family="Sora", size=12, color=TEXT),
                gridcolor="rgba(0,0,0,0.08)",
                linecolor="rgba(0,0,0,0.1)",
            ),
        ),
        paper_bgcolor=CARD,
        plot_bgcolor=CARD,
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.15,
            xanchor="center",
            x=0.5,
            font=dict(family="DM Sans", size=11, color=TEXT),
        ),
        height=480,
        margin=dict(l=60, r=60, t=20, b=40),
    )

    st.plotly_chart(radar, use_container_width=True, config={"displayModeBar": False})

with col_levels:
    st.markdown(f"""
    <div class="section-card">
        <div class="section-title">Distribución por nivel</div>
        <div class="section-sub">Segmentación de las {total_resp} respuestas según madurez.</div>
    </div>
    """, unsafe_allow_html=True)

    nivel_counts = df["nivel"].value_counts().reindex(
        ["Procesos estructurados", "Punto de inflexión", "Alta dependencia manual"],
        fill_value=0,
    )

    donut = go.Figure(go.Pie(
        labels=nivel_counts.index.tolist(),
        values=nivel_counts.values.tolist(),
        hole=0.65,
        marker=dict(
            colors=[LEVEL_COLORS[l] for l in nivel_counts.index],
            line=dict(color=CARD, width=3),
        ),
        textinfo="percent",
        textfont=dict(family="Sora", size=13, color="white"),
        hovertemplate="<b>%{label}</b><br>%{value} respuestas<br>%{percent}<extra></extra>",
    ))

    donut.update_layout(
        paper_bgcolor=CARD,
        plot_bgcolor=CARD,
        showlegend=True,
        legend=dict(
            orientation="v",
            yanchor="middle",
            y=0.5,
            xanchor="left",
            x=1.05,
            font=dict(family="DM Sans", size=11, color=TEXT),
        ),
        height=320,
        margin=dict(l=10, r=10, t=10, b=10),
        annotations=[dict(
            text=f"<b style='font-family:Sora;font-size:1.6rem;color:{TEXT};'>{total_resp}</b><br>" +
                 f"<span style='font-family:DM Sans;font-size:0.7rem;color:{MUTED};letter-spacing:1px;'>RESPUESTAS</span>",
            x=0.5, y=0.5, font_size=16, showarrow=False,
        )],
    )

    st.plotly_chart(donut, use_container_width=True, config={"displayModeBar": False})

    # Mini KPI por nivel
    st.markdown(f"""
    <div style="display:flex;flex-direction:column;gap:6px;">
        <div style="display:flex;justify-content:space-between;align-items:center;padding:8px 12px;background:#f0fdf4;border:1px solid #bbf7d0;border-radius:10px;">
            <span style="font-family:Sora;font-weight:700;font-size:0.78rem;color:#16a34a;">Estructurados</span>
            <span style="font-family:Sora;font-weight:800;color:#16a34a;">{n_estr}</span>
        </div>
        <div style="display:flex;justify-content:space-between;align-items:center;padding:8px 12px;background:#fffbeb;border:1px solid #fde68a;border-radius:10px;">
            <span style="font-family:Sora;font-weight:700;font-size:0.78rem;color:#d97706;">Inflexión</span>
            <span style="font-family:Sora;font-weight:800;color:#d97706;">{n_inflex}</span>
        </div>
        <div style="display:flex;justify-content:space-between;align-items:center;padding:8px 12px;background:{ORANGE_DIM};border:1px solid rgba(255,91,0,0.25);border-radius:10px;">
            <span style="font-family:Sora;font-weight:700;font-size:0.78rem;color:{ORANGE};">Alta dependencia</span>
            <span style="font-family:Sora;font-weight:800;color:{ORANGE};">{n_alta}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)


st.markdown("<div style='height:0.75rem;'></div>", unsafe_allow_html=True)

# ────────────────────────── BARRAS DE DIMENSIONES + TIMELINE ──────────────────────────
col_bars, col_time = st.columns([1, 1])

with col_bars:
    st.markdown(f"""
    <div class="section-card">
        <div class="section-title">Dolor por dimensión</div>
        <div class="section-sub">Promedio de cada dimensión (0–100%). Más alto = mayor cuello de botella.</div>
    </div>
    """, unsafe_allow_html=True)

    dim_df = pd.DataFrame({
        "Dimensión": categorias,
        "Promedio": valores_pct,
    }).sort_values("Promedio", ascending=True)

    bars = go.Figure(go.Bar(
        x=dim_df["Promedio"],
        y=dim_df["Dimensión"],
        orientation="h",
        marker=dict(
            color=dim_df["Promedio"],
            colorscale=[[0, "#fde6d6"], [0.5, ORANGE_LIGHT], [1, ORANGE]],
            line=dict(color=ORANGE, width=0),
        ),
        text=[f"{v:.0f}%" for v in dim_df["Promedio"]],
        textposition="outside",
        textfont=dict(family="Sora", size=12, color=TEXT, weight=700),
        hovertemplate="<b>%{y}</b><br>%{x:.1f}%<extra></extra>",
    ))

    bars.update_layout(
        paper_bgcolor=CARD,
        plot_bgcolor=CARD,
        height=340,
        margin=dict(l=20, r=60, t=10, b=30),
        xaxis=dict(
            range=[0, 110],
            showgrid=True,
            gridcolor="rgba(0,0,0,0.05)",
            tickfont=dict(family="DM Sans", size=10, color=MUTED),
            ticksuffix="%",
        ),
        yaxis=dict(
            tickfont=dict(family="Sora", size=11, color=TEXT),
        ),
        showlegend=False,
    )

    st.plotly_chart(bars, use_container_width=True, config={"displayModeBar": False})

with col_time:
    st.markdown(f"""
    <div class="section-card">
        <div class="section-title">Tendencia de respuestas</div>
        <div class="section-sub">Volumen de diagnósticos completados a lo largo del tiempo.</div>
    </div>
    """, unsafe_allow_html=True)

    df_time = df.dropna(subset=["timestamp"]).copy()

    if not df_time.empty:
        df_time["fecha"] = df_time["timestamp"].dt.date
        daily = df_time.groupby("fecha").agg(
            respuestas=("score_total", "count"),
            score_prom=("score_total", "mean"),
        ).reset_index()

        timeline = go.Figure()

        timeline.add_trace(go.Bar(
            x=daily["fecha"],
            y=daily["respuestas"],
            marker=dict(
                color=ORANGE,
                line=dict(color=ORANGE, width=0),
            ),
            opacity=0.85,
            name="Respuestas",
            hovertemplate="<b>%{x}</b><br>%{y} respuestas<extra></extra>",
            yaxis="y",
        ))

        timeline.add_trace(go.Scatter(
            x=daily["fecha"],
            y=daily["score_prom"],
            mode="lines+markers",
            line=dict(color="#111827", width=2.5, shape="spline"),
            marker=dict(size=8, color="#111827", line=dict(color="white", width=2)),
            name="Score promedio",
            yaxis="y2",
            hovertemplate="<b>%{x}</b><br>Score: %{y:.1f}<extra></extra>",
        ))

        timeline.update_layout(
            paper_bgcolor=CARD,
            plot_bgcolor=CARD,
            height=340,
            margin=dict(l=20, r=20, t=10, b=30),
            xaxis=dict(
                showgrid=False,
                tickfont=dict(family="DM Sans", size=10, color=MUTED),
            ),
            yaxis=dict(
                title=dict(text="Respuestas", font=dict(family="Sora", size=11, color=ORANGE)),
                showgrid=True,
                gridcolor="rgba(0,0,0,0.05)",
                tickfont=dict(family="DM Sans", size=10, color=MUTED),
            ),
            yaxis2=dict(
                title=dict(text="Score", font=dict(family="Sora", size=11, color=TEXT)),
                overlaying="y",
                side="right",
                range=[0, 20],
                showgrid=False,
                tickfont=dict(family="DM Sans", size=10, color=MUTED),
            ),
            legend=dict(
                orientation="h",
                yanchor="top",
                y=1.12,
                xanchor="right",
                x=1,
                font=dict(family="DM Sans", size=10, color=TEXT),
            ),
            hovermode="x unified",
        )

        st.plotly_chart(timeline, use_container_width=True, config={"displayModeBar": False})
    else:
        st.info("No hay datos con fecha para mostrar tendencia.")


st.markdown("<div style='height:0.75rem;'></div>", unsafe_allow_html=True)

# ────────────────────────── TOP EMPRESAS + DIST. SCORES ──────────────────────────
col_top, col_dist = st.columns([1, 1])

with col_top:
    st.markdown(f"""
    <div class="section-card">
        <div class="section-title">Top empresas evaluadas</div>
        <div class="section-sub">Por número de respuestas y score promedio.</div>
    </div>
    """, unsafe_allow_html=True)

    emp_df = df.groupby("empresa").agg(
        respuestas=("score_total", "count"),
        score_prom=("score_total", "mean"),
        pct_prom=("score_pct", "mean"),
    ).reset_index().sort_values("respuestas", ascending=False).head(10)

    if not emp_df.empty:
        emp_chart = go.Figure(go.Bar(
            x=emp_df["respuestas"],
            y=emp_df["empresa"],
            orientation="h",
            marker=dict(
                color=emp_df["pct_prom"],
                colorscale=[[0, "#16a34a"], [0.5, "#d97706"], [1, ORANGE]],
                cmin=0, cmax=100,
                colorbar=dict(
                    title=dict(text="% madurez", font=dict(family="Sora", size=10, color=MUTED)),
                    tickfont=dict(family="DM Sans", size=9, color=MUTED),
                    thickness=10,
                    len=0.7,
                ),
            ),
            text=[f"{r} resp · {p:.0f}%" for r, p in zip(emp_df["respuestas"], emp_df["pct_prom"])],
            textposition="outside",
            textfont=dict(family="DM Sans", size=10, color=TEXT),
            hovertemplate="<b>%{y}</b><br>Respuestas: %{x}<br>Score promedio: %{marker.color:.0f}%<extra></extra>",
        ))

        emp_chart.update_layout(
            paper_bgcolor=CARD,
            plot_bgcolor=CARD,
            height=max(280, 35 * len(emp_df) + 60),
            margin=dict(l=20, r=110, t=10, b=30),
            xaxis=dict(
                showgrid=True,
                gridcolor="rgba(0,0,0,0.05)",
                tickfont=dict(family="DM Sans", size=10, color=MUTED),
            ),
            yaxis=dict(
                tickfont=dict(family="DM Sans", size=11, color=TEXT),
                autorange="reversed",
            ),
        )
        st.plotly_chart(emp_chart, use_container_width=True, config={"displayModeBar": False})
    else:
        st.info("Sin datos de empresa.")

with col_dist:
    st.markdown(f"""
    <div class="section-card">
        <div class="section-title">Distribución de scores</div>
        <div class="section-sub">Cómo se reparten los puntajes (0–20). Cada barra es un rango.</div>
    </div>
    """, unsafe_allow_html=True)

    hist = go.Figure(go.Histogram(
        x=df["score_total"],
        xbins=dict(start=0, end=21, size=2),
        marker=dict(
            color=ORANGE,
            line=dict(color=CARD, width=2),
        ),
        opacity=0.9,
        hovertemplate="Rango: %{x}<br>Respuestas: %{y}<extra></extra>",
    ))

    hist.add_vline(
        x=score_avg,
        line=dict(color=TEXT, width=2, dash="dash"),
        annotation_text=f"Promedio: {score_avg:.1f}",
        annotation_position="top",
        annotation_font=dict(family="Sora", size=11, color=TEXT),
    )

    hist.update_layout(
        paper_bgcolor=CARD,
        plot_bgcolor=CARD,
        height=340,
        margin=dict(l=20, r=20, t=20, b=30),
        xaxis=dict(
            title=dict(text="Score (0–20)", font=dict(family="Sora", size=11, color=MUTED)),
            range=[0, 21],
            showgrid=False,
            tickfont=dict(family="DM Sans", size=10, color=MUTED),
        ),
        yaxis=dict(
            title=dict(text="Respuestas", font=dict(family="Sora", size=11, color=MUTED)),
            showgrid=True,
            gridcolor="rgba(0,0,0,0.05)",
            tickfont=dict(family="DM Sans", size=10, color=MUTED),
        ),
        bargap=0.15,
    )

    st.plotly_chart(hist, use_container_width=True, config={"displayModeBar": False})


st.markdown("<div style='height:0.75rem;'></div>", unsafe_allow_html=True)

# ────────────────────────── TABLA DE RESPUESTAS ──────────────────────────
st.markdown(f"""
<div class="section-card" style="padding-bottom:0.5rem;">
    <div class="section-title">Respuestas recientes</div>
    <div class="section-sub">Últimos diagnósticos completados. Se actualiza automáticamente.</div>
</div>
""", unsafe_allow_html=True)

table_df = df.sort_values("timestamp", ascending=False).head(50).copy()
table_df["timestamp"] = table_df["timestamp"].dt.strftime("%d/%m/%Y %H:%M")

display_df = table_df[[
    "timestamp", "nombre", "empresa", "cargo",
    "score_total", "score_pct", "nivel",
    "pct_dependencia", "pct_conocimiento", "pct_complejidad", "pct_calidad",
]].rename(columns={
    "timestamp": "Fecha",
    "nombre": "Nombre",
    "empresa": "Empresa",
    "cargo": "Cargo",
    "score_total": "Score",
    "score_pct": "%",
    "nivel": "Nivel",
    "pct_dependencia": "Dep. manual",
    "pct_conocimiento": "Conocimiento",
    "pct_complejidad": "Complejidad",
    "pct_calidad": "Calidad/Riesgo",
})

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True,
    height=min(400, 45 + 36 * len(display_df)),
    column_config={
        "Score": st.column_config.ProgressColumn(
            "Score", format="%d", min_value=0, max_value=20,
        ),
        "%": st.column_config.NumberColumn("%", format="%d%%"),
        "Dep. manual": st.column_config.ProgressColumn("Dep. manual", format="%d%%", min_value=0, max_value=100),
        "Conocimiento": st.column_config.ProgressColumn("Conocimiento", format="%d%%", min_value=0, max_value=100),
        "Complejidad": st.column_config.ProgressColumn("Complejidad", format="%d%%", min_value=0, max_value=100),
        "Calidad/Riesgo": st.column_config.ProgressColumn("Calidad/Riesgo", format="%d%%", min_value=0, max_value=100),
    },
)

# Descarga
csv_export = df.to_csv(index=False).encode("utf-8")
st.download_button(
    "⬇ Descargar CSV completo",
    data=csv_export,
    file_name=f"rpa_diagnosticos_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
    mime="text/csv",
)

# ────────────────────────── FOOTER ──────────────────────────
st.markdown(f"""
<div style="text-align:center;margin-top:2rem;padding:1rem;color:{MUTED};font-size:0.75rem;font-family:DM Sans;">
    KrugerTech Labs · RPA Intelligence · Última actualización: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
</div>
""", unsafe_allow_html=True)


# ────────────────────────── AUTO-REFRESH ──────────────────────────
if auto_refresh:
    time.sleep(60)
    st.cache_data.clear()
    st.rerun()
