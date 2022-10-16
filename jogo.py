import numpy as np
import pygame
import random
pygame.init()

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

#Tamanho e título da janela do jogo
janela = pygame.display.set_mode((800,800))
pygame.display.set_caption("Color Guess")

#Tamanho e fonte do texto dos botões
fonte = pygame.font.SysFont("cambria", 35)

class Botao():
    def __init__(self, image, x, y, texto_input):
        self.image = image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.texto_input = texto_input
        self.text = fonte.render(self.texto_input, True, "white")
        self.text_rect = self.text.get_rect(center=(self.x, self.y))

    def update(self):
        janela.blit(self.image, self.rect)
        janela.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return (self.texto_input)

#Tamanho e estilo do botão
botao_estilo = pygame.image.load("botao.png")
botao_estilo = pygame.transform.scale(botao_estilo, (200, 100))

botao1 =Botao(botao_estilo, 140, 300, "#" + resp_cor[0])
botao2 =Botao(botao_estilo, 400, 300, "#" + resp_cor[1])
botao3 =Botao(botao_estilo, 660, 300, "#" + resp_cor[2])

janela_aberta = True
while janela_aberta :
    pygame.time.delay(50)
    
    #Analisa cada evento
    for event in pygame.event.get():
        #Clicar em fechar o jogo
        if event.type == pygame.QUIT:
            janela_aberta = False
        #Clicar em algum dos botões
        if event.type == pygame.MOUSEBUTTONDOWN:
            if botao1.checkForInput(pygame.mouse.get_pos()) == ("#" + hex_ans):
                print("acertou")
            elif botao2.checkForInput(pygame.mouse.get_pos()) == ("#" + hex_ans):
                print("acertou")
            elif botao3.checkForInput(pygame.mouse.get_pos()) == ("#" + hex_ans):
                print("acertou")
            else:
                print("errou")
            
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
    
    #apaga o rastro do movimento da bolinha
    janela.fill((0,0,0))
    #atualiza os botões
    botao1.update()
    botao2.update()
    botao3.update()
    #cria a bolinha
    pygame.draw.circle(janela, rgb_ans, (x,y), 50)
    pygame.display.update()
        
pygame.quit()