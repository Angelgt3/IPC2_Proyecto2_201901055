from tkinter import ttk
from tkinter import *

class Product:

    def __init__(self,ventana):
        self.wind = ventana
        self.wind.title('Proyecto 2')

if __name__=='__main__':
    ventana=Tk()
    aplicacion=Product(ventana)
    ventana.mainloop()