from tkinter import *
from tkinter import messagebox

def abrir_ventana():
    ventana = Tk()
    ventana.title("BAKASH") 
    ventana.geometry("800x500+320+90")
    ventana.resizable(0, 0)
    ventana.config(background="#900474") 

    texto_ingresado = StringVar()

    etiqueta = Label(ventana, text="BAKASH",  
                     font="Arial 15 normal", 
                     background="#900474", 
                     foreground="#e0d2dd", 
                     padx=20, pady=20)
    etiqueta.pack()

    # Crear un Frame para agrupar el Entry y el Botón
    frame = Frame(ventana)
    frame.pack(pady=20)

    # Campo de entrada (Entry) para introducir texto
    inputUrl = Entry(frame, bg="white", font="Arial 9 normal", width=70)
    inputUrl.pack(side=LEFT, padx=5)

    # Función que será ejecutada cuando se presione el botón
    def urlingresada():
        texto_ingresado.set(inputUrl.get())  # Guardar el texto en la variable
        ventana.quit()  

    boton = Button(frame, text="Analizar", font="Arial 9 normal", height=2, width=17,
                   foreground="white", bg="#34bd4a", command=urlingresada)
    boton.pack(side=LEFT, padx=5)

   
    ventana.mainloop()
    return texto_ingresado.get()