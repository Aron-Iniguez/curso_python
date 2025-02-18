'''
Programa principal del juego ahorcado
'''
import argparse
import string
import unicodedata
from random import choice
import funciones as fn

def main(archivo_texto:str, nombre_plantilla='plantilla'):
    '''
    Programa principal del juego ahorcado
    '''
    # cargamos las plantillas
    plantillas = fn.carga_plantillas(nombre_plantilla)
    # cargamos las oraciones
    oraciones = fn.carga_archivo_texto(archivo_texto)
    # obtenemos las palabras
    palabras = fn.obten_palabras(oraciones)
    o = 5 # 5 oportunidades de fallar
    p = choice(palabras) # elegimos una palabra al azar
    abcdario = {letra:letra for letra in string.ascii_lowercase}
    adivinadas = set()
    while o>0:
        fn.despliega_plantilla(plantillas, o)
        o = fn.adivina_letra(abcdario, p, adivinadas, o)
        if p == ''.join([letra if letra in adivinadas else '_' for letra in p]):
            print('Felicidades, adivinaste la palabra')
            break
    fn.despliega_plantilla(plantillas, o)
    print(f"la palabra era: {p}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Juego del ahorcado')
    parser.add_argument('-a', '--archivo', help='Archivo de texto con palabras a adivinar', default='./datos/pg15532.txt')
    args = parser.parse_args()
    archivo = args.archivo
    #archivo = './datos/pg15532.txt'
    main(archivo)