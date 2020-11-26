from tkinter import *
from tkinter import ttk

import calculator

class MainApp(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.title ('Calculadora Romanos') #Titulo de la pantalla
        
        self.calculator = calculator.Calculator(self)
        self.calculator.pack(side = TOP)
                   
            

        # Creacion de botones sin crear la clase Calcbutton.
        """
        self.calcbotonC = ttk.Frame(self, width = 136, height = 50) # Creamos el frame del boton
        btn = ttk.Button (self.calcbotonC, text = 'C') # Creamos el boton y el texto que contiene
        self.calcbotonC.pack_propagate (False) # Hacemos que el boton se ajuste a la ventana del frame creado
        btn.pack (side = TOP, fill = BOTH, expand = True) # Mandamos el boton arriba, y que rellene el frame
        self.calcbotonC.grid (column = 0, row=1, columnspan = 2) # Cogemos el frame (ya conteniendo el boton) y lo subimos arriba

        self.calcbotonCs = ttk.Frame(self, width = 68, height = 50) # Creamos el frame del boton
        btn = ttk.Button (self.calcbotonCs, text = '+/-') # Creamos el boton y el texto que contiene
        self.calcbotonCs.pack_propagate (False) # Hacemos que el boton se ajuste a la ventana del frame creado
        btn.pack (side = TOP, fill = BOTH, expand = True)
        self.calcbotonCs.grid (column=2, row=1)

        self.calcbotondiv = ttk.Frame(self, width = 68, height = 50) # Creamos el frame del boton
        btn = ttk.Button (self.calcbotondiv, text = '/') # Creamos el boton y el texto que contiene
        self.calcbotondiv.pack_propagate (False) # Hacemos que el boton se ajuste a la ventana del frame creado
        btn.pack (side = TOP, fill = BOTH, expand = True)
        self.calcbotondiv.grid (column=3, row=1)
        """

        """
        def procesar ():
            if num -> pon num en display
            if + -> suma
            if - -> resta
            if X -> multiplica
            if / -> divide
        
        """


if __name__ == '__main__':   
    app = MainApp()
    app.mainloop ()