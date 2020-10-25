from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("CLOCK")


def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)


lbl = Label(root, font=('italic', 40, 'bold'),
            background='purple',
            foreground='black')
lbl.pack(anchor='center')
time()
mainloop()
