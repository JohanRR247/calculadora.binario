from tkinter import *

ventana = Tk()
ventana.title("calculadora")

# Establecer el color de fondo
ventana.configure(bg="light blue") 
i=0

e_texto = Entry (ventana, font= ("calibri 20"))
e_texto.grid(row =0, column= 0, columnspan= 4, padx=5, pady =5)

def click_boton(valor):
    global i
    e_texto.insert(i, valor)
    i += 1
    
def borrar():
    e_texto.delete(0, END)
    i=0
def opercacion():
    ecuacion = e_texto.get()
    resultado = eval(ecuacion)
    e_texto.delete(0, END)
    e_texto.insert(0, resultado)
    i = 0     
def borrar_caracter():
    ecuacion = e_texto.get()[:-1] 
    e_texto.delete(0, END)
    e_texto.insert(0, ecuacion)
    
def decimal_a_binario():
    ecuacion = e_texto.get()
    resultado_decimal = eval(ecuacion)
    resultado_binario = format(int(resultado_decimal), 'b')  
    e_texto.delete(0, END)
    e_texto.insert(0, resultado_binario)
    
def switchButtonState():
    if boton_ON['text'] == 'ON':
        boton_ON['text'] = 'OFF'
        state = DISABLED
    else:
        boton_ON['text'] = 'ON'
        state = NORMAL
        
    botones = [boton1, boton2, boton3, boton4, boton5, boton6, boton7, boton8, boton9, boton0,
               boton_borrar, boton_Parentesis1, boton_Parentesis2, boton_div, boton_mult, 
               boton_suma, boton_resta, boton_Punto, boton_igual, boton_binario, boton_borrar_caracter]
    
    for boton in botones:
        boton.config(state=state)

def resize(event):
    ventana.geometry(f"{event.width}x{event.height}")

def resize(event):
    # Configurar el tamaño de los botones en función del tamaño de la ventana
    button_width = event.width // 5
    button_height = event.height // 7
    
    # Configurar el tamaño de los botones
    for button in buttons:
        button.config(width=button_width, height=button_height)

boton_ON = Button(ventana, text="ON", width=5, height=2, command=switchButtonState)
boton_ON.grid(row=6, column=2, padx=5, pady=5)

# Lista de botones
button_texts = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
                "AC", "(", ")", "/", "*", "+", "-", ".", "="]

# Crear los botones y colocarlos en la ventana usando el sistema de grid
buttons = []
row_val, col_val = 1, 0
for button_text in button_texts:
    button = Button(ventana, text=button_text, bg="white", font=("calibri", 20))
    button.grid(row=row_val, column=col_val, sticky="nsew")
    buttons.append(button)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

    
boton1 = Button(ventana, text="1", width=5, height=2, command=lambda: click_boton(1), state=DISABLED, relief=SUNKEN, borderwidth=4, font=("Arial", 12, "bold"))
boton2 = Button(ventana, text="2", width=5, height=2,  state=DISABLED, command = lambda: click_boton(2), relief=SUNKEN, borderwidth=4, font=("Algerian", 12, "bold"))
boton3 = Button(ventana, text="3", width=5, height=2,  state=DISABLED, command = lambda: click_boton(3), relief=SUNKEN, borderwidth=4,font=(" Roman", 12, "bold"))
boton4 = Button(ventana, text="4", width=5, height=2,  state=DISABLED,command = lambda: click_boton(4), relief=SUNKEN, borderwidth=4, font=("Algerian", 12, "bold"))
boton5 = Button(ventana, text="5", width=5, height=2, state=DISABLED, command = lambda: click_boton(5), relief=SUNKEN, borderwidth=4,font=(" Roman", 12, "bold"))
boton6 = Button(ventana, text="6", width=5, height=2, state=DISABLED, command = lambda: click_boton(6), relief=SUNKEN, borderwidth=4, font=("Algerian", 12, "bold"))
boton7 = Button(ventana, text="7", width=5, height=2, state=DISABLED, command = lambda: click_boton(7), relief=SUNKEN, borderwidth=4, font=(" Roman", 12, "bold"))
boton8 = Button(ventana, text="8", width=5, height=2, state=DISABLED, command = lambda: click_boton(8), relief=SUNKEN, borderwidth=4, font=("Arial", 12, "bold"))
boton9 = Button(ventana, text="9", width=5, height=2, state=DISABLED, command = lambda: click_boton(9), relief=SUNKEN, borderwidth=4, font=("Arial", 12, "bold"))
boton0 = Button(ventana, text="0", width=5, height=2, state=DISABLED, command = lambda: click_boton(0), relief=SUNKEN, borderwidth=4, font=("Algerian", 12, "bold"))

boton_borrar = Button(ventana, text="AC", width=5, height=2,state=DISABLED, command = lambda: borrar(), bg='blue', fg='white')
boton_Parentesis1 = Button(ventana, text="(", width=5, height=2, state=DISABLED, command = lambda: click_boton("("), bg='red', fg='white')
boton_Parentesis2 = Button(ventana, text=")", width=5, height=2, state=DISABLED, command = lambda: click_boton(")"), bg='red', fg='white')
boton_Punto = Button(ventana, text=".", width=5, height=2, state=DISABLED, command = lambda: click_boton("."), bg='red', fg='white')

boton_div = Button(ventana, text="/", width=5, height=2, state=DISABLED, command = lambda: click_boton("/"), bg='orange', fg='white')
boton_mult = Button(ventana, text="x", width=5, height=2, state=DISABLED, command = lambda: click_boton("*"), bg='orange', fg='white')
boton_suma = Button(ventana, text="+", width=5, height=2, state=DISABLED, command = lambda: click_boton("+"), bg='orange', fg='white')
boton_resta = Button(ventana, text="-", width=5, height=2, state=DISABLED, command = lambda: click_boton("-"), bg='orange', fg='white')
boton_igual = Button(ventana, text="=", width=5, height=2, state=DISABLED, command = lambda: opercacion(), bg='orange', fg='white')

boton_borrar.grid(row =1, column= 0, padx = 5, pady = 5)
boton_Parentesis1.grid(row =1, column= 1, padx = 5, pady = 5)
boton_Parentesis2.grid(row =1, column= 2, padx = 5, pady = 5)
boton_div.grid(row =1, column= 3, padx = 5, pady = 5)

boton7.grid(row =2, column= 0, padx=5, pady =5)
boton8.grid(row =2, column= 1, padx=5, pady =5)
boton9.grid(row =2, column= 2, padx=5, pady =5)
boton_mult.grid(row =2, column= 3, padx=5, pady =5)

boton4.grid(row =3, column= 0, padx=5, pady =5)
boton5.grid(row =3, column= 1, padx=5, pady =5)
boton6.grid(row =3, column= 2, padx=5, pady =5)
boton_suma.grid(row =3, column= 3, padx=5, pady =5)

boton1.grid(row =4, column= 0, padx=5, pady =5)
boton2.grid(row =4, column= 1, padx=5, pady =5)
boton3.grid(row =4, column= 2, padx=5, pady =5)
boton_resta.grid(row =4, column= 3, padx=5, pady =5)

boton0.grid(row =5, column= 0, padx=5, pady =5)
boton_Punto.grid(row =5, column= 2, padx=5, pady =5)
boton_igual.grid(row =5, column= 3, padx=5, pady =5)

boton_binario = Button(ventana, text="Binario", width=5, height=2, state=DISABLED, command=decimal_a_binario)
boton_binario.grid(row=6, column=0, padx=5, pady=5)

boton_borrar_caracter = Button(ventana, text="C", width=5, height=2,state=DISABLED, command=borrar_caracter, bg='red', fg='white')
boton_borrar_caracter.grid(row=5, column=1, padx=5, pady=5)

boton_ON= Button(ventana, text = "ON" , width=5, height=2, command=lambda:switchButtonState())
boton_ON.grid(row=6, column=2, padx=5, pady=5)

ventana.mainloop()