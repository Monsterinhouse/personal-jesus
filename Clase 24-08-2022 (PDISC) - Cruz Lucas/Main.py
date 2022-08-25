from ast import Delete
from cgitb import text
from distutils.cmd import Command
import sqlite3
import tkinter
from cProfile import label
from tkinter import *
from tkinter import ttk
from tokenize import String
from turtle import width

root = Tk()
root.geometry("600x400")
root.title("Query Aplication")

# ALL THINGS BBDD RELATED
conex = sqlite3.connect("pdisc.db")
cursor = conex.cursor()

# FUNCIONES
nombre = StringVar()
apellido = StringVar()
dni = IntVar()

def dataentry() :
    cursor.execute (
        '''
        CREATE TABLE IF NOT EXISTS InfoTotalmenteImportante (
            nombre VARCHAR (30), apellido VARCHAR (20), dni INTEGER (8)
        )
        '''
    )

    cursor.execute("INSERT INTO InfoTotalmenteImportante (nombre, apellido, dni) VALUES (?, ?, ?)", (nombre.get(), apellido.get(), dni.get()))
    conex.commit()
   

noteb = ttk.Notebook(root)
noteb.pack(pady=10, padx=10, expand=True)

# FRAMES

frame1 = Frame(noteb, width=500, height=280)
frame2 = Frame(noteb, width=500, height=280)
frame1.pack (fill='both', expand=True)
frame2.pack (fill='both', expand=True)

# CONTENIDO DE FRAMES

labframe = LabelFrame(frame1, text='Data Entry', fg='blue', padx=5, pady=5)
labframe.grid(column=0, row=0, padx=15, pady=10)
f1l1 = Label(labframe, text='Nombre').grid(column=0, row=1)
f1l2 = Label(labframe, text='Apellido').grid(column=0, row=2)
f1l3 = Label(labframe, text='DNI').grid(column=0, row=3)
f1e1 = ttk.Entry(labframe, textvariable=nombre).grid(column=1, row=1)
f1e2 = ttk.Entry(labframe, textvariable=apellido).grid(column=1, row=2, pady=5)
f1e3 = ttk.Entry(labframe, textvariable=dni).grid(column=1, row=3)
f1b1 = ttk.Button(labframe, text='Ingresar', command=dataentry).grid(column=1, row=4, pady=5)

labframe = LabelFrame(frame2, text='Datos', fg='blue', padx=5, pady=5)
labframe.grid(column=0, row=0, padx=15, pady=10)

# TREELIST

columnas = ["Nombre", "Apellido", "DNI"]
data_table = ttk.Treeview(labframe)
data_table['columns'] = tuple(columnas)
data_table.column("#0", width=0,  stretch=NO)

def view() :
    cursor.execute("SELECT * FROM InfoTotalmenteImportante")
    rows = cursor.fetchall()
    for row in rows: 
        print (row)
        data_table.insert("", END, values=row)

for field in columnas:
    data_table.column(field, anchor=CENTER, width=80)
    data_table.heading(field, text=field.upper(), anchor=CENTER)
data_table.grid(column=1, row=4)

b2 = ttk.Button(labframe, text="Revisar Registros", command=view)
b2.grid(column=2, row=4, padx=5)

# AÑADIR FRAMES

noteb.add(frame1, text='Carga de Datos')
noteb.add(frame2, text='Consulta de Datos')

root.mainloop()