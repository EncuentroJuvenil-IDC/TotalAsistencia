#------------------------------------------------------------------
#Librerias
#------------------------------------------------------------------
import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection
#------------------------------------------------------------------
#Funciones
#------------------------------------------------------------------
def limpiar_y_leer(Libro,Hoja):
    try:
        st.cache_data.clear()
        conn = st.connection(Libro, type=GSheetsConnection)
        datosDeLibroHoja = conn.read(worksheet=Hoja)
        df = pd.DataFrame(datosDeLibroHoja)
        return df
    except:
        return
#------------------------------------------------------------------
#Principal
#------------------------------------------------------------------
if st.button("Revisar Asistencia", type="primary"):
    asistenciaQR = limpiar_y_leer("gsheets_asistencia","Asistencia")
    asistenciaManual = limpiar_y_leer("gsheets_asistenciaManual","RegistroAsistenciaManual")
    total = asistenciaQR["NombreCompleto"].count() + asistenciaManual["Nombre Completo"].count()
    with st.container(border=True):
        st.subheader(total)
        st.text("Total de asistencia")