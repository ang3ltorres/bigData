import os
import pandas as pd

def filtrar_edad(edad: int):
	# Lee el archivo CSV
	data_frame = pd.read_csv('CSV_base/DDAAxsom2022SE09.csv')

	# Filtra el DataFrame por la edad
	data_frame_filtrado = data_frame[data_frame['EDAD'] == edad]

	# Crear carpeta CSV_nuevas si no existe
	if not os.path.exists('CSV_nuevas'):
		os.makedirs('CSV_nuevas')

	# Guarda el DataFrame filtrado en un nuevo archivo CSV
	archivo_salida = f'CSV_nuevas/edad_{edad}.csv'
	data_frame_filtrado.to_csv(archivo_salida, index=False)

	# Mensaje de éxito
	print(f'Se ha creado el archivo "{archivo_salida}" con personas de {edad} años.')
