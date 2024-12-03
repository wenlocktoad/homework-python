from tkinter import *
from tkinter import messagebox as msb
from gui_util import create_window

window = create_window('demo gui 04', 400, 300)

lbl_a = Label(window, text='a:')
lbl_a.grid(row=0, column=0, sticky=E, padx=10, pady=10)

txt_a= Entry(window, width=20)
txt_a.grid(row=0, column=1, sticky=W, padx=10, pady=10, columnspan=4)

lbl_b = Label(window, text='b=')
lbl_b.grid(row=1, column=0, sticky=E,padx=10,pady=10)

txt_b = Entry(window, width=25)
txt_b.grid(row=1, column=0, sticky=E, padx=10,pady=10)

btn_add = Button(window, text='+', width=5, command=btn_add)