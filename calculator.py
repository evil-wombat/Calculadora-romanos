from tkinter import *
from tkinter import ttk

WIDTH = 68
HEIGHT = 50

lista_botones = ('C', '+/-', '%', '/', '7', '8', '9', 'X', '4', '5', '6', '-', '1', '2', '3', '+' , '0', ',', '=')
lista_botones2 = (('C',1), ('+/-',1), ('%',1), ('/',1), ('7',1), ('8',1), ('9',1), ('X',1), ('4',1), ('5',1), ('6',1), ('-',1), ('1',1), ('2',1), ('3',1), ('+' ,1), ('0',2), (',',1), ('=',1))
dbotones = [
    {
        'text': 'C',
        'r': 0,
        'c': 1,
    },
    {
        'text': '+/-',
        'r': 0,
        'c': 2,
    },
    {
        'text': '÷',
        'r': 0,
        'c': 3,
    },
    {
        'text': '7',
        'r': 1,
        'c': 0,
    },
    {
        'text': '8',
        'r': 1,
        'c': 1,
    },
    {
        'text': '9',
        'r': 1,
        'c': 2,
    },
    {
        'text': 'x',
        'r': 1,
        'c': 3,
    },
    {
        'text': '4',
        'r': 2,
        'c': 0,
    },
    {
        'text': '5',
        'r': 2,
        'c': 1,
    },
    {
        'text': '6',
        'r': 2,
        'c': 2,
    },
    {
        'text': '-',
        'r': 2,
        'c': 3,
    },
    {
        'text': '1',
        'r': 3,
        'c': 0,
    },
    {
        'text': '2',
        'r': 3,
        'c': 1,
    },
    {
        'text': '3',
        'r': 3,
        'c': 2,
    },
    {
        'text': '+',
        'r': 3,
        'c': 3,
    },
    {
        'text':'0',
        'r':4,
        'c':0,
        'w': 2
    },
    {
        'text': ',',
        'r': 4,
        'c': 2,
    },
    {
        'text': '=',
        'r': 4,
        'c': 3,
    },
]

# Command no acepta una función con parametros, solo una funcion vacia. Por lo que creamos una función lambda.
def retornaCaracter (tecla):
    print (tecla)
    

class Display (ttk.Frame):

    def  __init__ (self, parent):
        ttk.Frame.__init__(self, parent, width = WIDTH*4, height = HEIGHT)
        self.pack_propagate (0)
        s = ttk.Style ()
        s.theme_use('alt')

        self.label = ttk.Label (self, text = '0', anchor = E, background = 'black', foreground = 'white', font = 'Helvetica 36')
        self.label.pack (side = TOP, fill = BOTH, expand = True)
    
    def refresh (self, texto):
        self.label.config (text = texto)

class CalcButton (ttk.Frame):
    def __init__ (self, parent, text, command = None, width = 1, height = 1):
        ttk.Frame.__init__(self, parent, width = width*WIDTH, height = height*HEIGHT)
        self.pack_propagate (0)
        s = ttk.Style()
        s.theme_use ('alt')

        ttk.Button (self, text = text, command = lambda: command(text)).pack (side = TOP, fill = BOTH, expand = True)


class Keyboard_Adrian (ttk.Frame):
    def __init__ (self, parent, command):
        ttk.Frame.__init__(self, parent, width = 4*WIDTH, height = 5*HEIGHT)
        self.pack_propagate (0)
        s = ttk.Style()
        s.theme_use ('alt')

        row = 0
        column = 0
        for boton in lista_botones:
            
            if boton != '0':    
                botonC = CalcButton (self, boton, command = command)
                botonC.grid (row = row, column = column)
                column += 1
            
                if column > 3:
                    row +=1
                    column = 0
            else:
                boton0 = CalcButton (self, boton, width = 2, command = command)
                boton0.grid (row = row, column = column, columnspan = 2)
                column += 2

class Keyboard2 (ttk.Frame):
     def __init__(self, parent, command):
        ttk.Frame.__init__(self, parent, width=WIDTH*4, height=HEIGHT*5)
        self.pack_propagate(0)
        s = ttk.Style()
        s.theme_use('alt')

        coordenadas = []
        for fila in range(5):
            for columna in range(4):
                coordenadas.append((fila, columna))

        k = 0
        for tecla, ancho in lista_botones2:
            boton = CalcButton(self, tecla, width=ancho)
            boton.grid(row=coordenadas[k][0], column=coordenadas[k][1], columnspan=ancho)
            k += ancho
      
class Keyboard_con_diccionario(ttk.Frame):
    def __init__(self, parent, command):
        ttk.Frame.__init__(self, parent, width=WIDTH*4, height=HEIGHT*5)
        self.pack_propagate(0)
        s = ttk.Style()
        s.theme_use('alt')

        for boton in dbotones:
            w = boton.get('w', 1)
            h = boton.get('h', 1)

            btn = CalcButton(self, boton['text'],width=w, height=h, command = command)
            btn.grid(row=boton['r'], column=boton['c'], columnspan=w, rowspan=h)

class Calculator (ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=WIDTH*4, height=HEIGHT*6)
        self.pack_propagate(0)
        s = ttk.Style()
        s.theme_use('alt')

        self.display = calculator.Display (self)
        self.display.pack (side = TOP, fill = BOTH, expand = True)

        self.teclado = calculator.Keyboard_con_diccionario(self, self.display.refresh)
        self.teclado.pack (side = TOP)

    def gestiona_calculos (self, tecla):
         
        """
         OP1
         OP2
         operacion
         resultado
        """
        pass