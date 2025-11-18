import tkinter as Tk
from tkinter import Button, Entry, Label, Tk
ventana = Tk()
ventana.title("Calculadora IMC")
ventana.geometry("400x600")
ventana.resizable(False, False)
ventana.configure(bg="grey")

etiqueta_nombre = Label(ventana, text='Ingrese su nombre', fg='black', bg='grey')
etiqueta_nombre.pack(pady='10')

nombre = Entry(ventana, width='40')
nombre.pack(pady='5')

etiqueta_edad = Label(ventana, text='Ingrese su edad', fg='black', bg='grey')
etiqueta_edad.pack(pady='10')

edad = Entry(ventana, width='40')
edad.pack(pady='5')

etiqueta_estatura = Label(ventana, text='Ingrese su estatura', fg='black', bg='grey')
etiqueta_estatura.pack(pady='10')

estatura = Entry(ventana, width='40')
estatura.pack(pady='5')


etiqueta_peso = Label(ventana, text='Ingrese su peso', fg='black', bg='grey')
etiqueta_peso.pack(pady='10')

peso = Entry(ventana, width='40')
peso.pack(pady='5')

def calcular_imc():
    estatura_valor = estatura.get()
    peso_valor = peso.get()
    _imc = estatura_valor/peso_valor
    resultado.config(text=f'Hola {nombre}, tu calculo de IMC es {_imc}')

    btn_iniciar = Button(ventana, text='Calcular', command=calcular_imc)
    btn_iniciar.pack(pady='30')



    resultado = Label(ventana, text='', font=('Arial', 20, 'bold'))
    resultado.pack(pady='30')



ventana.mainloop()