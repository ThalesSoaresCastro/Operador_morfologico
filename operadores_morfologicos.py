#Thales de Castro Soares RA: 86958

import numpy as np
import cv2

def main():

    #img1 = cv2.imread('j.png')
    #img2 = cv2.imread('j_noise.png')
    #imgBinJotaNormal = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    #imgBinJotaRuido = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("Imagem Normal", img2)


    w_size = 3

########################################################################################
#   Primeira parte...
    #dilatacao e erosao
    #cv2.imshow('Dilatacao',dilatacao(imgBinJotaNormal, w_size))
    #cv2.imshow('Erosao',erosao(imgBinJotaNormal, w_size))

    #abertura e fechamento
    #cv2.imshow('Abertura', abertura(imgBinJotaRuido,w_size))
    #cv2.imshow('Fechamento', fechamento(imgBinJotaRuido,w_size))

########################################################################################
#   Segunda parte....
# #Retirar círculos pretos no interior dos círculos brancos na imagem circulos.png
# (sem modificar o tamanho dos círculos), utilizando operadores morfológicos;

    #img3 = cv2.imread('circulos.png')
    #imgBinCirculo = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('Circulo original', imgBinCirculo)

    #p1 = abertura((fechamento(imgBinCirculo, w_size)),w_size)
    #p2 = fechamento((dilatacao(p1, w_size)), w_size)
    #p3 = fechamento((dilatacao(p2, w_size)), w_size)

    #cv2.imshow('Resultado', p3)
########################################################################################
#   Terceira parte...
#Extrair o contorno do perfil na imagem perfil.png,
# utilizando operadores morfológicos.
    img4 = cv2.imread('perfil.png')
    imgBinPerfil = cv2.cvtColor(img4, cv2.COLOR_BGR2GRAY)

    p1 = abertura(imgBinPerfil, w_size)
    p2 = subtracao(imgBinPerfil, p1)

    cv2.imshow('Perfil Normal', img4)
    cv2.imshow('Contorno', p2)
########################################################################################
    cv2.waitKey(0)
    cv2.destroyAllWindows()
########################################################################################
################################### FUNCOES ############################################

def subtracao(z,h):

    g = np.copy(z)
    size = z.shape

    for i in range(size[0]):
        for j in range(size[1]):
            if(h[i][j] == 255):
                g[i][j] = 0
    return g

#atribuir o valor 1 a cada posicao da imagem que e sobreposta pelo elemento estruturante
#valor 1 = branco = 255 || valor 0 = preto = 0
def dilatacao(f, w_size):
    size = f.shape
    g = np.zeros((size[0], size[1]), dtype = 'uint8')

    for i in range(size[0]-w_size//2):
        for j in range(size[1]-w_size//2):
            if(f[i][j] > 0):
                for u in range(w_size):
                    for v in range(w_size):
                        g[i-(w_size//2)+u][j-(w_size//2)+v] = 255
    return g

def erosao(f, w_size):
    size = f.shape
    g = np.zeros((size[0], size[1]), dtype = 'uint8')
    sizeW = (w_size*w_size)
    aux = 0
    for i in range(size[0]-1):
        for j in range(size[1]-1):
            if(f[i][j] > 0):
                for u in range(w_size):
                    for v in range(w_size):
                        if(f[i-(w_size//2)+u][j-(w_size//2)+v] == 255):
                            aux+=1
                            #print(aux)
                if(aux == sizeW):
                  g[i][j] = 255
            aux = 0

    return g


def abertura(f, w_size):
    #primeira parte: erosao
    #segunda parte: dilatacao

    imgErosao = erosao(f,w_size)
    imgAbertura = dilatacao(imgErosao, w_size)

    return imgAbertura

def fechamento(f, w_size):
    #primeira parte: dilatacao
    #segunda parte: erosao
    imgP1 = dilatacao(f, w_size)
    imgFechamento= erosao(imgP1, w_size)

    return imgFechamento

#########################################################################################
if __name__ == "__main__":
    main()
