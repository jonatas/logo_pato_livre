from Tkinter import *

master = Tk()

w = Canvas(master, width=800, height=600)
w.pack()

width = 800
height = 600
horizontal_center = width  / 2
vertical_center = height / 2

def rounded_rectangle(x=0, y = 200,largura=200, tamanho = 400, cor="black"):
    if x == 0:
      x = horizontal_center - (largura / 2)
    circunferencia = int(tamanho / 2)
    raio = int(circunferencia/ 2)

    if (largura > tamanho):
      w.create_rectangle(x, y, x+largura, y+circunferencia, fill=cor)
      w.create_oval( x - raio, y, x + raio,y + circunferencia, fill=cor)
      w.create_oval( x + largura-raio, y, x + largura+raio, y + circunferencia, fill=cor)
    else:
      w.create_oval( x, y, x + circunferencia, y + circunferencia, fill=cor)

_y = 20
_tamanho = 40
rounded_rectangle(x=320,y=_y, largura=160, tamanho=_tamanho)
_y += 25
rounded_rectangle(x=320,y=_y, largura=240, tamanho=_tamanho)
_y += 25
rounded_rectangle(x=320,y=_y, largura=240, tamanho=_tamanho)
_y += 25
rounded_rectangle(y=_y, largura=80, tamanho=_tamanho)
_y += 25
rounded_rectangle(y=_y, largura=560, tamanho=_tamanho)
_y += 25
rounded_rectangle(y=_y, largura=640, tamanho=_tamanho)
_y += 25
pescoco = rounded_rectangle(y=_y, largura=720, tamanho=_tamanho)
_y += 25
rounded_rectangle(y=_y, largura=640, tamanho=_tamanho)
_y += 25
rounded_rectangle(y=_y, largura=560, tamanho=_tamanho)
_y += 25
rounded_rectangle(y=_y, largura=480, tamanho=_tamanho)
_y += 25
rounded_rectangle(y=_y, largura=400, tamanho=_tamanho)
_y += 25
rounded_rectangle(y=_y, largura=240, tamanho=_tamanho)
_y += 25
rounded_rectangle(y=_y, largura=320, tamanho=_tamanho)
_y += 25
rounded_rectangle(y=_y, largura=360, tamanho=_tamanho)
_y += 25

entre_pernas = 40

_largura = 32
direita_x = horizontal_center - (_largura/ 2)
rounded_rectangle(x = direita_x + entre_pernas, y=_y, largura=_largura, tamanho=_tamanho)
rounded_rectangle(x = direita_x - entre_pernas, y=_y, largura=_largura, tamanho=_tamanho)
_y += 25

_largura = 42 
direita_x = horizontal_center - (_largura/ 2)
rounded_rectangle(x = direita_x + entre_pernas, y=_y, largura=_largura, tamanho=_tamanho)
rounded_rectangle(x = direita_x - entre_pernas, y=_y, largura=_largura, tamanho=_tamanho)
_y += 25

_largura = 56
direita_x = horizontal_center - (_largura/ 2)
rounded_rectangle(x = direita_x + entre_pernas, y=_y, largura=_largura, tamanho=_tamanho) 
rounded_rectangle(x = direita_x - entre_pernas, y=_y, largura=_largura, tamanho=_tamanho)
_y += 25


mainloop()
