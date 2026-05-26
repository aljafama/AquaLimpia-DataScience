import pandas as pd

def cargar_y_limpiar_datos(nombre_ruta):
#Carga el dataset y estandariza las fechas.    
    df = pd.read_csv(nombre_ruta)
    df['fecha_registro'] = pd.to_datetime(df['fecha_registro'])
    
#Rellenar o eliminar nulos si existiesen
    df = df.dropna()
    return df

def calcular_eficiencia(df):
    #Calcula la eficiencia de remoción de DBO.
    df['eficiencia_remocion_%'] = ((df['DBO_entrada_mg_L'] - df['DBO_salida_mg_L']) / df['DBO_entrada_mg_L']) * 100
    return df
