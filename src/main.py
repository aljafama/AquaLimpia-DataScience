import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def procesar_datos_aqualimpia():
    # Cargar datos
        df = pd.read_csv()

    # Crear carpeta de salidas
        os.makedirs('outputs',exist_ok=True)

    # 1. Salida para Área de Operaciones
        cols_operaciones=['fecha_registro','planta','caudal_entrada_m3_d',
                          'DBO_entrada_mg_L','DBO_salida_mg_L','energia_aeracion_kWh',
                          'Iodos_generados_kg_d']
        df_operaciones=df[cols_operaciones]
        df_operaciones.to_csv('outputs/operaciones.csv',index=False)

    # 2. Salida para Área de Gestión Ambiental
        cols_ambiental = ['fecha_registro','planta','DBO_salida_mg_L','cumplimiento_norma']
        df_ambiental=df[cols_ambiental]
        df_ambiental.to_csv=('outputs/gestion_ambiental.csv',index=False)

    # 3. Dashboard Exploratorio (Visualizaciones)
        fig,axes=plt.subplot(2,2,figsize=(14,10))
        fig.suptitle('Dashboard Exploratorio - AquaLimpia S.A.',fontsize=16)

    #   Gáfico A: Cumplimiento por Planta
        sns.countplot(data=df,x='planta',hue='cumplimiento_norma', ax=axes[0,0],palette='Set2')
        axes[0,0].set_title('Cumplimiento Normativo de Planta')

    #   Gráfico B: DBO de Salida vs. Caudal
        sns.scatterplot(data=df,x='caudal_entrada_m3_d',y='DBO_salida_mg_L',hue='cumplimiento_norma',ax=axes[0,1])
        axes[0,1].set_title('Relación_Caudal Entrada vs DBO Salida')
        axes[0,1].axhline(40,color='red',linestyle='-') #Umbral teórica DBO

    #   Grafico C: Distribución de Energía en Aireación
        sns.boxplot(data=df,x='planta',y='energia_aeracion_kWh',ax=axes[1,0],palette='pastel')
        axes[1,0].set_title('Consumo de Energia en Aireación por Planta')

    #   Grafico D: Tendencia de DBO de Salida (Muestra aleatoria o serie temporal corta)
        df_sample=df.sort_values('fecha_registro').head(60)
        sns.lineplot(data=df_sample,x='fecha_regitro',y='DBO_salida_mg_L',hue='planta',ax=axes[1,1])

        axes[1,1].set_title('Tendencia Temporal de DBO de Salida')
        axes[1.1].tick_params(axis='x',rotation=45)
                              
        plt.tight_layout()
        plt.savefig('outputs/dashboard_exploratorio.png')
        plt.show()

    #   Ejecución
        if__name__=='__main__':
        procesar_datos_aqualimpia('dataset_set_A_aguas_residuales.xlsx - sheet1.csv')

                                  