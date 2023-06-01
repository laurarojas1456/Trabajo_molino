import random
from tkinter import *

import yaml

# ---------------------
# variables globales
# ---------------------
BASE = 460
ALTURA = 220
RADIO = 50

# funcion para modificar arco
def modificar_arco(angulo):
      c.itemconfig(arco, extent=angulo)

# --------------------
# ventana principal
# --------------------
ventana_principal = Tk()
ventana_principal.title("Trabajo molino")
ventana_principal.resizable(False, False)
ventana_principal.geometry("500x500")
ventana_principal.config(bg="white")

# frame de graficacion
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="green", width=480, height=240)
frame_graficacion.place(x=10,y=10)

# creacion canvas
c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=10,y=10)

# arco
arco = c.create_arc(BASE/2-RADIO,ALTURA/2-RADIO,BASE/2+RADIO,ALTURA/2+RADIO, start=0,extent=0, fill="blue")

'''# dibujar viento 
rect_1 = c.create_rectangle(BASE/2-70,ALTURA/2+60,BASE/2+90,ALTURA/2+40,fill="#00ffff", outline="red")

#dibujar poligonos
polig_1 = c.create_polygon(3*BASE/4-105,ALTURA/2-50,BASE/2-30,ALTURA/2+40,BASE/2+50,ALTURA/2+40, fill="#ffff00")'''

'''# Generar 100 circulos de 20 de radio, y color y posicion aleatoria, sin salirse del canvas
for i in range(30):
    # generar color aleatorio
    color = "#"
    for i in range(6):
            color = color + random.choice("0123456789ABCDEF")
    # generar valor de radio, x e y aleatorio
    radio = random.randint(5,25)
    x = random.randint(0, BASE-2*radio)
    y = random.randint(0,ALTURA-2*radio)
        
    # dibujamos el circulo
    circulo = c.create_oval(x,y,x+2*radio,y+2*radio, fill=color)'''

'''# agregar una imagen al canvas
img_nave = PhotoImage(file="nave2.png")
nave = c.create_image(BASE/2,ALTURA/2,image=img_nave)'''

# ---------------------
# frame de controles
# ---------------------
frame_controles = Frame(ventana_principal)
frame_controles.config(bg="green", width=480, height=230)
frame_controles.place(x=10,y=260)

#barra de deslizamientos
barra_deslizamiento = Scale(frame_controles, label="angulo", from_=0, to=360, orient="horizontal", length=460, tickinterval=45,
command=modificar_arco)
barra_deslizamiento.place(x=10,y=10)

# desplegar ventana
ventana_principal.mainloop()