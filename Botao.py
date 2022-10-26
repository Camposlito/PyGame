class Botao():
    def __init__(self, image, x, y, texto_input, janela, fonte):
        #Define a janela para o botão, sua imagem, texto e posição
        self.janela = janela
        self.image = image
        self.texto_input = texto_input
        self.x = x
        self.y = y
        #Centraliza a posição da imagem
        self.rect = self.image.get_rect(center=(self.x, self.y))
        #Define a fonte e a posição do texto no botão
        self.text = fonte.render(self.texto_input, True, "white")
        self.text_rect = self.text.get_rect(center=(self.x, self.y))

    def update(self):
        #'blita', ou imprime o botão com a imagem e o texto
        self.janela.blit(self.image, self.rect)
        self.janela.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        #Retorna o texto do botão quando o ele for selecionado na posição em que foi definido 
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return (self.texto_input)
        
    def mudar_estilo(self, image):
        #Recebe e imprime o botão com nova imagem
        self.image = image
        self.janela.blit(self.image, self.rect)
        
    def mudar_texto(self, texto_input, fonte):
        #Recebe e imprime o botão com novo texto e fonte
        self.fonte = fonte
        self.texto_input = texto_input
        self.text = fonte.render(self.texto_input, True, "white")
        self.janela.blit(self.text, self.text_rect)
        
    def reset(self, texto_input, fonte, image):
        #Recebe e imprime o botão com novo texto, fonte e imagem
        self.image = image
        self.fonte = fonte
        self.texto_input = texto_input
        self.text = fonte.render(self.texto_input, True, "white")
        self.janela.blit(self.text, self.text_rect)
        self.janela.blit(self.image, self.rect)