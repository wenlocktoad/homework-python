from tkinter import *
from tkinter import messagebox as msb
from gui_util import create_window, run

window = create_window('demo radio', 400, 200)

def btn_buy_click():
    movie = txt_movie.get()
    price=float(txt_price.get())
    vip = vip_var.get()
    if vip == 1:
        price *=0.9 

lbl_movie = Label(window, text='Moive')
lbl_movie.grid(row=0, column=1, padx=5, pady=5, sticky=E)

txt_movie = Entry(window, width=15)
txt_movie.grid(row=0, column=1, padx=5, pady=5, sticky=W, columnspan=2)

lbl_price=Label(window, text='Price')
lbl_price.grid(row=1, column=0, padx=5, pady=5, sticky=E)

txt_price=Entry(window, width=15)
txt_price.grid(row=1, column=1, padx=5, pady=5, sticky=W, columnspan=2)

lbl_vip=Label(window, text='VIP')
lbl_vip.grid(row=2, column=0, padx=5, pady=5, sticky=E)

vip_var= IntVar()
vip_var.set(0)
rd_yes = Radiobutton(window, text='yes', value=1, variable=vip_var)
rd_yes.grid(row=2, column=1, padx=5, pady=5, sticky=W)

rd_no = Radiobutton(window, text='no', value=0)
rd_no.grid(row=2,column=2,padx=5,pady=5,sticky=W)

btn_buy = Button(window, text='buy',width=15, command=btn_buy_click)
btn_buy.grid(row=3, column=1, padx=5, pady=5, sticky=W, columnspan=2)

run(window)