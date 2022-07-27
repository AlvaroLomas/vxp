# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 19:31:49 2022

@author: boall
"""

import tkinter as tk
from tkinter import *
from ReconocimientoFacial import reconocimientoFacial
from CapturandoRostros import captura

def insertarNombre ():
    ws = Tk()
    ws.title('Dataset')
    ws.geometry('400x200')
    def enviarNombre():
        name= name_Tf.get()
        captura(name)
    Label(ws, text="Ingrese su nombre").pack()
    name_Tf = Entry(ws)
    name_Tf.pack()
    Button(ws, text="Aceptar", command=enviarNombre).pack()
    return name_Tf
    
class Menu():
    ventana = tk.Tk()
    ventana.title("Proyecto Reconocimiento Facial")
    ventana.geometry("500x500")
    imagen= PhotoImage(file="C:/Users/boall/OneDrive/Escritorio/Reconocimiento Facial/ups3.png")
    Label(ventana, image=imagen, bd=0).pack()
    #el_menu = tk.Menu(ventana)
    boton = Frame( ventana) 
    boton.pack(pady = 10) 
    button1 = Button( boton, text = "Detector de Rostros (Dataset y Entrenamiento)", command=insertarNombre) 
    button1.pack(pady = 10)
    button2 = Button( boton, text = "Reconocimiento Facial (Aplastar letra Q para salir)", command=reconocimientoFacial) 
    button2.pack(pady = 10)
    #ventana.config(menu=el_menu)
    ventana.mainloop()