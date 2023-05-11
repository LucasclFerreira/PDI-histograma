import plotly.express as px
import pandas as pd
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

# número total de pixels
total_pixels = num_lin * num_col

# vetor com o histograma nulo
histograma = [0 for i in range(256)]

# calculando o histograma para cada valor encontrado na imagem
for i in range(num_lin):
    for j in range(num_col):
        histograma[img[i][j]] += 1

print(len(histograma))

df = pd.DataFrame(histograma, columns=['frequencia'])


#fig = px.histogram(df)
#fig.show()



# calculando as probabilidades
probabilidades = [0 for i in range(256)]
for i in range(len(histograma)):
    probabilidades[i] = round((histograma[i] / total_pixels), 3)

probabilidades_acumuladas = [0 for i in range(256)]
probabilidades_acumuladas[0] = probabilidades[0]

for i in range(1, len(probabilidades)):
    probabilidades_acumuladas[i] = probabilidades_acumuladas[i - 1] + probabilidades[i]
    #print(probabilidades_acumuladas[i])

novos_valores = [0 for i in range(256)]

for i in range(len(probabilidades_acumuladas)):
    novos_valores[i] = round(probabilidades_acumuladas[i] * 255, 0)
    print(novos_valores[i])