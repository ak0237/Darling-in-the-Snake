
## Imports

from operator import truediv
import pygame
from pygame.locals import *
from sys import exit
from random import randint


## Inicio

pygame.init()


## Musicas
pygame.mixer.music.set_volume(0.2)
musica_de_fundo = pygame.mixer.music.load('NTR.mp3')
pygame.mixer.music.play(-1)

som_colisao = pygame.mixer.Sound('DarinOhayo.wav')



## Posições
x_darin = randint(40, 600)
y_darin = randint(50, 430)

largura = 640
altura = 480

x = largura/2
y = altura/2

velocidade = 10

x_controle = velocidade
y_controle = 0



## Textos/Tela/Fps

pontos = 0

fonte = pygame.font.SysFont('arial', 20, True, True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo Foda')

relogio = pygame.time.Clock()

def aumenta_z2(lista_z2):
    for XeY in lista_z2:
        pygame.draw.rect(tela, (255,0,255), (XeY[0], XeY[1], 20, 20))

lista_z2 = []
comp_inicial = 5

## Loop do Jogo
while True:
    relogio.tick(30)
    tela.fill ((0,0,0))

    mensagem = f'Ohayos: {pontos}'
    texto_formatado = fonte.render(mensagem, False, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
       
    ## Movimentação
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0

       

    x += x_controle
    y += y_controle

    ## Criamento de Personagens
    z2 = pygame.draw.rect(tela, (255, 0, 255), (x, y, 20, 20))
    darin = pygame.draw.rect(tela, (0,0,255), (x_darin, y_darin, 20, 20))


    ## Colisão

    if z2.colliderect(darin):
        x_darin = randint(40, 600)
        y_darin = randint(50, 430)    
        pontos += 1 
        som_colisao.play()
        comp_inicial += 1
        
        


    
    lista_cabeca = []
    lista_cabeca.append(x)
    lista_cabeca.append(y)
    lista_z2.append(lista_cabeca)
    if len(lista_z2) > comp_inicial:
        del lista_z2[0]

    aumenta_z2(lista_z2)




    tela.blit(texto_formatado, (520, 20))
    pygame.display.update()