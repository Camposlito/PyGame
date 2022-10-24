class Botao():
    def __init__(self, image, x, y, texto_input, janela, fonte):
        self.janela = janela
        self.image = image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.texto_input = texto_input
        self.text = fonte.render(self.texto_input, True, "white")
        self.text_rect = self.text.get_rect(center=(self.x, self.y))

    def update(self):
        self.janela.blit(self.image, self.rect)
        self.janela.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return (self.texto_input)
        
    def mudar_estilo(self, image):
        self.image = image
        self.janela.blit(self.image, self.rect)
        
    def mudar_texto(self, texto_input, fonte):
        self.fonte = fonte
        self.texto_input = texto_input
        self.text = fonte.render(self.texto_input, True, "white")
        self.janela.blit(self.text, self.text_rect)
        
    def reset(self, texto_input, fonte, image):
        self.image = image
        self.fonte = fonte
        self.texto_input = texto_input
        self.text = fonte.render(self.texto_input, True, "white")
        self.janela.blit(self.text, self.text_rect)
        self.janela.blit(self.image, self.rect)