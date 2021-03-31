from tkinter import ttk
from tkinter import *
from datetime import datetime
import tkinter.font as tkFont
from xml.dom import minidom
import xml.etree.ElementTree as ET 
import threading 
import webbrowser
import io
import os


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

        #Boton ayuda 
        ttk.Button(self.vent, text="Ayuda",command=event.ayuda).grid(row=0,column=10)
        #Boton reporte 
        ttk.Button(self.vent, text="Reporte",command=event.reporte).grid(row=0,column=9)
        
        #botones radiales //panel 3
        self.opcion_radioboton2=IntVar()
        Radiobutton(panel3,text="Union",variable=self.opcion_radioboton2, value=1).grid(column=0, row=1, sticky="W")
        Radiobutton(panel3,text="Intersección",variable=self.opcion_radioboton2, value=2).grid(column=0, row=2, sticky="W")
        Radiobutton(panel3,text="Diferencia",variable=self.opcion_radioboton2, value=3).grid(column=0, row=3, sticky="W")
        Radiobutton(panel3,text="Diferencia simétrica",variable=self.opcion_radioboton2, value=4).grid(column=0, row=4, sticky="W")

        #Boton opciones de dos imagenes //Panel 3
        ttk.Button(panel3, text="Continuar",command=event.boton_dos_imagenes).grid(row=5,columnspan=2)

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

        #panel4 pregunta 
        panel4 = LabelFrame(self.vent,text='Valores: Limpiar,agregar para una imagen')
        panel4.grid(row=2,column=8 ,pady=20,columnspan=3)
        #input 1 fila inicial
        Label(panel4,text='Ingrese no. fila inicial:').grid(row=0,column=1)
        self.fila_inicial=Entry(panel4)
        self.fila_inicial.grid(row=1,column=1)
        #input 3 fila final
        Label(panel4,text='Ingrese no. fila final:').grid(row=2,column=1)
        self.fila_final=Entry(panel4)
        self.fila_final.grid(row=3,column=1)
        #input 2 columna inicial
        Label(panel4,text='Ingrese no. columna inicial:').grid(row=4,column=1)
        self.columna_inicial=Entry(panel4)
        self.columna_inicial.grid(row=5,column=1)
        #input 4 columna final
        Label(panel4,text='Ingrese no. columna final:').grid(row=6,column=1)
        self.columna_final=Entry(panel4)
        self.columna_final.grid(row=7,column=1)


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
                celda = Entry(panel4, width=5)
                celda.grid(row=cont_columna, column=cont_fila)
                celda.insert(0, lista.getDato(cont_fila,cont_columna))
                tipo=tkFont.Font(family="Arial",size="120",weight="bold",slant="italic")
                celda.configure(font=tipo)
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
                celda = Entry(panel5, width=5)
                celda.grid(row=cont_columna, column=cont_fila)
                celda.insert(0, lista2.getDato(cont_fila,cont_columna))
                tipo=tkFont.Font(family="Arial",size="120",weight="bold",slant="italic")
                celda.configure(font=tipo)
                cont_fila+=1
            cont_fila=0
            cont_columna+=1
    
class form_new_matriz2():
    def __init__(self,ventana,es,filas,columnas,lista,filas2,columnas2,lista2,lista3,filas3,columnas3):
        self.vent2 = ventana
        self.vent2.title(f'Operacion {es}')

        #panel4 tabla
        panel4 = LabelFrame(self.vent2,text=f'Matriz 1')
        panel4.grid(row=3,column=5 ,pady=20,columnspan=3)
        cont_fila=0
        cont_columna=0
        for c in range(int(filas)):
            for a in range(int(columnas)):
                celda = Entry(panel4, width=5)
                celda.grid(row=cont_columna, column=cont_fila)
                celda.insert(0, lista.getDato(cont_fila,cont_columna))
                tipo=tkFont.Font(family="Arial",size="120",weight="bold",slant="italic")
                celda.configure(font=tipo)
                cont_fila+=1
            cont_fila=0
            cont_columna+=1

        #panel5 tabla
        panel5 = LabelFrame(self.vent2,text=f'Matriz 2')
        panel5.grid(row=6,column=5 ,pady=20,columnspan=3)
        cont_fila=0
        cont_columna=0
        for c in range(int(filas2)):
            for a in range(int(columnas2)):
                celda = Entry(panel5, width=5)
                celda.grid(row=cont_columna, column=cont_fila)
                celda.insert(0, lista2.getDato(cont_fila,cont_columna))
                tipo=tkFont.Font(family="Arial",size="120",weight="bold",slant="italic")
                celda.configure(font=tipo)
                cont_fila+=1
            cont_fila=0
            cont_columna+=1

        #Panel6 tabla
        panel6 = LabelFrame(self.vent2,text=f'Matriz operada')
        panel6.grid(row=9,column=5 ,pady=20,columnspan=3)
        cont_fila=0
        cont_columna=0
        for c in range(int(filas3)):
            for a in range(int(columnas3)):
                celda = Entry(panel6, width=5)
                celda.grid(row=cont_columna, column=cont_fila)
                celda.insert(0, lista3.getDato(cont_fila,cont_columna))
                tipo=tkFont.Font(family="Arial",size="120",weight="bold",slant="italic")
                celda.configure(font=tipo)
                cont_fila+=1
            cont_fila=0
            cont_columna+=1
        

class Eventos:

    def leer_ruta(self):
        rut= str(aplicacion.ruta.get())
        #try:
        archivo = minidom.parse(rut)
        matrices=archivo.getElementsByTagName("matriz")
        for matriz in matrices:
            nombre=matriz.getElementsByTagName("nombre")[0].firstChild.data
            imagen=matriz.getElementsByTagName("imagen")[0].firstChild.data
            x=imagen.splitlines()
            vacios=0
            llenos=0
            for y in x:
                z=y.strip()
                if z!="":
                    for a in z:
                        if a=="_" or a=="-":
                            vacios+=1
                        else:
                            llenos+=1
            fecha=datetime.now().strftime('%d/%m/%Y - %H:%M:%S')
            Report.agregar_ultimo(fecha,nombre,llenos,vacios)
        #Report.recorrer()
        print("Archivo leido correctamente")
        #except:
        #print("No se pudo abrir el documento")


    def boton_una_imagen(self):
        archivo=minidom.parse(aplicacion.ruta.get())
        Matriz1=event.cargar_matriz(archivo,aplicacion.op1_matriz.get(),aplicacion.opcion_radioboton.get())
        
    def boton_dos_imagenes(self):
        archivo=minidom.parse(aplicacion.ruta.get())
        event.cargar_matriz2(archivo,aplicacion.op2_matriz1.get(),aplicacion.op2_matriz2.get(),aplicacion.opcion_radioboton2.get())

    def ayuda(self):
        print("sot la ayuda")
    
    def reporte(self):
        f = open('REPORTE.html','w')
        mensaje="""
        <html>
            <head><title>REPORTE</title></head>
            <body>
                <h1>REPORTE MATRICES</h1>
                <TABLE BORDER>
                    <TR>
                        <TH>No</TH> <TH>Fecha</TH> <TH>Nombre</TH><TH>Espacios llenos</TH><TH>Espacios vacios</TH>
                    </TR>
            """
        mensaje2=""
        n=0
        for e in range(int(Report.tamaño())):
            temp_mensaje=f"""
                    <TR>
                        <TD>{n+1}</TD> <TD>{Report.buscar(n,0)}</TD> <TD>{Report.buscar(n,1)}</TD><TD>{Report.buscar(n,2)}</TD><TD>{Report.buscar(n,3)}</TD>
                    </TR>"""
            mensaje2+=temp_mensaje
            n+=1
        
        mensaje4="""
                </TABLE>
                <h1>REPORTE OPERACIONES</h1>
                <TABLE BORDER>
                    <TR>
                        <TH>No</TH> <TH>Fecha</TH> <TH>Operacion</TH><TH>Nombre(s)</TH>
                    </TR>
            """
        for e in range(int(Report2.tamaño())):
            temp_mensaje=f"""
                    <TR>
                        <TD>{e+1}</TD> <TD>{Report2.buscar(e,0)}</TD> <TD>{Report2.buscar(e,1)}</TD><TD>{Report2.buscar(e,2)}</TD>
                    </TR>"""
            mensaje4+=temp_mensaje

        mensaje3="""
                </TABLE>
            </body>
        </html>
                """
        mensajefinal=mensaje+mensaje2+mensaje4+mensaje3
        f.write(mensajefinal)
        f.close()

        try:
            nombreArchivo = 'C:/Users/angge/OneDrive/Documentos/GitHub/IPC2_Proyecto2_201901055/Proyecto 2/REPORTE.html'
            webbrowser.open_new_tab(nombreArchivo)
        except :
            print("no se pudo abrir automaticamente")


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
    
    def Limpiar_1I(self,filas,columnas,Matriz1,Matriz2):
        f_i=aplicacion.fila_inicial.get()
        f_f=aplicacion.fila_final.get()
        c_i=aplicacion.columna_inicial.get()
        c_f=aplicacion.columna_final.get()

        for a in range(int(filas)):
            for b in range(int(columnas)):
                Matriz2.agregar(b,a,Matriz1.getDato(b,a))
 
        for a in range(int(filas)):
            for b in range(int(columnas)):
                if a>=int(f_i)-1 and a<=int(f_f)-1 and b>=int(c_i)-1 and b<=int(c_f)-1: 
                    Matriz2.agregar(b,a,"")
        #Matriz2.recorrer()

    def agregar_FH(self,filas,columnas,Matriz1,Matriz2):
        f_i=aplicacion.fila_inicial.get()
        c_i=aplicacion.columna_inicial.get()
        c_f=aplicacion.columna_final.get()

        for a in range(int(filas)):
            for b in range(int(columnas)):
                Matriz2.agregar(b,a,Matriz1.getDato(b,a))
 
        for a in range(int(filas)):
            for b in range(int(columnas)):
                if (a==int(f_i)-1 and b>=int(c_i)-1 and b<=int(c_f)-1): 
                    Matriz2.agregar(b,a,"*")
    
    def agregar_FV(self,filas,columnas,Matriz1,Matriz2):
        f_i=aplicacion.fila_inicial.get()
        f_f=aplicacion.fila_final.get()
        c_i=aplicacion.columna_inicial.get()

        for a in range(int(filas)):
            for b in range(int(columnas)):
                Matriz2.agregar(b,a,Matriz1.getDato(b,a))
 
        for a in range(int(filas)):
            for b in range(int(columnas)):
                if (a>=int(f_i)-1 and a<=int(f_f)-1 and b==int(c_i)-1): 
                    Matriz2.agregar(b,a,"*")

    def Rectangulo_1I(self,filas,columnas,Matriz1,Matriz2):
        f_i=aplicacion.fila_inicial.get()
        f_f=aplicacion.fila_final.get()
        c_i=aplicacion.columna_inicial.get()
        c_f=aplicacion.columna_final.get()

        for a in range(int(filas)):
            for b in range(int(columnas)):
                Matriz2.agregar(b,a,Matriz1.getDato(b,a))
 
        for a in range(int(filas)):
            for b in range(int(columnas)):
                if  ((a>=int(f_i)-1 and a<=int(f_f)-1) and (b==int(c_i)-1 or b==int(c_f)-1)) or ((a==int(f_i)-1 or a==int(f_f)-1) and (b>=int(c_i)-1 and b<=int(c_f)-1)): 
                    Matriz2.agregar(b,a,"*")
    
    def Triangulo_1I(self,filas,columnas,Matriz1,Matriz2):
        f_i=aplicacion.fila_inicial.get()
        c_i=aplicacion.columna_inicial.get()
        f_f=aplicacion.fila_final.get()
        c_f=f_f
        longitud=int(f_f)-int(f_i)
        for a in range(int(filas)):
            for b in range(int(columnas)):
                Matriz2.agregar(b,a,Matriz1.getDato(b,a))

        for a in range(int(filas)):
            for b in range(int(columnas)):
                if (a>=int(f_i)-1 and a<=int(f_f)-1 and b==int(c_i)-1):
                    Matriz2.agregar(b,a,"*")
                if (a==int(f_f)-1 and b>=int(c_i)-1 and b<=int(c_f)-1):
                    Matriz2.agregar(b,a,"*")
                if a==int(f_i)-1 and b==int(c_i)-1:
                    for c in range(longitud):
                        Matriz2.agregar(b+(c+1),a+(c+1),"*")

    def cargar_matriz(self,archivo,nombre,valor):
        matrices=archivo.getElementsByTagName("matriz")
        imagen=""
        filas=""
        columnas=""

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
                            if a=="_" or a=="-":
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
            fecha=datetime.now().strftime('%d/%m/%Y - %H:%M:%S')
            Report2.agregar_ultimo(fecha,"Rotación horizontal",nombre)
            t = threading.Thread(target=event.ventana("ventana_matriz",f'Matriz seleccionada:  "{nombre}" ',filas,columnas,Matriz1,filas,columnas,Matriz2)) 
            t.start()
        elif valor==2:
            Matriz2=Lista_ortogonal()
            Matriz2.crear(filas,columnas)
            event.Rotacion_V_1I(filas,columnas,Matriz1,Matriz2)
            fecha=datetime.now().strftime('%d/%m/%Y - %H:%M:%S')
            Report2.agregar_ultimo(fecha,"Rotación vertical",nombre)
            t = threading.Thread(target=event.ventana("ventana_matriz",f'Matriz seleccionada:  "{nombre}" ',filas,columnas,Matriz1,filas,columnas,Matriz2)) 
            t.start()
        elif valor==3:
            Matriz2=Lista_ortogonal()
            Matriz2.crear(columnas,filas)
            event.Traspuesta_1I(columnas,filas,Matriz1,Matriz2)
            fecha=datetime.now().strftime('%d/%m/%Y - %H:%M:%S')
            Report2.agregar_ultimo(fecha,"Transpuesta",nombre)
            t = threading.Thread(target=event.ventana("ventana_matriz",f'Matriz seleccionada:  "{nombre}" ',filas,columnas,Matriz1,columnas,filas,Matriz2)) 
            t.start()
        elif valor==4:
            Matriz2=Lista_ortogonal()
            Matriz2.crear(filas,columnas)
            event.Limpiar_1I(filas,columnas,Matriz1,Matriz2)
            fecha=datetime.now().strftime('%d/%m/%Y - %H:%M:%S')
            Report2.agregar_ultimo(fecha,"Limpiar zona",nombre)
            t = threading.Thread(target=event.ventana("ventana_matriz",f'Matriz seleccionada:  "{nombre}" ',filas,columnas,Matriz1,filas,columnas,Matriz2)) 
            t.start()
        elif valor==5:
            Matriz2=Lista_ortogonal()
            Matriz2.crear(filas,columnas)
            event.agregar_FH(filas,columnas,Matriz1,Matriz2)
            fecha=datetime.now().strftime('%d/%m/%Y - %H:%M:%S')
            Report2.agregar_ultimo(fecha,"Agregar línea horizontal",nombre)
            t = threading.Thread(target=event.ventana("ventana_matriz",f'Matriz seleccionada:  "{nombre}" ',filas,columnas,Matriz1,filas,columnas,Matriz2)) 
            t.start()
        elif valor==6:
            Matriz2=Lista_ortogonal()
            Matriz2.crear(filas,columnas)
            event.agregar_FV(filas,columnas,Matriz1,Matriz2)
            fecha=datetime.now().strftime('%d/%m/%Y - %H:%M:%S')
            Report2.agregar_ultimo(fecha,"Agregar línea vertical",nombre)
            t = threading.Thread(target=event.ventana("ventana_matriz",f'Matriz seleccionada:  "{nombre}" ',filas,columnas,Matriz1,filas,columnas,Matriz2)) 
            t.start()
        elif valor==7:
            Matriz2=Lista_ortogonal()
            Matriz2.crear(filas,columnas)
            event.Rectangulo_1I(filas,columnas,Matriz1,Matriz2)
            fecha=datetime.now().strftime('%d/%m/%Y - %H:%M:%S')
            Report2.agregar_ultimo(fecha,"Agregar rectángulo",nombre)
            t = threading.Thread(target=event.ventana("ventana_matriz",f'Matriz seleccionada:  "{nombre}" ',filas,columnas,Matriz1,filas,columnas,Matriz2)) 
            t.start()
        elif valor==8:
            Matriz2=Lista_ortogonal()
            Matriz2.crear(filas,columnas)
            event.Triangulo_1I(filas,columnas,Matriz1,Matriz2)
            fecha=datetime.now().strftime('%d/%m/%Y - %H:%M:%S')
            Report2.agregar_ultimo(fecha,"Agregar triángulo rectángulo",nombre)
            t = threading.Thread(target=event.ventana("ventana_matriz",f'Matriz seleccionada:  "{nombre}" ',filas,columnas,Matriz1,filas,columnas,Matriz2)) 
            t.start()
      

    def ventana(self,nombre,es,filas,columnas,lista,filas2,columnas2,lista2):
        nombre=Tk()
        aplicacion1=form_new_matriz(nombre,es,filas,columnas,lista,filas2,columnas2,lista2)
        nombre.mainloop()

    def union(self,Matriz1,Matriz2,Matriz3,filas,columnas):
        for a in range(int(filas)):
            for b in range(int(columnas)):
                try:
                    if Matriz1.getDato(b,a)=="*" or Matriz2.getDato(b,a)=="*":
                        Matriz3.agregar(b,a,"*")
                    else:
                        Matriz3.agregar(b,a,"")
                except:
                    continue

    def Interseccion(self,Matriz1,Matriz2,Matriz3,filas,columnas):
        for a in range(int(filas)):
            for b in range(int(columnas)):
                try:
                    if Matriz1.getDato(b,a)=="*" and Matriz2.getDato(b,a)=="*":
                        Matriz3.agregar(b,a,"*")
                    else:
                        Matriz3.agregar(b,a,"")
                except:
                    continue

    def Diferencia(self,Matriz1,Matriz2,Matriz3,filas,columnas):
        for a in range(int(filas)):
            for b in range(int(columnas)):
                try:
                    if Matriz1.getDato(b,a)=="*" and Matriz2.getDato(b,a)!="*":
                        Matriz3.agregar(b,a,"*")
                    else:
                        Matriz3.agregar(b,a,"")
                except:
                    continue
    
    def Diferencia_simetrica(self,Matriz1,Matriz2,Matriz3,filas,columnas):
        for a in range(int(filas)):
            for b in range(int(columnas)):
                try:
                    if (Matriz1.getDato(b,a)=="*" and Matriz2.getDato(b,a)!="*") or (Matriz1.getDato(b,a)!="*" and Matriz2.getDato(b,a)=="*"):
                        Matriz3.agregar(b,a,"*")
                    else:
                        Matriz3.agregar(b,a,"")
                except:
                    continue


    def cargar_matriz2(self,archivo,nombre1,nombre2,valor):
        matrices=archivo.getElementsByTagName("matriz")
        imagen=""
        filas=""
        columnas=""
        imagen2=""
        filas2=""
        columnas2=""
        for matriz in matrices:
            if nombre1==matriz.getElementsByTagName("nombre")[0].firstChild.data:
                filas=matriz.getElementsByTagName("filas")[0].firstChild.data
                columnas=matriz.getElementsByTagName("columnas")[0].firstChild.data
                imagen=matriz.getElementsByTagName("imagen")[0].firstChild.data
                Matriz1=Lista_ortogonal()
                Matriz1.crear(filas,columnas)
                x=imagen.splitlines()
                cont_fila=0
                cont_columna=0
                for y in x:
                    z=y.strip()
                    if z!="":
                        #print(f"z:{z}")
                        for a in z:
                            #print(f"a:{a}")
                            if a=="_" or a=="-":
                                a=""
                            Matriz1.agregar(cont_fila,cont_columna,a)
                            cont_fila+=1      
                    else:
                        cont_columna-=1
                    cont_fila=0
                    cont_columna+=1
            elif nombre2==matriz.getElementsByTagName("nombre")[0].firstChild.data:
                filas2=matriz.getElementsByTagName("filas")[0].firstChild.data
                columnas2=matriz.getElementsByTagName("columnas")[0].firstChild.data
                imagen2=matriz.getElementsByTagName("imagen")[0].firstChild.data
                Matriz2=Lista_ortogonal()
                Matriz2.crear(filas2,columnas2)
                q=imagen2.splitlines()
                cont_fila=0
                cont_columna=0
                for u in q:
                    m=u.strip()
                    if m!="":
                        #print(f"z:{z}")
                        for d in m:
                            #print(f"a:{a}")
                            if d=="_" or d=="-":
                                d=""
                            Matriz2.agregar(cont_fila,cont_columna,d)
                            cont_fila+=1      
                    else:
                        cont_columna-=1
                    cont_fila=0
                    cont_columna+=1
        nc=0
        nf=0
        if columnas>columnas2 or columnas==columnas2:
            nc=columnas
        elif columnas<columnas2:
            nc=columnas2

        if filas>filas2 or filas==filas2:
            nf=filas
        elif filas<filas2:
            nf=filas2
             
        if valor==1:
            Matriz3=Lista_ortogonal()
            Matriz3.crear(nf,nc)
            event.union(Matriz1,Matriz2,Matriz3,nf,nc)
            fecha=datetime.now().strftime('%d/%m/%Y - %H:%M:%S')
            nombres=f"{nombre1},{nombre2}"
            Report2.agregar_ultimo(fecha,"Union",nombres)
            t = threading.Thread(target=event.ventana2("ventana_matriz","Union",filas,columnas,Matriz1,filas2,columnas2,Matriz2,Matriz3,nf,nc)) 
            t.start()
        elif valor==2:
            Matriz3=Lista_ortogonal()
            Matriz3.crear(nf,nc)
            event.Interseccion(Matriz1,Matriz2,Matriz3,nf,nc)
            fecha=datetime.now().strftime('%d/%m/%Y - %H:%M:%S')
            nombres=f"{nombre1},{nombre2}"
            Report2.agregar_ultimo(fecha,"Interseccion",nombres)
            t = threading.Thread(target=event.ventana2("ventana_matriz","Union",filas,columnas,Matriz1,filas2,columnas2,Matriz2,Matriz3,nf,nc)) 
            t.start()
        elif valor==3:
            Matriz3=Lista_ortogonal()
            Matriz3.crear(nf,nc)
            event.Diferencia(Matriz1,Matriz2,Matriz3,nf,nc)
            fecha=datetime.now().strftime('%d/%m/%Y - %H:%M:%S')
            nombres=f"{nombre1},{nombre2}"
            Report2.agregar_ultimo(fecha,"Diferencia",nombres)
            t = threading.Thread(target=event.ventana2("ventana_matriz","Union",filas,columnas,Matriz1,filas2,columnas2,Matriz2,Matriz3,nf,nc)) 
            t.start()

        elif valor==4:
            Matriz3=Lista_ortogonal()
            Matriz3.crear(nf,nc)
            event.Diferencia_simetrica(Matriz1,Matriz2,Matriz3,nf,nc)
            fecha=datetime.now().strftime('%d/%m/%Y - %H:%M:%S')
            nombres=f"{nombre1},{nombre2}"
            Report2.agregar_ultimo(fecha,"Diferencia_simetrica",nombres)
            t = threading.Thread(target=event.ventana2("ventana_matriz","Union",filas,columnas,Matriz1,filas2,columnas2,Matriz2,Matriz3,nf,nc)) 
            t.start()
            
        
                
    def ventana2(self,nombre,es,filas,columnas,lista,filas2,columnas2,lista2,lista3,filas3,columnas3):
        nombre=Tk()
        aplicacion2=form_new_matriz2(nombre,es,filas,columnas,lista,filas2,columnas2,lista2,lista3,filas3,columnas3)
        nombre.mainloop()


class Nodo_C(object):
    def __init__(self,fecha,nombre,llenos,vacios):
        self.fecha =fecha 
        self.nombre=nombre
        self.llenos=llenos
        self.vacios=vacios
        self.siguiente = None

class Lista_Circular(object):
    def __init__(self):
        self.cabeza=None
    
    def esta_vacia(self):
        if self.cabeza is None:
            return True
        else:
            return False

    def tamaño(self):
        temp=self.cabeza
        cont=0
        while temp is not None:
            cont+=1
            if temp.siguiente == self.cabeza:
                break
            else:
                temp=temp.siguiente
        #print(cont)
        return cont
    
    def agregar_ultimo(self,fecha,nombre,llenos,vacios):
        nodo=Nodo_C(fecha,nombre,llenos,vacios)
        if self.esta_vacia():
            self.cabeza = nodo
            nodo.siguiente=self.cabeza
        else:
            temp=self.cabeza
            while temp.siguiente is not self.cabeza:
                temp=temp.siguiente
            temp.siguiente=nodo
            nodo.siguiente =self.cabeza

    def recorrer(self):
        if self.esta_vacia():
            return print("Esta vacia")
        temp=self.cabeza
        print(temp.fecha)
        print(temp.nombre)
        print(temp.llenos)
        print(temp.vacios)
        while temp.siguiente is not self.cabeza:
            temp=temp.siguiente
            print(temp.fecha)
            print(temp.nombre)
            print(temp.llenos)
            print(temp.vacios)
            


    def buscar(self,posicion,cual):
        if self.esta_vacia():
            return("la lista esta vacia")
        if posicion==0:
            if cual==0:
                return self.cabeza.fecha
            elif cual==1:
                return self.cabeza.nombre
            elif cual==2:
                return self.cabeza.llenos
            elif cual==3:
                return self.cabeza.vacios
        elif posicion >0:
            temp=self.cabeza
            for a in range(int(posicion)):
                temp=temp.siguiente
            if cual==0:
                return temp.fecha
            elif cual==1:
                return temp.nombre
            elif cual==2:
                return temp.llenos
            elif cual==3:
                return temp.vacios


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

class Nodo_C2(object):
    def __init__(self,fecha,operacion,nombre):
        self.fecha =fecha 
        self.nombre=nombre
        self.operacion=operacion
        self.siguiente = None

class Lista_Circular2(object):
    def __init__(self):
        self.cabeza=None
    
    def esta_vacia(self):
        if self.cabeza is None:
            return True
        else:
            return False

    def tamaño(self):
        temp=self.cabeza
        cont=0
        while temp is not None:
            cont+=1
            if temp.siguiente == self.cabeza:
                break
            else:
                temp=temp.siguiente
        #print(cont)
        return cont
    
    def agregar_ultimo(self,fecha,operacion,nombre):
        nodo=Nodo_C2(fecha,operacion,nombre)
        if self.esta_vacia():
            self.cabeza = nodo
            nodo.siguiente=self.cabeza
        else:
            temp=self.cabeza
            while temp.siguiente is not self.cabeza:
                temp=temp.siguiente
            temp.siguiente=nodo
            nodo.siguiente =self.cabeza

    def recorrer(self):
        if self.esta_vacia():
            return print("Esta vacia")
        temp=self.cabeza
        print(temp.fecha)
        print(temp.nombre)
        print(temp.operacion)
        while temp.siguiente is not self.cabeza:
            temp=temp.siguiente
            print(temp.fecha)
            print(temp.nombre)
            print(temp.operacion)  


    def buscar(self,posicion,cual):
        if self.esta_vacia():
            return("la lista esta vacia")
        if posicion==0:
            if cual==0:
                return self.cabeza.fecha
            elif cual==1:
                return self.cabeza.nombre
            elif cual==2:
                return self.cabeza.operacion
        elif posicion >0:
            temp=self.cabeza
            for a in range(int(posicion)):
                temp=temp.siguiente
            if cual==0:
                return temp.fecha
            elif cual==1:
                return temp.nombre
            elif cual==2:
                return temp.operacion



event=Eventos()
Report=Lista_Circular()
Report2=Lista_Circular2()



if __name__=='__main__':
    ventana=Tk()
    aplicacion=Principal(ventana)
    ventana.mainloop()