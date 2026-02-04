import streamlit as st
import time

# 1. ESTILO Y CONFIGURACIÓN
st.set_page_config(page_title="Ana MDQ | Lab", page_icon="⚡")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    .stButton>button { 
        width: 100%; border-radius: 15px; 
        background: linear-gradient(45deg, #00f2fe 0%, #4facfe 100%);
        color: white; font-weight: bold; height: 3.5em; border: none;
        box-shadow: 0px 0px 15px #4facfe;
    }
    input { background-color: #1a1a1a !important; color: #00f2fe !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. INTERFAZ
st.title("⚡ Ana MDQ | Soluciones")
st.write("Calculadora de presupuestos interactiva")

col1, col2 = st.columns(2)
with col1:
    cliente = st.text_input("Cliente", "Empresa X")
with col2:
    servicio = st.selectbox("Servicio", ["CV Web", "App Python", "E-commerce"])

precios = {"CV Web": 45000, "App Python": 95000, "E-commerce": 180000}
monto = precios[servicio]

paginas = st.slider("Secciones extra", 1, 10, 1)
total = monto + ((paginas - 1) * 5000)

desc = st.toggle("¿Bonificación Ana MDQ?")
if desc: total *= 0.85

st.markdown(f"<h1 style='text-align: center; color: #00f2fe;'>Total: ${total:,.2f}</h1>", unsafe_allow_html=True)

# 3. GENERAR ARCHIVO DE TEXTO
resumen = f"""
PRESUPUESTO DIGITAL - ANA MDQ
------------------------------
Cliente: {cliente}
Servicio: {servicio}
Páginas: {paginas}
Total Final: ${total:,.2f}
------------------------------
Gracias por confiar en tecnología Python.
"""

# 4. BOTONES FINALES
if st.button("CALCULAR"):
    barra = st.progress(0)
    for p in range(100):
        time.sleep(0.01)
        barra.progress(p + 1)
    st.snow()
    st.balloons()
    st.success("¡Cálculo finalizado!")

# Botón para descargar
st.download_button(
    label="📥 DESCARGAR PRESUPUESTO",
    data=resumen,
    file_name=f"Presupuesto_{cliente}.txt",
    mime="text/plain"
)