import pandas as pd
import matplotlib.pyplot as plt
from dumpPorEdad import filtrar_edad

def mostrarGraficoEdad(edad: int):
	filtrar_edad(edad)

	df = pd.read_csv(f'../CSV_nuevas/edad_{edad}.csv')

	# Convertir la columna 'FECHA_DEFUNCION' a tipo datetime
	df['FECHA_DEFUNCION'] = pd.to_datetime(df['FECHA_DEFUNCION'], dayfirst=True)

	# Contar la cantidad de decesos para cada fecha
	# Se agrega la columna de manera temporal
	conteo_decesos = df['FECHA_DEFUNCION'].value_counts().sort_index().reset_index()
	conteo_decesos.columns = ['FECHA_DEFUNCION', 'CANTIDAD_DE_DECESOS']

	# Crea el gráfico
	plt.figure(figsize=(10, 6))
	plt.plot(conteo_decesos['FECHA_DEFUNCION'], conteo_decesos['CANTIDAD_DE_DECESOS'], marker='o', linestyle='-')
	plt.title(f'Cantidad de Decesos para Edad {edad} a lo largo del Tiempo')
	plt.xlabel('Fecha de Defunción')
	plt.ylabel('Cantidad de Decesos')
	plt.grid(True)
	plt.show()
