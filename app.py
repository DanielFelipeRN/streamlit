import streamlit as st
import cv2
from PIL import Image

# Configuración de la página (Diseño corporativo ancho)
st.set_page_config(
    page_title="Control de Acceso - Recepción Financiera",
    page_icon="🏢",
    layout="wide"
)

# Título principal de la aplicación
st.title("🛡️ Sistema Automatizado de Control de Acceso - Recepción")
st.markdown("---")

# Distribución en dos columnas (Izquierda: Cámara | Derecha: Panel de Control/Acciones)
col_camara, col_panel = st.columns([1.2, 1.8])

with col_camara:
    st.subheader("🔴 Monitoreo en Vivo")
    # Espacio reservado para el feed de video de OpenCV o Streamlit WebRTC
    marco_video = st.empty()
    
    # Botón de control de emergencia o fallback manual
    if st.button("⚠️ Activar Modo Fallback (Registro Manual)", use_container_width=True):
        st.warning("Modo manual activado: Saltando reconocimiento facial.")

with col_panel:
    st.subheader("📋 Estado y Validación de Visita")
    
    # Estado simulado según la lógica de decisión:
    estado_actual = "zona_gris" # Opciones: 'nuevo', 'zona_gris', 'conococido'
    
    if estado_actual == "conococido":
        st.success("✅ **Persona Identificada con Éxito**")
        st.markdown("**Nombre:** Carlos Andrés Mendoza")
        st.markdown("**Empresa:** Proveedor Externo S.A.")
        st.markdown("**Historial:** 🟢 Sin incidentes reportados")
        if st.button("Registrar Entrada", type="primary", use_container_width=True):
            st.toast("¡Acceso registrado correctamente!")

    elif estado_actual == "zona_gris":
        st.warning("⚠️ **Coincidencia Ambigua (Zona Gris)**")
        st.info("El sistema detectó una similitud parcial. Por favor, confirme la identidad visualmente.")
        
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("✅ Confirmar Identidad", use_container_width=True):
                st.success("Identidad confirmada por recepcionista.")
        with col_btn2:
            if st.button("❌ Rechazar / Es Nuevo", use_container_width=True):
                st.info("Redirigiendo a registro de nuevo usuario...")

    elif estado_actual == "nuevo":
        st.info("➕ **Nuevo Visitante Detectado**")
        with st.form("form_nuevo_visitante"):
            st.markdown("Complete los datos para la captura guiada:")
            tipo_doc = st.selectbox("Tipo de Documento", ["CC", "CE", "PASAPORTE", "PPT"])
            num_doc = st.text_input("Número de Documento")
            nombre = st.text_input("Nombres y Apellidos")
            empresa = st.text_input("Empresa de Procedencia")
            consentimiento = st.checkbox("Autoriza el tratamiento de datos biométricos (Ley de Protección de Datos)")
            
            submit_registro = st.form_submit_button("Guardar y Registrar Ingreso", use_container_width=True)
            if submit_registro:
                if consentimiento:
                    st.success("¡Visitante registrado y acceso autorizado!")
                else:
                    st.error("Debe aceptar el consentimiento de datos para continuar.")
