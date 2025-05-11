import Levenshtein

input1 = "feria"
input2 = "fiera"

ratio = Levenshtein.ratio(input1, input2)

print(f'El radio de Levenhstein entre {input1} y {input2} es de : {ratio}')