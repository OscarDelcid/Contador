import tkinter 
import tkinter.font as tkFont

ventana = tkinter.Tk()
ventana.geometry("450x300")
fontStyle = tkFont.Font(size = 40)

#Función sumar
def suma():
    valor= int(contador["text"]) 
    contador["text"]  = (valor+ 1)
    valor = contador["text"]
    cambiar_color(valor)

#Función restar
def restar():
    valor= int(contador["text"])
    contador["text"] = f"{valor-1}"
    valor = contador["text"]
    cambiar_color(valor)

#Función Reinciar    
def reiniciar():
    valor= int(contador["text"])
    contador["text"] = (valor*0)
    valor = contador["text"]
    cambiar_color(valor)

#Función Cambiar Color
def cambiar_color(valor):
    if int(valor) < 0:
        contador.config(fg= "red")
    elif int(valor) > 0:
        contador.config(fg= "green")
    else:
        contador.config(fg= "black")


#botones

contador = tkinter.Label(ventana, text = "0", font=fontStyle )
contador.place(x=210, y=100)

#Boton Sumar
btn_1 = tkinter.Button(ventana, text = "Sumar", width=20, height=-4,  command=suma)
btn_1.place(x=40, y=200)

#Boton Reiniciar
btn_2 = tkinter.Button(ventana, text = "Reiniciar", width=20, height=-4, command=reiniciar)
btn_2.place(x=150, y=200)

#Boton Restar
btn_3 = tkinter.Button(ventana, text = "Restar", width=20, height=-4, command=restar)
btn_3.place(x=260, y=200)

ventana.mainloop()