import streamlit as st

# 1. Configuración de página expandida al 100%
st.set_page_config(
    page_title="Control de Acceso - Recepción Financiera",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. CSS Personalizado para eliminar scroll y ajustar a la pantalla completa
st.markdown("""
    <style>
        /* Ocultar elementos superiores de Streamlit para ganar espacio limpio */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Ajustar contenedor principal al 100% sin scroll vertical */
        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
            padding-left: 1.5rem;
            padding-right: 1.5rem;
            max-width: 100% !important;
            overflow: hidden;
        }
        
        /* Estilizar tarjetas contenedoras */
        div.stButton > button {
            width: 100%;
        }
    </style>
""", unsafe_allow_html=True)

# Título compacto superior
st.markdown("### 🏢 Control Automatizado de Acceso - Recepción Financiera")
st.markdown("---")

# Distribución de la pantalla completa (Izquierda: Cámara | Derecha: Registro Rápido / Estado)
col_camara, col_panel = st.columns([1.3, 1.7], gap="medium")

with col_camara:
    st.subheader("🔴 Monitoreo en Vivo (Cámara Emeet S800)")
    
    # Contenedor simulando el frame de video de la cámara
    with st.container(border=True):
        # Aquí iría el streaming de video estático o en vivo
        st.markdown(
            "<div style='background-color: #0e1117; height: 420px; display: flex; align-items: center; justify-content: center; color: #555; border-radius: 8px; font-size: 18px;'>[ Feed de Video en Tiempo Real ]</div>", 
            unsafe_allow_html=True
        )
    
    # Botón de respaldo (Fallback)
    if st.button("⚠️ Activar Modo Fallback (Registro Manual)", type="secondary"):
        st.toast("Modo manual activado por el operador.", icon="⚠️")

with col_panel:
    st.subheader("📋 Panel de Validación y Estado")
    
    # Simulación de estados para probar los pop-ups
    estado_demo = st.radio(
        "Simular estado de la persona en puerta (para pruebas de diseño):",
        ["Zona Gris (Ambiguo)", "Persona Conocida", "Persona Nueva"],
        horizontal=True
    )
    
    with st.container(border=True):
        if "Zona Gris" in estado_demo:
            st.warning("⚠️ **Alerta Activa: Coincidencia Ambigua (Zona Gris)**")
            st.write("El sistema detectó una similitud parcial del vector facial. Se requiere validación visual por parte del recepcionista.")
            
            col_b1, col_b2 = st.columns(2)
            with col_b1:
                if st.button("✅ Confirmar Ingreso", type="primary"):
                    st.success("¡Identidad validada manualmente! Acceso registrado.")
            with col_b2:
                if st.button("❌ Rechazar / Desconocido"):
                    st.error("Acceso denegado / Redirigiendo a nuevo registro.")

        elif "Conocida" in estado_demo:
            st.success("✅ **Acceso Automático Autorizado**")
            st.markdown("**Nombre:** Carlos Andrés Mendoza")
            st.markdown("**Documento:** CC 1.098.xxx.xxx")
            st.markdown("**Empresa:** Consultores Financieros S.A.")
            st.markdown("---")
            st.info("ℹ️ **Historial:** Sin incidentes reportados en visitas previas.")
            if st.button("Registrar Salida / Finalizar Visita"):
                st.toast("Salida registrada con éxito.")

        else:
            st.info("➕ **Nuevo Visitante Detectado**")
            with st.form("form_rapido_nuevo"):
                f_col1, f_col2 = st.columns(2)
                with f_col1:
                    st.selectbox("Tipo Doc", ["CC", "CE", "PASAPORTE", "PPT"], key="td")
                    st.text_input("Nombres y Apellidos", key="nombre")
                with f_col2:
                    st.text_input("Número de Documento", key="doc")
                    st.text_input("Empresa de Procedencia", key="emp")
                
                st.checkbox("Autoriza el tratamiento de datos biométricos (Consentimiento Ley)", key="cons")
                st.form_submit_button("Guardar y Autorizar Ingreso", use_container_width=True)
