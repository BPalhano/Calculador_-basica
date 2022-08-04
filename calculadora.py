import tkinter as tk
import math

import sys
import os

dirpath = os.getcwd()
sys.path.append(dirpath)

if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)


# Map do layout dos botões.
botao_config = {

    "bg": "#242743",
    "fg": "#808080",
    "font": ("Consolas bold", 12),
    "height": "12",
    "width": "7",
    "relief": "flat",
    "activebackground": "#313454"
}

# Digitos especiais que serão importados da biblioteca math
digitos = ["√", "x²", "C", "n!", "sin", "cos",
           "tan", "arcsin", "arccos", "arctan",  "π", "↑", "↓"]

#  Variáveis de apoio para a conversão Rad <-> Deg
deg = 1
inversa_deg = 1
cnt = 0

# Classe Calculadora.


class Calculadora:
    def __init__(self, master):  # Construtor.

        self.master = master

        self.displayframe = tk.Frame(self.master)
        self.displayframe.pack()  # Criar Espaço para Display.

        self.buttonsframe = tk.Frame(self.master)
        self.buttonsframe.pack()  # Criar Espaço para Botões

        self.output = tk.Entry(self.displayframe, width=30, relief="sunken", bd=3, font=(
            "Consolas bold", 17), fg="#c9c9c5", bg="#242742")  # Criar Visor.

        self.output.grid(row=0, column=0)

        self.converte = tk.Button(self.displayframe, botao_config, width=3,
                                  height=0, text="DEG", bg="#e35124", command=self.degreesRadians)  # Criar Conversor Rad <-> Deg

        self.converte.grid(row=0, column=1)

        self.criarbotoes()  # Criar Botões.

    def criarbotoes(self):  # Função de criação e iterações de botões.
        self.botoes = [
            ["√", "x²", "**", "(", ")", "/", "↑"],
            ["sin", "cos", "7", "8", "9", "+", ""],
            ["arcsin", "arccos", "4", "5", "6", "-", "↓"],
            ["tan", "arctan", "1", "2", "3", "*", " "],
            ["n!", "π", ".", "0", "=", "C", " "]
        ]

        for linha in range(len(self.botoes)):
            for coluna in range(len(self.botoes[linha])):
                # Recebe o texto de cada botão.
                texto = self.botoes[linha][coluna]

                b = tk.Button(self.buttonsframe, botao_config, text=texto,
                              command=lambda x=texto: self.acaoBotoes(x))
                # Função lâmbida faz ação de cada botão usando função.
                b.grid(row=linha, column=coluna)

    def acaoBotoes(self, texto):  # Ação de cada botão.

        global deg
        global inversa_deg
        global cnt

        if texto != "=":  # Se o botão apertado não for a solicitação de resultados.
            if texto not in digitos:  # Se o botão apertado não está contido no vetor digitos.

                # Insira a esquerda do ultimo elemento da tela.
                self.output.insert('end', texto)

            else:  # se estão contido no vetor:
                if texto == "√":
                    try:
                        self.addValor(math.sqrt(float(self.output.get())))
                    except ValueError as e:
                        self.output.delete(0, 'end')
                        self.output.insert('end', 'MATH ERROR')

                elif texto == "↑":
                    self.addValor(math.ceil(float(self.output.get())))

                elif texto == "↓":
                    self.addValor(math.floor(float(self.output.get())))

                elif texto == "n!":
                    self.addValor(math.factorial(float(self.output.get())))

                elif texto == "x²":
                    self.addValor((float(self.output.get()) ** 2))

                elif texto == "C":
                    self.addValor("")

                elif texto == "π":
                    self.addValor(3.14159265359)

                elif texto == "sin":

                    try:
                        self.addValor(math.sin(float(self.output.get())) * deg)
                    except ValueError as e:
                        self.output.delete(0, 'end')
                        self.output.insert('end', 'MATH ERROR')

                elif texto == "cos":
                    try:
                        self.addValor(math.cos(float(self.output.get())) * deg)
                    except ValueError as e:
                        self.output.delete(0, 'end')
                        self.output.insert('end', 'MATH ERROR')

                elif texto == "tan":
                    try:
                        self.addValor(math.tan(float(self.output.get())) * deg)
                    except ValueError as e:
                        self.output.delete(0, 'end')
                        self.output.insert('end', 'MATH ERROR')

                elif texto == "arcsin":
                    try:
                        self.addValor(
                            math.asin(float(self.output.get())) * inversa_deg)
                    except ValueError as e:
                        self.output.delete(0, 'end')
                        self.output.insert('end', 'MATH ERROR')

                elif texto == "arccos":
                    try:
                        self.addValor(
                            math.acos(float(self.output.get())) * inversa_deg)
                    except ValueError as e:
                        self.output.delete(0, 'end')
                        self.output.insert('end', 'MATH ERROR')

                elif texto == "arctan":
                    try:
                        self.addValor(
                            math.atan(float(self.output.get())) * inversa_deg)
                    except ValueError as e:
                        self.output.delete(0, 'end')
                        self.output.insert('end', 'MATH ERROR')

        else:  # Se não está contido em digitos e é a solicitação de resultados:

            try:
                self.addValor(eval(self.output.get()))  # Resultado.

            except ZeroDivisionError or math.isnan as e:
                self.output.delete(0, 'end')
                self.output.insert('end', 'MATH ERROR')

    # Função para executar as iterações matemáticas de cada botão.
    def addValor(self, valor):

        self.output.delete(0, 'end')
        self.output.insert('end', valor)

    def degreesRadians(self):  # Função conversora de radianos.
        global deg
        global inversa_deg
        global cnt

        if(cnt == 0):
            deg = math.pi/180
            inversa_deg = 180 / math.pi
            self.converte['text'] = "RAD"
            cnt = 1

        else:
            deg = 1
            inversa_deg = 1
            self.converte['text'] = "DEG"
            cnt = 0


# Execução.
raiz = tk.Tk()
Calculadora(raiz)
raiz.mainloop()


"""
Cada conjunto de try/except/else tem função de testar possível erro matemático no processo de construção da expressão.

"""
