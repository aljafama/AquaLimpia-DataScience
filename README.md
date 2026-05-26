
#  Análisis de Eficiencia - AquaLimpia S.A.

## Objetivos
- Analizar los patrones operativos que influyen en el incumplimiento de la norma DBO.
- Automatizar la entrega de datos limpios a las áreas de Operaciones y Gestión Ambiental.

## Proceso
1. **Recolección:** Uso del dataset `dataset_set_A_aguas_residuales.csv`.
2. **Procesamiento:** Script en Python que segmenta los datos de interés (Caudal, DBO, Energía, Lodos).
3. **Exploración:** Creación de dashboard usando Seaborn para evaluar el DBO de salida según el caudal y la planta.

## Resultados y Entregables
- `operaciones.csv`: Métricas de proceso y consumo.
- `gestion_ambiental.csv`: KPI de cumplimiento para reportes.
- `dashboard_exploratorio.png`: Visualización gráfica de anomalías operativas.
