import numpy as np
import pygame
import random
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

def reiniciar_jogo():
    #FIXME: não sei pq não aparece a mensagem na tela ;-;
    global fim_de_jogo
    msg_reiniciar = fonte_menor.render("Pressione R para reiniciar", True, (255,255,255))
    #msg_reiniciar_rect = msg_reiniciar.get_rect(center = (400,400))
    janela.blit(msg_reiniciar, (0,0))
    fim_de_jogo = True

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

#Tamanho e estilo dos botões
botao_estilo = pygame.image.load("lib/botao.png")
botao_estilo = pygame.transform.scale(botao_estilo, (200, 100))

botao_estilo_acertou = pygame.image.load("lib/botao_certo.png")
botao_estilo_acertou = pygame.transform.scale(botao_estilo_acertou, (200, 100))

botao_estilo_errou = pygame.image.load("lib/botao_errado.png")
botao_estilo_errou = pygame.transform.scale(botao_estilo_errou, (200, 100))

botao1 = Botao(botao_estilo, 140, 300, "#" + resp_cor[0])
botao2 = Botao(botao_estilo, 400, 300, "#" + resp_cor[1])
botao3 = Botao(botao_estilo, 660, 300, "#" + resp_cor[2])

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
                botao1 = Botao(botao_estilo_acertou, 140, 300, "#" + resp_cor[0])
                botao2 = Botao(botao_estilo_errou, 400, 300, "#" + resp_cor[1])
                botao3 = Botao(botao_estilo_errou, 660, 300, "#" + resp_cor[2])
                reiniciar_jogo()
            elif botao2.checkForInput(pygame.mouse.get_pos()) == ("#" + hex_ans):
                print("acertou")
                botao2 = Botao(botao_estilo_acertou, 400, 300, "#" + resp_cor[1])
                botao1 = Botao(botao_estilo_errou, 140, 300, "#" + resp_cor[0])
                botao3 = Botao(botao_estilo_errou, 660, 300, "#" + resp_cor[2])
                reiniciar_jogo()
            elif botao3.checkForInput(pygame.mouse.get_pos()) == ("#" + hex_ans):
                print("acertou")
                botao3 = Botao(botao_estilo_acertou, 660, 300, "#" + resp_cor[2])
                botao2 = Botao(botao_estilo_errou, 400, 300, "#" + resp_cor[1])
                botao1 = Botao(botao_estilo_errou, 140, 300, "#" + resp_cor[0])
                reiniciar_jogo()
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
        botao_estilo = pygame.image.load("lib/botao.png")
        botao_estilo = pygame.transform.scale(botao_estilo, (200, 100))
        botao1 = Botao(botao_estilo, 140, 300, "#" + resp_cor[0])
        botao2 = Botao(botao_estilo, 400, 300, "#" + resp_cor[1])
        botao3 = Botao(botao_estilo, 660, 300, "#" + resp_cor[2])
        print(rgb_ans)
        print(hex_ans)
        fim_de_jogo = False
    
    #apaga o rastro do movimento da bolinha
    janela.fill((0,0,0))
    #atualiza os botões
    botao1.update()
    botao2.update()
    botao3.update()
    #cria a bolinha
    pygame.draw.circle(janela, rgb_ans, (x,y), 100)
    pygame.display.update()
        
pygame.quit()