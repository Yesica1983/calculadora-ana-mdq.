import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA Y ESTILO NEÓN
st.set_page_config(page_title="Ana MDQ | Lab", page_icon="⚡")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    .stButton>button { 
        width: 100%; border-radius: 20px; 
        background: linear-gradient(45deg, #00f2fe 0%, #4facfe 100%);
        color: white; font-weight: bold; border: none;
        box-shadow: 0px 0px 15px #00f2fe;
    }
    .stTextInput>div>div>input { background-color: #111; color: #00f2fe; border: 1px solid #4facfe; }
    .stSelectbox>div>div>div { background-color: #111; color: white; }
    /* Estilo para el precio gigante */
    .precio-header {
        text-align: center;
        color: #00f2fe;
        font-size: 3rem !important;
        font-weight: bold;
        text-shadow: 0px 0px 20px #00f2fe;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- INICIALIZACIÓN DE ESTADOS ---
if "logueado" not in st.session_state:
    st.session_state["logueado"] = False
if "generado" not in st.session_state:
    st.session_state["generado"] = False

# --- PANTALLA DE LOGIN ---
if not st.session_state["logueado"]:
    st.title("🔐 Acceso Privado | Ana MDQ")
    st.write("Ingresá para gestionar tus presupuestos.")
    clave = st.text_input("Contraseña", type="password")
    
    if st.button("DESBLOQUEAR"):
        if clave == "ana2026":
            st.session_state["logueado"] = True
            st.session_state["generado"] = False 
            st.rerun()
        else:
            st.error("Clave incorrecta")
else:
    # --- APP PARA EL CLIENTE ---
    with st.sidebar:
        if st.button("CERRAR SESIÓN"):
            st.session_state["logueado"] = False
            st.session_state["generado"] = False
            st.rerun()

    st.title("⚡ Calculadora de Presupuestos")
    
    # --- LÓGICA DE CÁLCULO INSTANTÁNEO ---
    col1, col2 = st.columns(2)
    
    with col1:
        cliente = st.text_input("Nombre del Cliente", placeholder="Ej: Marcos")
        servicio = st.selectbox("Tipo de Servicio", ["Landing Page", "E-commerce", "Web Corporativa", "App Python"])
    
    with col2:
        paginas = st.slider("Cantidad de secciones", 1, 15, 1)
        descuento = st.toggle("¿Bonificación especial (10%)?")

    # Precios
    precios = {
        "Landing Page": 150000, 
        "E-commerce": 500000, 
        "Web Corporativa": 350000, 
        "App Python": 450000
    }
    
    precio_base = precios[servicio]
    total = precio_base + (paginas * 20000)
    if descuento: total = total * 0.9

    total_formateado = f"{total:,.0f}".replace(",", ".")

    # --- MOSTRAR PRECIO EN TIEMPO REAL ---
    st.markdown(f"<div class='precio-header'>TOTAL: ${total_formateado}</div>", unsafe_allow_html=True)
    st.markdown("---")

    # BOTÓN PARA GENERAR EFECTOS Y DESCARGA
    if st.button("🚀 CONFIRMAR Y PREPARAR DESCARGA"):
        st.session_state["generado"] = True
        st.balloons()
        st.snow()

    # Muestra la descarga solo si presionó el botón
    if st.session_state["generado"]:
        resumen = (f"PRESUPUESTO ANA MDQ\n"
                    f"Cliente: {cliente}\n"
                    f"Servicio: {servicio}\n"
                    f"Total: ${total_formateado}")
        
        st.download_button(
            label="📥 CLIC PARA DESCARGAR .TXT",
            data=resumen,
            file_name=f"Presupuesto_{cliente}.txt",
            mime="text/plain"
        )

    st.info("Desarrollado por Ana MDQ")
