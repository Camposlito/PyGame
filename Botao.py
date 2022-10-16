import pygame
class Botao():
    def __init__(self, imagem, x, y, texto_input):
        self.imagem = imagem
        self.x = x
        self.y = y
        self.rect = self.imagem.get_rect(center=(self.x, self.y))
        self.texto_input = texto_input
        self.text = pygame.font.SysFont("cambria", 35).render(self.texto_input, True, "white")
        