'''
Archivo para funciones del buscador de palabras de frases celebres
'''
import csv

def lee_archivo_csv(archivo:str)->list:
    ''' Lee un archivo CSV y lo convierte en una lista de diccionarios '''
    with open(archivo, "r", encoding='utf8') as f:
        return [x for x in csv.DictReader(f)]

def busca_frases_con_palabra(lista:list, palabra:str)->list:
    ''' Busca frases que contengan una palabra específica y la resalta en mayúsculas '''
    palabra_lower = palabra.lower()
    resultado = []
    for fila in lista:
        frase = fila['frase']
        palabras = frase.split()
        frase_resaltada = ' '.join([
            p.upper() if palabra_lower in p.lower() else p for p in palabras
        ])
        if palabra_lower in frase.lower():
            resultado.append({'frase': frase_resaltada, 'pelicula': fila['pelicula']})
    return resultado

if __name__ == '__main__':
    archivo_csv = 'frases.csv'
    lista_palabras = lee_archivo_csv(archivo_csv)
    palabra_buscada = 'hace'
    resultado = busca_frases_con_palabra(lista_palabras, palabra_buscada)
    for r in resultado:
        print(f"{r['frase']} ({r['pelicula']})")