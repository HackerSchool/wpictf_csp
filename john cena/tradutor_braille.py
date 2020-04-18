from random import randint
import pickle

import json
with open("braille.json", 'rb') as f:
    braille = json.load(f)

with open("code.pkl", "rb") as file:
    strings = pickle.load(file)

num_encontrado = False
data = b""  # Guarda os dados binários que vão ser escritos no ficheiro
byte = 0    # Guarda o byte que vai ser adicionado a data
count = 0   # Usado para determinar se estamos a escrever a parte mais ou menos significativa do byte

for i in range(len(strings)):
    try:
        if strings[i] in braille['numeros'] or strings[i] in braille['letras']:
            if num_encontrado:
                print(braille['numeros'][strings[i]], end="")
                half_char = int(braille['numeros'][strings[i]], 16)
                count += 1
                num_encontrado = False
            else:
                print(braille['letras'][strings[i]], end="")
                half_char = int(braille['letras'][strings[i]], 16)
                count += 1
            if count == 1:      # O half_char é a metade mais significativa
                byte += half_char << 4
            elif count == 2:    # O half_char é a metade menos significativa
                byte += half_char
                data += chr(byte).encode()  # Transformar em byte
                count = 0
                byte = 0
        elif strings[i] in braille:
            num_encontrado = True 
            continue
        else:
            print("\nNão foi encontrado conversão deste caracter: " + strings[i], end="")
    except:
        print("Erro no caracter: " + strings[i])

with open("data", "wb") as file:
    file.write(data)