from mostrarGraficoEdad import mostrarGraficoEdad
from mostrarGraficoEdadPrediccion import mostrarGraficoEdadPrediccion

import tkinter
from tkinter import *
from tkinter import ttk


def main():
	global screen
	global edad_entry
	prediccon = False
	screen = tkinter.Tk()
	screen.title("Inicio")
	screen.geometry("300x200")

	tkinter.Label(screen, text="Ingrese una edad para mostrar el grafico", font=("Arial", 15)).pack()
	edad_entry = tkinter.Entry(screen)
	edad_entry.pack()
	tkinter.Label(screen, text="").pack()

	tkinter.Button(screen, text="Mostrar Grafico", width=20, height=2, command=mostrarGrafico).pack()
	tkinter.Label(screen, text="").pack()
	tkinter.Button(screen, text="Mostrar Grafico con Prediccion", width=20, height=2, command=mostrarGraficoPrediccion).pack()
	screen.mainloop()

def mostrarGrafico():
	edad = int(edad_entry.get())
	mostrarGraficoEdad(edad)

def mostrarGraficoPrediccion():
	edad = int(edad_entry.get())
	mostrarGraficoEdadPrediccion(edad)


if __name__ == '__main__':
	main()
