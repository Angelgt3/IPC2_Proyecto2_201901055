from tkinter import ttk
from tkinter import *

class Principal:

    def __init__(self,ventana):
        self.vent = ventana
        self.vent.title('Proyecto 2')
        
        #contenedor
        pantalla = LabelFrame(self.vent,text='Cargar Arhivo')
        pantalla.grid(row=0,column=0,columnspan=3,pady=20)

        #Input cargar archivo
        Label(pantalla,text='Ingrese la ruta del archivo').grid(row=1,column=1)
        self.ruta=Entry(pantalla)
        self.ruta.grid(row=1,column=2)

        #Boton cargar archivo
        ttk.Button(pantalla, text="Cargar").grid(row=4,columnspan=5)


if __name__=='__main__':
    ventana=Tk()
    aplicacion=Principal(ventana)
    ventana.mainloop()