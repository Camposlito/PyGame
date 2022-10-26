import numpy as np
import pygame
import random
from Botao import Botao
pygame.init()
fim_de_jogo = False

#Tamanho e título da janela do jogo
janela = pygame.display.set_mode((800,800))
pygame.display.set_caption("Color Guess")

#Tamanho e fonte do texto dos botões
fonte = pygame.font.SysFont("cambria", 35)
fonte_menor = pygame.font.SysFont("cambria", 30)

#Função que retorna uma lista de uma cor RGB aleatória
def random_color_rgb():
    return tuple(np.random.randint(256, size=3))

#Função que transforma uma lista de uma cor RGB em uma cor Hexadecimal
def rgb_hex(r,g,b):
    return ('{:X}{:X}{:X}').format(r,g,b)

#Função que cria uma cor aleatória em Hexadecimal
def random_color_hex():
    rgb = random_color_rgb()
    return rgb_hex(rgb[0],rgb[1],rgb[2])
    
def msg_reiniciar():
    janela.blit(fonte_menor.render("Aperte R Para Reiniciar", True, "white"), (250,150))

#Posição e velocidade inicial da bolinha
x=400
y=500
velocidade=15

#Cores aleatórias
rgb_ans = random_color_rgb()
hex_ans = rgb_hex(rgb_ans[0],rgb_ans[1],rgb_ans[2])
resp_cor = [hex_ans, random_color_hex(), random_color_hex()]
random.shuffle(resp_cor)
print(rgb_ans)
print(hex_ans)

#Tamanho e estilo dos botões
botao_estilo = pygame.image.load("lib/botao.png")
botao_estilo = pygame.transform.scale(botao_estilo, (200, 100))

botao_estilo_acertou = pygame.image.load("lib/botao_certo.png")
botao_estilo_acertou = pygame.transform.scale(botao_estilo_acertou, (200, 100))

botao_estilo_errou = pygame.image.load("lib/botao_errado.png")
botao_estilo_errou = pygame.transform.scale(botao_estilo_errou, (200, 100))

botao1 = Botao(botao_estilo, 140, 300, "#" + resp_cor[0], janela, fonte)
botao2 = Botao(botao_estilo, 400, 300, "#" + resp_cor[1], janela, fonte)
botao3 = Botao(botao_estilo, 660, 300, "#" + resp_cor[2], janela, fonte)

janela_aberta = True
while janela_aberta :
    pygame.time.delay(50)
    
    #Analisa cada evento
    for event in pygame.event.get():
        #Clicar em fechar o jogo
        if event.type == pygame.QUIT:
            janela_aberta = False
        if fim_de_jogo == False:
        #Clicar em algum dos botões
            if event.type == pygame.MOUSEBUTTONDOWN:
                b1 = botao1.checkForInput(pygame.mouse.get_pos())
                b2 = botao2.checkForInput(pygame.mouse.get_pos())
                b3 = botao3.checkForInput(pygame.mouse.get_pos())
                if b1 != ("#" + hex_ans) and b1 == ("#" + resp_cor[0]):
                    botao1.mudar_estilo(botao_estilo_errou)
                    botao1.update()
                    print("errou")
                elif b1 == ("#" + hex_ans):
                    botao1.mudar_estilo(botao_estilo_acertou)
                    print("acertou")
                    fim_de_jogo = True
                elif b2 != ("#" + hex_ans) and b2 == ("#" + resp_cor[1]):
                    botao2.mudar_estilo(botao_estilo_errou)
                    botao2.update()
                    print("errou")
                elif b2 == ("#" + hex_ans):
                    botao2.mudar_estilo(botao_estilo_acertou)
                    print("acertou")
                    fim_de_jogo = True
                elif b3 != ("#" + hex_ans) and b3 == ("#" + resp_cor[2]):
                    botao3.mudar_estilo(botao_estilo_errou)
                    botao3.update()
                    print("errou")
                elif b3 == ("#" + hex_ans):
                    botao3.mudar_estilo(botao_estilo_acertou)
                    print("acertou")
                    fim_de_jogo = True
            
    #teclas de movimento
    comandos= pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y-=velocidade
    if comandos[pygame.K_DOWN]:
        y+=velocidade
    if comandos[pygame.K_LEFT]:
        x-=velocidade
    if comandos[pygame.K_RIGHT]:
        x+=velocidade
    
    #Reseta as configurações inciais quando apertar R e fim_de_jogo = True
    if comandos[pygame.K_r] and fim_de_jogo:
        #reposiciona a bolinha
        x=400
        y=500
        #redefine as cores aleatórias
        rgb_ans = random_color_rgb()
        hex_ans = rgb_hex(rgb_ans[0],rgb_ans[1],rgb_ans[2])
        resp_cor = [hex_ans, random_color_hex(), random_color_hex()]
        random.shuffle(resp_cor)
        #redefine os botões
        botao1.reset("#" + resp_cor[0], fonte, botao_estilo)
        botao2.reset("#" + resp_cor[1], fonte, botao_estilo)
        botao3.reset("#" + resp_cor[2], fonte, botao_estilo)
        print(rgb_ans)
        print(hex_ans)
        fim_de_jogo = False
    
    #apaga o rastro do movimento da bolinha
    janela.fill((0,0,0))
    #atualiza os botões
    botao1.update()
    botao2.update()
    botao3.update()
    if fim_de_jogo:
        msg_reiniciar()
    #cria a bolinha
    pygame.draw.circle(janela, rgb_ans, (x,y), 100)
    pygame.display.update()
        
pygame.quit()