# lista de listas = [[0,0,0,0,0,0],...]

from random import randint
import pickle

with open("code.pkl", "rb") as file:
    strings = pickle.load(file)

braille_lista = [[0,1,1,1,0,0], [1,0,0,0,0,0], [1,0,1,0,0,0], [1,1,0,0,0,0],
                [1,1,0,1,0,0], [1,0,0,1,0,0], [1,1,1,0,0,0], [1,1,1,1,0,0],
                [1,0,1,1,0,0], [0,1,1,0,0,0], [1,0,0,0,0,0], [1,0,1,0,0,0],
                [1,1,0,0,0,0], [1,1,0,1,0,0], [1,0,0,1,0,0], [1,1,1,0,0,0],
                [1,1,1,1,0,0], [1,0,1,1,0,0], [0,1,1,0,0,0], [0,1,1,1,0,0],
                [1,0,0,0,1,0], [1,0,1,0,1,0], [1,1,0,0,1,0], [1,1,0,1,1,0],
                [1,0,0,1,1,0], [1,1,1,0,1,0], [1,1,1,1,1,0], [1,0,1,1,1,0],
                [0,1,1,0,1,0], [0,1,1,1,1,0], [1,0,0,0,1,1], [1,0,1,0,1,1],
                [0,1,1,1,0,1], [1,1,0,0,1,1], [1,1,0,1,1,1], [1,0,0,1,1,1],
                [0,1,0,1,1,1], [0,1,0,1,0,1], [1,0,1,0,0,1], [0,1,0,1,1,0]]


braille_lista_txt = []

for elemento in braille_lista: 
    texto = ""
    for caracter in elemento:
        texto = texto + str(caracter)
    braille_lista_txt.append(texto)

dicionario_braille_numeros = {
    braille_lista_txt[0] : "0",
    braille_lista_txt[1] : "1",
    braille_lista_txt[2] : "2",
    braille_lista_txt[3] : "3",
    braille_lista_txt[4] : "4",
    braille_lista_txt[5] : "5",
    braille_lista_txt[6] : "6",
    braille_lista_txt[7] : "7",
    braille_lista_txt[8] : "8",
    braille_lista_txt[9] : "9"

}

dicionario_braille_pt = {
    braille_lista_txt[10] : "A",
    braille_lista_txt[11] : "B",
    braille_lista_txt[12] : "C",
    braille_lista_txt[13] : "D",
    braille_lista_txt[14] : "E",
    braille_lista_txt[15] : "F",
    braille_lista_txt[16] : "G",
    braille_lista_txt[17] : "H",
    braille_lista_txt[18] : "I",
    braille_lista_txt[19] : "J",
    braille_lista_txt[20] : "K",
    braille_lista_txt[21] : "L",
    braille_lista_txt[22] : "M",
    braille_lista_txt[23] : "N",
    braille_lista_txt[24] : "O",
    braille_lista_txt[25] : "P",
    braille_lista_txt[26] : "Q",
    braille_lista_txt[27] : "R",
    braille_lista_txt[28] : "S",
    braille_lista_txt[29] : "T",
    braille_lista_txt[30] : "U",
    braille_lista_txt[31] : "V",
    braille_lista_txt[32] : "W",
    braille_lista_txt[33] : "X",
    braille_lista_txt[34] : "Y",
    braille_lista_txt[35] : "Z",
    braille_lista_txt[36] : True,
}

passador = False
data = b""  # Guarda os dados binários que vão ser escritos no ficheiro
byte = 0    # Guarda o byte que vai ser adicionado a data
count = 0   # Usado para determinar se estamos a escrever a parte mais ou menos significativa do byte

for i in range(len(strings)):
    if passador == True:
        passador = False
        continue
    if (strings[i] in dicionario_braille_pt or strings[i] in dicionario_braille_numeros):
        if dicionario_braille_pt[strings[i]] == True and i < len(strings):
            half_char = int(dicionario_braille_numeros[strings[i+1]], 16)
            count += 1
            passador = True
        else:
            half_char = int(dicionario_braille_pt[strings[i]], 16)
            count += 1

        if count == 1:      # O half_char é a metade mais significativa
            byte += half_char << 4
        elif count == 2:    # O half_char é a metade menos significativa
            byte += half_char
            data += chr(byte).encode()  # Transformar em byte
            count = 0
            byte = 0

    elif strings[i] in dicionario_braille_pt and passador == True:
        passador = False
    else:
        print("\nNão está no dicionario. ", strings[i])

with open("data", "wb") as file:
    file.write(data)