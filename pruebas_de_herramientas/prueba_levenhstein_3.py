'''
Prueba con hamming
'''
import Levenshtein

input1 = "feria"
input2 = "fiera"

hamming = Levenshtein.hamming(input1, input2)

print(f"La distancia de hamming entre {input1} y {input2} es : {hamming}")