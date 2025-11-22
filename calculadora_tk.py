from tkinter import Tk, Label, Entry, Button, messagebox

ventana = Tk()
ventana.title("Calculadora IMC")
ventana.geometry("500x450")
ventana.resizable(False, False)
ventana.configure(bg="grey")

lbl_peso = Label(ventana, text="Ingrese su peso (kg)", fg="black", font=("Arial", 12,), bg='grey')
lbl_peso.pack(pady=25)

peso = Entry(ventana, width=30, bg='grey', font=("Arial", 11))
peso.pack(pady=0)

lbl_altura = Label(ventana, text="Ingrese su altura (cm)", fg="black", bg='grey', font=("Arial", 12))
lbl_altura.pack(pady=25)

altura = Entry(ventana, width=30, bg='grey', font=("Arial", 11))
altura.pack(pady=0)

resultado = Label(ventana, text="", font=("Arial", 12), bg='grey', wraplength=450, fg="black")
resultado.pack(pady=30)

def iniciar():
    try:
        peso_valor = peso.get()
        altura_valor = altura.get()
        peso_kg = float(peso_valor)
        altura_m = float(altura_valor) / 100
        imc = peso_kg / (altura_m ** 2)
        if peso <= 0 or altura <= 0:
            messagebox.showerror("Error", "El peso y la estatura deben ser números positivos.")
            return
    except ValueError:
        messagebox.showerror("Por favor, ingresa solo números válidos en los campos.")  
    resultado.config(text=f"Tu peso es {peso_valor} kilos y tu altura es {altura_valor} cm y tu IMC es {imc}", fg= 'red', bg= 'white')

def reiniciar():
    peso.delete(0, 'end')
    altura.delete(0, 'end')
    resultado.config(text="")
    peso.focus()

frame_botones = Label(ventana,bg='grey',)
frame_botones.pack(pady=20)

btn_iniciar = Button(frame_botones, text="Iniciar", command=iniciar)
btn_iniciar.pack(side="left", padx=10)

btn_reiniciar = Button(frame_botones, text="Reiniciar", command=reiniciar)
btn_reiniciar.pack(side="left", padx=10)

ventana.mainloop()


resultado = Label(ventana, text='', font=('Arial', 15, 'bold'))
resultado.pack(pady='30')



ventana.mainloop()
