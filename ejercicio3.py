from tkinter import *
from tkinter import ttk
import tkinter as tk

# Crear la ventana principal
raiz = tk.Tk()
raiz.title("Interfaz gráfica con Tkinter")
raiz.configure(background="Black")

imagen1 = PhotoImage(file="encendido.png")
imagen2 = PhotoImage(file="apagado.png")
imagen3 = PhotoImage(file="temperatura1.png")
imagen4 = PhotoImage(file="temperatura2.png")
imagen5 = PhotoImage(file="grafica.png")
imagen6 = PhotoImage(file="bomba.png")
imagen7 = PhotoImage(file="niveldetanque.png")
imagen8 = PhotoImage(file="imagenboton.png")
#imagenes
'''
imagen2 = PhotoImage(file="bomba.png")
imagen3 = PhotoImage(file="encendido.png")
imagen4 = PhotoImage(file="grafica.png")
imagen5 = PhotoImage(file="imagen boton.png")
imagen6 = PhotoImage(file="niveldetanque.png")
imagen7 = PhotoImage(file="temperatura1.png")
imagen8 = PhotoImage(file="temp.png")'''


# Crear la barra azul en la parte superior
barraazul=Frame(raiz, height=40, bg="cyan4")
barraazul.grid(row=1, column=0, columnspan=5,rowspan=1, sticky="ew")
btnImagen12=Button(barraazul,borderwidth=0)
btnImagen12.grid(column=0,row=0)
btnImagen12['image'] = imagen8
barrablanca=Frame(raiz, height=40, bg="white")
barrablanca.grid(row=0, column=0, columnspan=5,rowspan=1, sticky="ew")




# Crear los cinco frames con grid

frame1=Frame(raiz, width=200, height=200, bg="gray20")
frame1.grid(row=2, column=0, padx=0, pady=2,sticky=NW)

frame2=Frame(raiz, width=200, height=200, bg="gray20")
frame2.grid(row=2, column=1, padx=0, pady=2,sticky=(NW))

frame3=Frame(raiz, width=200, height=200, bg="gray20")
frame3.grid(row=2, column=2, padx=1, pady=2,sticky=(NW))

frame4=Frame(raiz, width=200, height=200, bg="gray20")
frame4.grid(row=2, column=0, padx=0, pady=170,sticky=(N))

frame5=tk.Frame(raiz, width=200, height=200, bg="gray20")
frame5.grid(row=2, column=1, padx=0, pady=170,sticky=(SW))

'''boton y label barra azul'''
spai=Label(barraazul,text="SPAI 4.0",bg="cyan4",font=("arial",10),fg="white")
spai.grid(column=1,row=0,sticky=(W))



'''Texto frame1'''
titulo=Label(frame1,text="Indicadores digitales                                     ",bg="gray20",font=("Arial",12),fg="turquoise2")
titulo.grid(column=0,row=0)
linea1=Label(frame1,text="Linea 1:",bg="gray20",font=("Arial",8),fg="white")
linea1.grid(column=0,row=3,sticky=(W))
linea2=Label(frame1,text="Linea 2:",bg="gray20",font=("Arial",8),fg="white")
linea2.grid(column=0,row=5,sticky=(W))
lineauno=Label(frame1,text="Linea 1:",bg="gray20",font=("Arial",8),fg="white")
lineauno.grid(column=0,row=7,sticky=(W))
gabinete=Label(frame1,text="Gabinete:",bg="gray20",font=("Arial",8),fg="white")
gabinete.grid(column=0,row=9,sticky=(W))
alarma=Label(frame1,text="Alarma:",bg="gray20",font=("Arial",8),fg="white")
alarma.grid(column=0,row=11,sticky=(W))
alarma2=Label(frame1,text="Alarma2:",bg="gray20",font=("Arial",8),fg="white")
alarma2.grid(column=0,row=13,sticky=(W))
relleno=Label(frame1,text="",bg="gray20")
relleno.grid(column=0,row=14)
on1=Label(frame1,text="On",bg="gray20",font=("Arial",8),fg="white")
on1.grid(column=0,row=3)
on2=Label(frame1,text="On",bg="gray20",font=("Arial",8),fg="white")
on2.grid(column=0,row=5)
on3=Label(frame1,text="On",bg="gray20",font=("Arial",8),fg="white")
on3.grid(column=0,row=7)
abierto=Label(frame1,text="Abierto",bg="gray20",font=("Arial",8),fg="white")
abierto.grid(column=0,row=9)
on4=Label(frame1,text="On",bg="gray20",font=("Arial",8),fg="white")
on4.grid(column=0,row=11)
off=Label(frame1,text="Off",bg="gray20",font=("Arial",8),fg="white")
off.grid(column=0,row=13)

btnImagen=Label(frame1,borderwidth=(0))
btnImagen.grid(column=1,row=3,)
btnImagen['image'] = imagen1

btnImagen=Label(frame1,borderwidth=(0))
btnImagen.grid(column=1,row=5)
btnImagen['image'] = imagen1

btnImagen=Label(frame1,borderwidth=(0))
btnImagen.grid(column=1,row=7)
btnImagen['image'] = imagen1

btnImagen=Label(frame1,borderwidth=(0))
btnImagen.grid(column=1,row=9)
btnImagen['image'] = imagen2

btnImagen=Label(frame1,borderwidth=(0))
btnImagen.grid(column=1,row=11)
btnImagen['image'] = imagen2

btnImagen=Label(frame1,borderwidth=(0))
btnImagen.grid(column=1,row=13)
btnImagen['image'] = imagen1
'''texto temperaturas'''
titulotemperatura=Label(frame2,text="Temperaturas:",bg="gray20",font=("Arial",12),fg="turquoise2")
titulotemperatura.grid(column=0,row=0)
temperatura1=Label(frame2,text="Temperatura 1:",bg="gray20",font=("Arial",8),fg="white")
temperatura1.grid(column=0,row=1)
temperatura2=Label(frame2, text="Temperatura 2:                         ",bg="gray20",font=("Arial",8),fg="white")
temperatura2.grid(column=1,row=1,sticky=E)
tempagua=Label(frame2,text="Temp.Agua: 58°C",bg="gray20",font=("Arial",8),fg="white")
tempagua.grid(column=0,row=3, sticky=(E))
tempambiente=Label(frame2, text="Temp.Ambiente: 32",bg="gray20",font=("Arial",8),fg="white")
tempambiente.grid(column=1,row=5, sticky=(W))
'''extraambiente=Label(frame2, text="",bg="gray20",font=("Arial",8),fg="white")
extraambiente.grid(column=1,row=6, sticky=(W))'''

btnImagen=Label(frame2,borderwidth=(0))
btnImagen.grid(column=0,row=2)
btnImagen['image'] = imagen3

btnImagen=Label(frame2,borderwidth=(0))
btnImagen.grid(column=1,row=2)
btnImagen['image'] = imagen4

'''textoproduccion'''
tituloproduccion=Label(frame3,text="Produccion",bg="gray20",font=("Arial",12),fg="turquoise2")
tituloproduccion.grid(column=0,row=0)

piezasp=Label(frame3,text="Piezas producidas: 50",bg="gray20",font=("Arial",8),fg="white")
piezasp.grid(column=0,row=2)

piezasd=Label(frame3,text="Piezas defectuosas: 12",bg="gray20",font=("Arial",8),fg="white")
piezasd.grid(column=0,row=3)

btnImagen=Label(frame3,borderwidth=(0))
btnImagen.grid(column=0,row=1)
btnImagen['image'] = imagen5





'''texto bomba'''
bomba=Label(frame4,text="                                                                           ",bg="gray20",font=("Arial",12),fg="white")
bomba.grid(column=0,row=2)
bomba2=Label(frame4,text=" Velocidad bomba:  "                                             ,bg="gray20",font=("Arial",12),fg="white")
bomba2.grid(column=0,row=3, pady=0)
Relleno1=Label(frame4,text="",bg="gray20",font=("Arial",8),fg="white")
Relleno1.grid(column=0,row=4)


btnImagen=Label(frame4,borderwidth=(0))
btnImagen.grid(column=0,row=7)
btnImagen['image'] = imagen6


'''texto tanque'''
tanque=Label(frame5,text="Nivel de tanque                                        ",bg="gray20",font=("Arial",12),fg="turquoise2")
tanque.grid(column=0,row=0,pady=5)
btnImagen=Label(frame5,borderwidth=(0))
btnImagen.grid(column=0,row=1)
btnImagen['image'] = imagen7

'''imagenes'''
'''btnImagen=Label(grisFrame,borderwidth=(0))
btnImagen.grid(column=0,row=0,sticky=(W))
btnImagen['image'] = imagen1
btnImagen=Label(grisFrame,borderwidth=(0))
btnImagen.grid(column=0,row=0,sticky=(W))
btnImagen['image'] = imagen2
btnImagen=Label(grisFrame,borderwidth=(0))
btnImagen.grid(column=0,row=0,sticky=(W))
btnImagen['image'] = imagen3
btnImagen=Label(grisFrame,borderwidth=(0))
btnImagen.grid(column=0,row=0,sticky=(W))
btnImagen['image'] = imagen4
btnImagen=Label(grisFrame,borderwidth=(0))
btnImagen.grid(column=0,row=0,sticky=(W))
btnImagen['image'] = imagen5
btnImagen=Label(grisFrame,borderwidth=(0))
btnImagen.grid(column=0,row=0,sticky=(W))
btnImagen['image'] = imagen6
btnImagen=Label(grisFrame,borderwidth=(0))
btnImagen.grid(column=0,row=0,sticky=(W))
btnImagen['image'] = imagen7
btnImagen=Label(grisFrame,borderwidth=(0))
btnImagen.grid(column=0,row=0,sticky=(W))
btnImagen['image'] = imagen8'''


# Iniciar el loop principal de la ventana
raiz.mainloop()
