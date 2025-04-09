#------------------------------------------------------------------
#Librerias
#------------------------------------------------------------------
import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection
#------------------------------------------------------------------
#Funciones
#------------------------------------------------------------------
def limpiar_leer_contar(Libro,Hoja,contar):
    try:
        st.cache_data.clear()
        conn = st.connection(Libro, type=GSheetsConnection)
        datosDeLibroHoja = conn.read(worksheet=Hoja)
        df = pd.DataFrame(datosDeLibroHoja)
        total = df[contar].count()
        return total
    except:
        return 0
#------------------------------------------------------------------
#Principal
#------------------------------------------------------------------
if st.button("Revisar Asistencia", type="primary"):
    asistenciaQR = limpiar_leer_contar("gsheets_asistencia","Asistencia","NombreCompleto")
    laptop1 = limpiar_leer_contar("gsheets_asistenciaManual_laptops","Registro_laptop1","Nombre Completo")
    laptop2 = limpiar_leer_contar("gsheets_asistenciaManual_laptops","Registro_laptop2","Nombre Completo")
    laptop3 = limpiar_leer_contar("gsheets_asistenciaManual_laptops","Registro_laptop3","Nombre Completo")
    laptop4 = limpiar_leer_contar("gsheets_asistenciaManual_laptops","Registro_laptop4","Nombre Completo")
    laptop5 = limpiar_leer_contar("gsheets_asistenciaManual_laptops","Registro_laptop5","Nombre Completo")
    total = asistenciaQR + laptop1 + laptop2 + laptop3 + laptop4 + laptop5
    with st.container(border=True):
        st.subheader(total)
        st.text("Total de asistencia")
    with st.container(border=True):
        st.text(f"Rgistros QR = {asistenciaQR}")
        st.text(f"Rgistros Laptop 1 = {laptop1}")
        st.text(f"Rgistros Laptop 2 = {laptop2}")
        st.text(f"Rgistros Laptop 3 = {laptop3}")
        st.text(f"Rgistros Laptop 4 = {laptop4}")
        st.text(f"Rgistros Laptop 5 = {laptop5}")