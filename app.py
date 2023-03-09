import pandas as pd
import streamlit as st
import logging

logging.basicConfig(
    level=logging.INFO,
    handlers=[
        logging.FileHandler("Despegar.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger()

#titulo
st.title("Comparador de Columnas")
#descripcion
st.write('Este script permite comparar columnas y ver sus coincidencias o valores unicos!')
st.write("")
st.write("")
st.write("")

# si se carga un archivo:
st.write("**Cargar archivo de Excel**")
archivo = st.file_uploader("Selecciona el archivo Excel", type="xlsx")
if archivo is not None:
    comparar = st.button("Comparar columnas")
    if comparar:
        dataframe = pd.read_excel(
            archivo,
            header=None,
            names=['A', 'B'],
            dtype={
                'A': str,
                'B': str
            }
        )

        # Comparacion
        elementos_A = set(dataframe['A'].to_list())
        elementos_B = set(dataframe['B'].to_list())
        ambos = set.intersection(
            elementos_A,
            elementos_B
        )
        solo_en_A = elementos_A - elementos_B
        solo_en_B = elementos_B - elementos_A
        dataframe_coinciden = pd.DataFrame(list(ambos), columns =['Coinciden'])
        dataframe_solo_A = pd.DataFrame(list(solo_en_A), columns =['Solo en A'])
        dataframe_solo_B = pd.DataFrame(list(solo_en_B), columns =['Solo en B'])

        # Mostrar las coincidencias o valores unicos
        col1, col2, col3 = st.columns(3)

        col1.write(dataframe_solo_A)
        col2.write(dataframe_solo_B)
        col3.write(dataframe_coinciden)

st.write("")
st.write("")

# si ingreso manualmente la informacion
st.write("**Ingresa los datos de forma manual**")
columna_A = st.text_area("Columna A")
columna_B = st.text_area("Columna B")
if st.button("Comparar"):
    
    lista_A = columna_A.split("\n")
    lista_B = columna_B.split("\n")
    dataframe = pd.DataFrame({'A': lista_A, 'B': lista_B})
    
    # Compararar
    elementos_A = set(dataframe['A'].to_list())
    elementos_B = set(dataframe['B'].to_list())
    ambos = set.intersection(elementos_A, elementos_B)
    solo_en_A = elementos_A - elementos_B
    solo_en_B = elementos_B - elementos_A
    dataframe_coinciden = pd.DataFrame(list(ambos), columns =['Coinciden'])
    dataframe_solo_A = pd.DataFrame(list(solo_en_A), columns =['Solo en A'])
    dataframe_solo_B = pd.DataFrame(list(solo_en_B), columns =['Solo en B'])

    # Mostrar las coincidencias o valores unicos
    col1, col2, col3 = st.columns(3)

    col1.write(dataframe_solo_A)
    col2.write(dataframe_solo_B)
    col3.write(dataframe_coinciden)