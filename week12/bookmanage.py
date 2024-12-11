from tkinter import *
from tkinter import messagebox as msb
from gui_util import create_window, run

window=create_window('demo checkbox', 500,300)
lbl_book=Label(window,text='select books:')
lbl_book.grid(row=0,column=0,padx=5,pady=5,sticky=W)
lst_books= Listbox(window,selectmode=SINGLE,width=38,height=10,exportselection=0)
lst_books.grid(row=1,column=0,padx=5,pady=5,sticky=W,rowspan=4,columnspan=2)
