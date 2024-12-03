from tkinter import *
from tkinter import messagebox as msb

def btn_ok_click():
    msb.showinfo('ok', 'you clicked ok button')

def btn_show_python_click():
    #get text from label hello
    s1= lbl_hello['text']
    #gettext frim label python
    s2= lbl_python['text']
    #swap text
    lbl_hello['text'] =s2
    lbl_python['text'] =s1

#create window
window = Tk()
window.title ('demo gui 01') #set title of window
window.geometry('300x200') #set dimension with x height
# create widgets 
lbl_hello = Label(window, text='hello, world',)
#place widget on wndow 
lbl_hello.grid(row=0, column=0, sticky=W)
#run the window 
lbl_python = Label(window, text='python is fun')
lbl_python.grid(row=1, column=1, sticky=E)

btn_ok = Button(window, text='ok', command=btn_ok_click)
btn_ok.grid(row=0, column=1, sticky=E)

btn_pyhton = Button(window, text='show python', command=btn_show_python_click)
btn_pyhton.grid(row=0, column=2, sticky=W)
window.mainloop()