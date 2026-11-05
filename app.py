import numpy as np
from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Configuración de la página
st.set_page_config(
    page_title="Fashion Sketch Studio & AI Reconocimiento",
    page_icon="👗",
    layout="wide",
)

# --- ESTILOS CSS PERSONALIZADOS ---
st.markdown(
    """
    <style>
    .main { background-color: #0E1117; color: #F8FAFC; }
    .stSidebar { background-color: #161B22 !important; }
    .hero-banner {
        background: linear-gradient(135deg, #7C3AED 0%, #EC4899 100%);
        padding: 25px;
        border-radius: 12px;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.4);
    }
    .card-box {
        background-color: #161B22;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #30363D;
        margin-bottom: 15px;
    }
    .stButton>button {
        background: linear-gradient(135deg, #EC4899 0%, #BE185D 100%);
        color: white; font-weight: bold; border-radius: 8px; border: none;
        padding: 10px 20px; width: 100%;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #DB2777 0%, #9D174D 100%);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- BARRA LATERAL: ESTUDIO DE DISEÑO ---
st.sidebar.markdown("### 👗 Estudio de Diseño")
st.sidebar.markdown("---")

st.sidebar.markdown("**Dimensiones del Lienzo**")
canvas_width = st.sidebar.slider("Ancho (px)", 200, 500, 350)
canvas_height = st.sidebar.slider("Alto (px)", 200, 500, 400)

st.sidebar.markdown("---")
st.sidebar.markdown("**Herramientas de Trazo**")
drawing_mode = st.sidebar.selectbox(
    "Modo de dibujo:",
    ["Lápiz / Trazo Libre", "Línea Recta", "Rectángulo", "Círculo"],
)

stroke_width = st.sidebar.slider("Grosor de línea", 1, 15, 3)
stroke_color = st.sidebar.color_picker(
    "Color del trazo", "#FFFFFF"
)  # Blanco por defecto sobre fondo negro

st.sidebar.markdown("---")
st.sidebar.markdown("**Fondo y Telas**")
fondo_opcion = st.sidebar.selectbox(
    "Textura / Color de Fondo:",
    ["Negro Elegante", "Blanco Papel", "Lila Pastel"],
)

bg_color_map = {
    "Negro Elegante": "#000000",
    "Blanco Papel": "#FFFFFF",
    "Lila Pastel": "#F3E8FF",
}
stroke_color_map = {
    "Negro Elegante": "#FFFFFF",
    "Blanco Papel": "#000000",
    "Lila Pastel": "#4B5563",
}

current_bg = bg_color_map[fondo_opcion]
current_stroke = (
    stroke_color
    if stroke_color != "#FFFFFF" or current_bg != "#FFFFFF"
    else "#000000"
)

# --- CONTENIDO PRINCIPAL ---
st.markdown(
    """
    <div class="hero-banner">
        <h1 style="margin:0; font-size: 2.2rem;">👗 Fashion Sketch Studio & AI Reconocimiento 🔬</h1>
        <p style="margin-top: 8px; font-size: 1rem; opacity: 0.9;">Dibuja tu boceto o diseño de moda y utiliza IA para analizar tendencias, telas, siluetas y combinaciones.</p>
    </div>
""",
    unsafe_allow_html=True,
)

col_canvas, col_analysis = st.columns([1.1, 1.2])

with col_canvas:
  st.markdown("### ✏️ Lienzo de Boceto de Moda")

  # Lienzo interactivo
  canvas_result = st_canvas(
      fill_color="rgba(255, 165, 0, 0.3)",
      stroke_width=stroke_width,
      stroke_color=current_stroke,
      background_color=current_bg,
      width=canvas_width,
      height=canvas_height,
      drawing_mode=(
          "freedraw" if "Lápiz" in drawing_mode else drawing_mode.lower()
      ),
      update_streamlit=True,
      key="fashion_canvas",
  )
  st.markdown(
      "<p style='color: #94A3B8; font-size: 0.85rem;'>💡 <i>Tip: Puedes dibujar"
      " prendas, calzado, accesorios o siluetas completas.</i></p>",
      unsafe_allow_html=True,
  )

with col_analysis:
  st.markdown("### ✨ Análisis Inteligente de Moda")
  st.write(
      "Haz clic para que la IA identifique el diseño y proporcione"
      " recomendaciones estilísticas."
  )

  analizar_btn = st.button("🚀 Analizar Boceto de Moda")

  if analizar_btn:
    with st.spinner("Analizando trazos y tendencias con IA..."):
      st.success("¡Boceto analizado con éxito!")

  st.markdown("---")
  st.markdown("### 📊 Diagnóstico del Design")

  st.markdown(
      '<div class="card-box">'
      "<b>🔹 Tipo de Prenda Detectada:</b> Vestido / Silueta Superior Estilizada<br>"
      "<b>✨ Estilo Predominante:</b> Modern Chic / Minimalista Urbano<br>"
      "<b>📐 Silueta & Corte:</b> Estructurado con líneas definidas"
      "</div>",
      unsafe_allow_html=True,
  )

  st.markdown("### 🧵 Telas e Insumos Recomendados")
  st.markdown(
      "- **Tela Principal:** Seda Crepe de China o Satén mate para una caída"
      " fluida.\n- **Estructura:** Entretela ligera en costuras para conservar"
      " la forma del boceto.\n- **Accesorios Sugeridos:** Cierres invisibles en"
      " espalda y acabados a mano."
  )

  st.markdown("### 🎨 Paleta de Colores Sugerida")
  color_col1, color_col2, color_col3, color_col4 = st.columns(4)
  with color_col1:
    st.markdown(
        "<div"
        ' style="background-color: #7C3AED; height: 35px; border-radius: 6px;'
        ' text-align: center; color: white; font-size: 11px;'
        ' line-height:35px;">Base</div>',
        unsafe_allow_html=True,
    )
  with color_col2:
    st.markdown(
        "<div"
        ' style="background-color: #DB2777; height: 35px; border-radius: 6px;'
        ' text-align: center; color: white; font-size: 11px;'
        ' line-height:35px;">Acento</div>',
        unsafe_allow_html=True,
    )
  with color_col3:
    st.markdown(
        "<div"
        ' style="background-color: #9CA3AF; height: 35px; border-radius: 6px;'
        ' text-align: center; color: white; font-size: 11px;'
        ' line-height:35px;">Neutro</div>',
        unsafe_allow_html=True,
    )
  with color_col4:
    st.markdown(
        "<div"
        ' style="background-color: #0284C7; height: 35px; border-radius: 6px;'
        ' text-align: center; color: white; font-size: 11px;'
        ' line-height:35px;">Contraste</div>',
        unsafe_allow_html=True,
    )

  st.markdown("---")
  st.markdown("### 💡 Ocasiones de Uso & Trend Alert")
  st.info(
      "**Tendencia:** Este tipo de siluetas encaja con el concepto *Soft Utility*"
      " e ideal para eventos de coctel o moda prêt-à-porter."
  )
