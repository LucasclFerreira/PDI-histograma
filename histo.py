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

# cria uma matriz para alocar o valores de uma imagem
def imgAlloc(nl, nc):
    img = []
    for i in range(nl):
        lin = []
        for j in range(nc):
            lin.append(0)
        img.append(lin)
    return img

