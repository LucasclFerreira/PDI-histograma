"""
   ==============================================================
   * UNIFAL = Universidade Federal de Alfenas
   * BACHARELADO EM CIENCIA DA COMPUTACAO.
   * Trabalho....: Imagem ASCII
   * Disciplina..: Processamento de Imagens
   * Professor...: Luiz Eduardo da Silva
   * Aluno.......: Lucas Costa Lima Ferreira
   * Data........: 20/04/2023
   ==============================================================
"""

# Comando para executar: python3 arte_ascii.py cao.pgm 100 30 "@$#*%o!=+;:~=,. "
#import matplotlib.pyplot as plt
import sys
import math

# lê o arquivo .pgm
def readPgm(name):
    file = open(name, 'r')
    assert file.readline() == 'P2\n'
    line = file.readline()
    while line[0] == '#':
        line = file.readline()
    
    (width, height) = [int(i) for i in line.split()]
    #print (width, height)
    depth = int(file.readline())
    assert depth <= 255
    #print(depth)

    img = []
    row = []
    j = 0
    for line in file:
        values = line.split()
        for val in values:
            row.append(int(val))
            j += 1
            if j >= width:
                img.append(row)
                j = 0
                row = []
    file.close()
    return img

# lendo imagem PGM
img = readPgm('cao.pgm')

# tamanho da imagem
num_col = len(img[0])
num_lin = len(img)

total_pixels = num_lin * num_col

histograma = [0 for i in range(256)]

for i in range(num_lin):
    for j in range(num_col):
        histograma[img[i][j]] += 1

print(histograma[0])