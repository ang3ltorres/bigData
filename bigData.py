import pandas as pd

# df = pd.read_csv('CSV_base/DDAAxsom2022SE09.csv')
# print(df.head()) #imprime primaeras 5 filas
# print(df.head(10)) #imprime primeras 10 filas
# print(df.tail()) #imprime ultimas 5 filas


# menor_de_edad = df[(df['EDAD'] < 18)] #del archivo  busca las filas con edad menor a 18
# menor_hombre = df[(df['EDAD'] < 18) & (df['SEXO'] == 1)] #del archivo  busca las filas con edad menor a 18 y sexo masculino
# print(len(menor_de_edad))

# menor_de_edad.to_csv('CSV_nuevas/menor_de_edad.csv',index=False) #se crea un archivo con los datos filtrados

def leer_en_partes(): #leer en partes y no saturar la memoria
    counter=0
    result =pd.Series([], dtype='float64')

    for chunk in pd.read_csv('CSV_base/DDAAxsom2022SE09.csv', chunksize=1000): #lee cada 1000 elementos

        # results = pd.concat([result, chunk['EDAD'] < 18]) #concatena los resultados
        results = pd.concat([result, chunk[(chunk['EDAD'] < 18)]]) #concatena los resultados y regresa todo el registro
        counter+=1
        if counter == 5:
            break
    print(results)


def excel(nombre_hoja): #funcion para convertir excel a csv
    excel = pd.read_excel('CSV_base/Catalogos_Exceso_Mortalidad_2020.xlsx', sheet_name=nombre_hoja) #lee el archivo excel
    print(excel)
    excel.to_csv('CSV_nuevas/' + nombre_hoja + '.csv',index=False) #se crea un archivo con los datos filtrados

excel('CATALOGO SEXO')
# excel('CATALOGO ENTIDADES')
# excel('CATALOGO MUNICIPIOS')

leer_en_partes()