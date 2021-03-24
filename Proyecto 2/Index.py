from tkinter import ttk
from tkinter import *
import tkinter.font as tkFont
from xml.dom import minidom
import xml.etree.ElementTree as ET 
import threading 


class Principal:

    def __init__(self,ventana):
        self.vent = ventana
        self.vent.title('Proyecto 2')
        
        #panel1 cargar archivo
        panel1 = LabelFrame(self.vent,text='Cargar Arhivo')
        panel1.grid(row=0,column=0,columnspan=3)

        #panel2 operaciones Una imagen
        panel2 = LabelFrame(self.vent,text='Operaciones para una imagen')
        panel2.grid(row=2,column=0 ,pady=20,columnspan=3)

        #panel3 operaciones con dos imagenes
        panel3 = LabelFrame(self.vent,text='Operaciones con dos iamgenes imagen')
        panel3.grid(row=4,column=0 ,pady=20,columnspan=3)


        #botones radiales //panel 3
        self.opcion_radioboton2=IntVar()
        Radiobutton(panel3,text="Union",variable=self.opcion_radioboton2, value=1).grid(column=0, row=1, sticky="W")
        Radiobutton(panel3,text="Intersección",variable=self.opcion_radioboton2, value=2).grid(column=0, row=2, sticky="W")
        Radiobutton(panel3,text="Diferencia",variable=self.opcion_radioboton2, value=3).grid(column=0, row=3, sticky="W")
        Radiobutton(panel3,text="Diferencia simétrica",variable=self.opcion_radioboton2, value=4).grid(column=0, row=4, sticky="W")

        #Boton opciones de dos imagenes //Panel 3
        ttk.Button(panel3, text="Continuar").grid(row=5,columnspan=2)

        #Input operaciones de dos imagenes //panel3
        Label(panel3,text='Ingrese el nombre de la matriz 1').grid(row=1,column=6)
        self.op2_matriz1=Entry(panel3)
        self.op2_matriz1.grid(row=2,column=6)
        Label(panel3,text='Ingrese el nombre de la matriz 2').grid(row=3,column=6)
        self.op2_matriz2=Entry(panel3)
        self.op2_matriz2.grid(row=4,column=6)


        #botones radiales opcion de una imagen //panel 2
        self.opcion_radioboton=IntVar()
        Radiobutton(panel2,text="Rotacion Horizontal",variable=self.opcion_radioboton, value=1).grid(column=0, row=1, sticky="W")
        Radiobutton(panel2,text="Rotacion Vertical",variable=self.opcion_radioboton, value=2).grid(column=0, row=2, sticky="W")
        Radiobutton(panel2,text="Traspuesta",variable=self.opcion_radioboton, value=3).grid(column=0, row=3, sticky="W")
        Radiobutton(panel2,text="Limpiar",variable=self.opcion_radioboton, value=4).grid(column=0, row=4, sticky="W")
        Radiobutton(panel2,text="Agregar Horizontal",variable=self.opcion_radioboton, value=5).grid(column=0, row=5, sticky="W")
        Radiobutton(panel2,text="Agregar Vertical",variable=self.opcion_radioboton, value=6).grid(column=0, row=6, sticky="W")
        Radiobutton(panel2,text="Agregar Rectangulo",variable=self.opcion_radioboton, value=7).grid(column=0, row=7, sticky="W")
        Radiobutton(panel2,text="Agregar Triangulo",variable=self.opcion_radioboton, value=8).grid(column=0, row=8, sticky="W")

        #Boton opciones de una imagen //Panel 2
        ttk.Button(panel2, text="Continuar", command=event.boton_una_imagen).grid(row=10,columnspan=2)

        #Input operaciones de una iamgen //panel2
        Label(panel2,text='Ingrese el nombre de la matriz').grid(row=3,column=6)
        self.op1_matriz=Entry(panel2)
        self.op1_matriz.grid(row=4,column=6)
        
        #Input cargar archivo //panel1
        Label(panel1,text='Ingrese la ruta del archivo').grid(row=1,column=1)
        self.ruta=Entry(panel1)
        self.ruta.grid(row=2,column=1)

        #Boton cargar archivo //panel1
        ttk.Button(panel1, text="Cargar", command=event.leer_ruta).grid(row=4,columnspan=2)

class form_new_matriz():
    def __init__(self,ventana,es,filas,columnas,lista,filas2,columnas2,lista2):
        self.vent2 = ventana
        self.vent2.title(f'Matriz {es}')

        #panel4 tabla
        panel4 = LabelFrame(self.vent2,text=f'Matriz selecionada')
        panel4.grid(row=3,column=5 ,pady=20,columnspan=3)
        cont_fila=0
        cont_columna=0
        for c in range(int(filas)):
            for a in range(int(columnas)):
                cell = Entry(panel4, width=5)
                cell.grid(row=cont_columna, column=cont_fila)
                cell.insert(0, lista.getDato(cont_fila,cont_columna))
                tipo=tkFont.Font(family="Arial",size="120",weight="bold",slant="italic")
                cell.configure(font=tipo)
                cont_fila+=1
            cont_fila=0
            cont_columna+=1

        #panel5 tabla
        panel5 = LabelFrame(self.vent2,text=f'Matriz operada')
        panel5.grid(row=6,column=5 ,pady=20,columnspan=3)
        cont_fila=0
        cont_columna=0
        for c in range(int(filas2)):
            for a in range(int(columnas2)):
                cell = Entry(panel5, width=5)
                cell.grid(row=cont_columna, column=cont_fila)
                cell.insert(0, lista2.getDato(cont_fila,cont_columna))
                tipo=tkFont.Font(family="Arial",size="120",weight="bold",slant="italic")
                cell.configure(font=tipo)
                cont_fila+=1
            cont_fila=0
            cont_columna+=1

        

class Eventos:

    def leer_ruta(self):
        rut= str(aplicacion.ruta.get())
        try:
            archivo = minidom.parse(rut)
            print("Archivo leido correctamente")
        except:
            print("No se pudo abrir el documento")


    def boton_una_imagen(self):
        archivo=minidom.parse(aplicacion.ruta.get())
        Matriz1=event.cargar_matriz(archivo,aplicacion.op1_matriz.get(),aplicacion.opcion_radioboton.get())
        

        
    def Rotacion_H_1I(self,filas,columnas,Matriz1,Matriz2):
        cont_x=0
        cont_y=int(filas)-1
        for a in range(int(filas)):
            for b in range(int(columnas)):
                #print(f"coordenadas: {cont_x,cont_y}")
                #print(f"dato: {Matriz1.getDato(a,b)} de: {a,b}")
                Matriz2.agregar(cont_x,cont_y,Matriz1.getDato(b,a))
                cont_x+=1
            cont_x=0
            cont_y-=1
    
    def Rotacion_V_1I(self,filas,columnas,Matriz1,Matriz2):
        cont_x=int(columnas)-1
        cont_y=0
        for a in range(int(filas)):
            for b in range(int(columnas)):
                #print(f"coordenadas: {cont_x,cont_y}")
                #print(f"dato: {Matriz1.getDato(a,b)} de: {b,a}")
                Matriz2.agregar(cont_x,cont_y,Matriz1.getDato(b,a))
                cont_x-=1
            cont_x=int(columnas)-1
            cont_y+=1

    def Traspuesta_1I(self,filas,columnas,Matriz1,Matriz2):
        cont_x=0
        cont_y=0
        for a in range(int(filas)):
            for b in range(int(columnas)):
                #print(f"coordenadas: {cont_x,cont_y}")
                #print(f"dato: {Matriz1.getDato(a,b)} de: {a,b}")
                Matriz2.agregar(cont_x,cont_y,Matriz1.getDato(a,b))
                cont_x+=1
            cont_x=0
            cont_y+=1           
    

    def cargar_matriz(self,archivo,nombre,valor):
        matrices=archivo.getElementsByTagName("matriz")
        imagen=""
        filas=""
        columnas=""
        temp=archivo.getElementsByTagName("matriz")

        for matriz in matrices:
            if nombre==matriz.getElementsByTagName("nombre")[0].firstChild.data:
                filas=matriz.getElementsByTagName("filas")[0].firstChild.data
                columnas=matriz.getElementsByTagName("columnas")[0].firstChild.data
                imagen=matriz.getElementsByTagName("imagen")[0].firstChild.data
                
                Matriz1=Lista_ortogonal()
                Matriz1.crear(filas,columnas)
                #Matriz1.recorrer()
                
                x=imagen.splitlines()
                cont_fila=0
                cont_columna=0
                for y in x:
                    z=y.strip()
                    if z!="":
                        #print(f"z:{z}")
                        for a in z:
                            #print(f"a:{a}")
                            if a=="_":
                                a=""
                            Matriz1.agregar(cont_fila,cont_columna,a)
                            cont_fila+=1      
                    else:
                        cont_columna-=1
                    cont_fila=0
                    cont_columna+=1
                
                
        if valor==1:
            Matriz2=Lista_ortogonal()
            Matriz2.crear(filas,columnas)
            event.Rotacion_H_1I(filas,columnas,Matriz1,Matriz2)
            t = threading.Thread(target=event.ventana("ventana_matriz",f'Matriz seleccionada:  "{nombre}" ',filas,columnas,Matriz1,filas,columnas,Matriz2)) 
            t.start()
        elif valor==2:
            Matriz2=Lista_ortogonal()
            Matriz2.crear(filas,columnas)
            event.Rotacion_V_1I(filas,columnas,Matriz1,Matriz2)
            t = threading.Thread(target=event.ventana("ventana_matriz",f'Matriz seleccionada:  "{nombre}" ',filas,columnas,Matriz1,filas,columnas,Matriz2)) 
            t.start()
        elif valor==3:
            Matriz2=Lista_ortogonal()
            Matriz2.crear(columnas,filas)
            event.Traspuesta_1I(columnas,filas,Matriz1,Matriz2)
            t = threading.Thread(target=event.ventana("ventana_matriz",f'Matriz seleccionada:  "{nombre}" ',filas,columnas,Matriz1,columnas,filas,Matriz2)) 
            t.start()
            
        

    def ventana(self,nombre,es,filas,columnas,lista,filas2,columnas2,lista2):
        nombre=Tk()
        aplicacion1=form_new_matriz(nombre,es,filas,columnas,lista,filas2,columnas2,lista2)
        nombre.mainloop()




class nodo():

    def __init__(self,dato):
        self.dato=dato
        self.derecha=None
        self.izquierda=None
        self.arriba=None
        self.abajo=None


class Lista_ortogonal():    
    
    def __init__(self):
        self.cabeza = None
    
    def crear(self,fila,columna):
        temp_arriba=nodo(None)
        temp_derecha=nodo(None)
        for a in range(int(fila)):
            for b in range(int(columna)):
                nuevo = nodo(f"*{a+1},{b+1}")
                #print(nuevo.dato)
                nuevo.abajo=None
                nuevo.derecha=None
                if b == 0:
                    nuevo.derecha=None
                    if self.cabeza==None:
                        self.cabeza=nuevo
                    temp_derecha=nuevo
                else:
                    nuevo.izquierda=temp_derecha
                    temp_derecha.derecha=nuevo
                    temp_derecha = nuevo
                if a == 0:
                    nuevo.arriba=None
                    temp_derecha=nuevo
                else:
                    nuevo.arriba=temp_arriba
                    temp_arriba.abajo = nuevo
                    temp_arriba=temp_arriba.derecha
            temp_arriba=self.cabeza
            while temp_arriba.abajo is not None:
                temp_arriba=temp_arriba.abajo
        
    def agregar(self,x,y,valor):
        if self.cabeza is not None:
            temp=self.cabeza
            cont_x=0
            cont_y=0
            while temp is not None:
                temp2=temp
                while temp2 is not None:
                    if cont_x==int(x) and cont_y==int(y):
                        temp2.dato=valor
                        #print(f" temp2= {temp2.dato}")
                        break
                    temp2=temp2.derecha
                    cont_x+=1
                cont_x=0
                temp=temp.abajo
                cont_y+=1
        else:
            print("La lista esta vacia ")

    def getDato(self,x,y):
        if self.cabeza is not None:
            temp=self.cabeza
            cont_x=0
            cont_y=0
            while temp is not None:
                temp2=temp
                while temp2 is not None:
                    if cont_x==int(x) and cont_y==int(y):
                        return temp2.dato
                    temp2=temp2.derecha
                    cont_x+=1
                cont_x=0
                temp=temp.abajo
                cont_y+=1
        else:
            print("La lista esta vacia ")

    

    def recorrer(self):
        if self.cabeza is not None:
            temp=self.cabeza
            while temp is not None:
                temp2=temp
                while temp2 is not None:
                    print(temp2.dato)
                    temp2=temp2.derecha
                temp=temp.abajo
        else:
            print("La lista esta vacia")


event=Eventos()


if __name__=='__main__':
    ventana=Tk()
    aplicacion=Principal(ventana)
    ventana.mainloop()