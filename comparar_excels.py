import pandas as pd
import logging
import os

logging.basicConfig(
    level=logging.INFO,
    handlers=[
        logging.FileHandler("Despegar.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger()

files = []
DIRECTORIO = ''

archivos = [f for f in os.listdir('.') if os.path.isfile(f)]
for x in archivos:
    if x.endswith(".xlsx"):
        files.append(x)

i = 0
for file in files:
    i = i + 1
    dataframe = pd.read_excel(
        io=f'{DIRECTORIO}{file}',
        header=None,
        names=['A', 'B'],
        dtype={
            'A': str,
            'B': str
        }
    )
    """
    dataframe_coinciden = dataframe[dataframe['A'] == dataframe['B']]
    dataframe_solo_a = dataframe[dataframe['B'].isna()]
    dataframe_solo_a = dataframe_solo_a.fillna('')
    # dataframe_solo_a = dataframe_solo_a.drop(columns=['B'])
    dataframe_solo_b = dataframe[dataframe['A'].isna()]
    dataframe_solo_b = dataframe_solo_b.fillna('')
    # dataframe_solo_b = dataframe_solo_b.drop(columns=['A'])
    """
    elementos_A = set(dataframe['A'].to_list())
    elementos_B = set(dataframe['B'].to_list())
    ambos = set.intersection(
        elementos_A,
        elementos_B
    )
    solo_en_A = elementos_A - elementos_B
    solo_en_B = elementos_B - elementos_A
    dataframe_coinciden = pd.DataFrame(list(ambos), columns =['Cuentas'])
    dataframe_solo_A = pd.DataFrame(list(solo_en_A), columns =['Cuentas'])
    dataframe_solo_B = pd.DataFrame(list(solo_en_B), columns =['Cuentas'])
    dataframe_coinciden.rename( columns={'Unnamed: 0': 'Cuenta'}, inplace=True )

DIRECTORIO_SALIDA = f'salida/'

def salida():
        os.makedirs(DIRECTORIO_SALIDA, exist_ok=True)
        with pd.ExcelWriter(f'{DIRECTORIO_SALIDA}Resultado {i}.xlsx') as writer:
            dataframe_coinciden.to_excel(
                writer,
                sheet_name="Coincidencias",
                index=False
            )
            dataframe_solo_A.to_excel(
                writer,
                sheet_name="Sólo en A",
                index=False
            )
            dataframe_solo_B.to_excel(
                writer,
                sheet_name="Sólo en B",
                index=False
            )
