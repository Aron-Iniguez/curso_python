'''
Archivo para funciones del buscador de palabras de frases celebres
'''
import csv

def lee_archivo_csv(archivo:str)->list:
    ''' Lee un archivo CSV y lo convierte en una lista de diccionarios '''
    with open(archivo, "r", encoding='utf8') as f:
        return [x for x in csv.DictReader(f)]

def busca_frases_con_palabra(lista:list, palabra:str)->list:
    ''' Busca frases que contengan una palabra específica '''
    palabra = palabra.lower()
    resultado = []
    for fila in lista:
        if palabra in fila['frase'].lower():
            resultado.append({'frase': fila['frase'], 'pelicula': fila['pelicula']})
    return resultado

if __name__ == '__main__':
    archivo_csv = 'frases.csv'
    lista_palabras = lee_archivo_csv(archivo_csv)
    resultado = busca_frases_con_palabra(lista_palabras, 'hace')
    for r in resultado:
        print(f"{r['frase']} ({r['pelicula']})")