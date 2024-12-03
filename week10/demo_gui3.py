from tkinter import *
from tkinter import messagebox as mb
from gui_util import create_window

def btn_invoice_click():
    product = txt_product.get()
    price= float(txt_price.get())


window = create_window('demo_gui3',800, 900)
    