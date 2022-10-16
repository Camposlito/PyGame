import numpy as np
import random

def rgb_to_hex(r, g, b):
    #Cria o valor hex usando {:X}, que converte o valor decimal em hexadecimal
    return ('{:X}{:X}{:X}').format(r, g, b)

#print(rgb_to_hex(51, 255, 189))

rgb = tuple(np.random.randint(256, size=3))
#print(rgb)
#print(rgb[1])
hex_ans = ('{:X}{:X}{:X}').format(rgb[0],rgb[1],rgb[2])
#print(hex_ans)
resp_cor = ["hex", "random_color_hex", "random"]
#resp_cor2 = random.shuffle(resp_cor)

print("a lista é " + str(resp_cor))
random.shuffle(resp_cor)
print("a outra lista é " + str(resp_cor))