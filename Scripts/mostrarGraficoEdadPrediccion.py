import pandas as pd
import matplotlib.pyplot as plt
from dumpPorEdad import filtrar_edad
from sklearn.linear_model import LinearRegression

def mostrarGraficoEdadPrediccion(edad: int):
	filtrar_edad(edad)

	df = pd.read_csv(f'../CSV_nuevas/edad_{edad}.csv')

	# Convertir la columna 'FECHA_DEFUNCION' a tipo datetime
	df['FECHA_DEFUNCION'] = pd.to_datetime(df['FECHA_DEFUNCION'], dayfirst=True)

	# Contar la cantidad de decesos para cada fecha
	# Se agrega la columna de manera temporal
	conteo_decesos = df['FECHA_DEFUNCION'].value_counts().sort_index().reset_index()
	conteo_decesos.columns = ['FECHA_DEFUNCION', 'CANTIDAD_DE_DECESOS']

	fechas_futuras = pd.date_range(df['FECHA_DEFUNCION'].max(), periods=365*3, freq='D')
	df_futuro = pd.DataFrame({'FECHA_DEFUNCION': fechas_futuras})

	# Entrenar un modelo de regresión lineal
	X_train = pd.to_numeric(conteo_decesos['FECHA_DEFUNCION']).values.reshape(-1, 1)
	y_train = conteo_decesos['CANTIDAD_DE_DECESOS'].values
	regression_model = LinearRegression().fit(X_train, y_train)

	# Predecir la cantidad de decesos para las fechas futuras
	X_future = pd.to_numeric(df_futuro['FECHA_DEFUNCION']).values.reshape(-1, 1)
	y_pred = regression_model.predict(X_future)

	# Crear el gráfico para la predicción
	plt.figure(figsize=(10, 6))
	plt.plot(conteo_decesos['FECHA_DEFUNCION'], conteo_decesos['CANTIDAD_DE_DECESOS'], marker='o', linestyle='-', label='Datos existentes')
	plt.plot(df_futuro['FECHA_DEFUNCION'], y_pred, linestyle='--', color='red', label='Predicción')
	plt.title(f'Predicción de Decesos para Edad {edad} en los Próximos 3 Años')
	plt.xlabel('Fecha de Defunción')
	plt.ylabel('Cantidad de Decesos')
	plt.legend()
	plt.grid(True)
	plt.show()
