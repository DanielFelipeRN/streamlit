import streamlit as st

# 1. Configuración de página expandida
st.set_page_config(
    page_title="Control de Acceso - Recepción Financiera",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. CSS para alinear y ajustar espacios sin scroll


# Título compacto superior
st.markdown("### 🏢 Control Automatizado de Acceso - Recepción Financiera")
st.markdown("<div style='margin-bottom: 5px;'></div>", unsafe_allow_html=True)

# Contenedor de columnas principales
col_camara, col_panel = st.columns([1.2, 1.8], gap="medium")

with col_camara:
    st.markdown("#### 🔴 Monitoreo en Vivo (Emeet S800)")
    
    # Cuadro de video con altura exacta para emparejar con el panel derecho
    st.markdown(
        """
        <div style='background-color: #0e1117; height: 380px; display: flex; align-items: center; justify-content: center; color: #777; border-radius: 6px; font-size: 16px; border: 1px solid #333;'>
            [ Feed de Video en Tiempo Real ]
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    st.markdown("<div style='margin-top: 5px;'></div>", unsafe_allow_html=True)
    if st.button("⚠️ Activar Modo Fallback (Registro Manual)", type="secondary", use_container_width=True):
        st.toast("Modo manual activado.", icon="⚠️")

with col_panel:
    st.markdown("#### 📋 Panel de Validación y Estado")
    
    # Selector de prueba para ver los estados
    estado_demo = st.radio(
        "Simular estado de la persona en puerta:",
        ["Zona Gris (Ambiguo)", "Persona Conocida", "Persona Nueva"],
        horizontal=True,
        label_visibility="collapsed"
    )
    
    st.markdown("<div style='margin-top: 2px;'></div>", unsafe_allow_html=True)

    # Contenedor dinámico ajustado exactamente a la altura del bloque izquierdo
    if "Zona Gris" in estado_demo:
        with st.container(border=True):
            st.warning("⚠️ **Coincidencia Ambigua (Zona Gris)**")
            st.write("Similitud parcial detectada. Valide la identidad visualmente.")
            
            col_b1, col_b2 = st.columns(2)
            with col_b1:
                if st.button("✅ Confirmar Ingreso", type="primary", use_container_width=True):
                    st.success("¡Identidad validada!")
            with col_b2:
                if st.button("❌ Rechazar", use_container_width=True):
                    st.error("Acceso denegado.")

    elif "Conocida" in estado_demo:
        with st.container(border=True):
            st.success("✅ **Acceso Automático Autorizado**")
            st.markdown("**Nombre:** Carlos Andrés Mendoza | **CC:** 1.098.xxx.xxx")
            st.markdown("**Empresa:** Consultores Financieros S.A.")
            st.info("ℹ️ **Historial:** Sin incidentes reportados.")
            if st.button("Registrar Salida / Finalizar Visita", use_container_width=True):
                st.toast("Salida registrada con éxito.")

    else:
        with st.container(border=True):
            st.markdown("➕ **Nuevo Visitante Detectado - Registro Rápido**")
            with st.form("form_rapido_nuevo"):
                f_col1, f_col2 = st.columns(2)
                with f_col1:
                    st.selectbox("Tipo Doc", ["CC", "CE", "PASAPORTE", "PPT"], key="td")
                    st.text_input("Nombres y Apellidos", key="nombre")
                with f_col2:
                    st.text_input("Nro Documento", key="doc")
                    st.text_input("Empresa", key="emp")
                
                st.checkbox("Autoriza el tratamiento de datos biométricos", key="cons")
                st.form_submit_button("Guardar y Autorizar Ingreso", use_container_width=True)
