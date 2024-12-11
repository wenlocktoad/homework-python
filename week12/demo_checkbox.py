from tkinter import *
from tkinter import messagebox as msb
from gui_util import create_window, run

window = create_window('demo checkbox', 400, 200)

def calculatebill():
    total=0
    if phone_var.get()==1:
        total+=2000
    elif phone_var.get()==2:
        total+=1500
    elif phone_var.get()==3:
        total+=2500    
    
    if pen_var.get()==True:
        total+=30
    if cover_var.get()==True:
        total+=15
    if film_var.get()==True:
        total+=5        
    lbl_bill.config(text=f'Total bill: ${total}')    

lbl_phone= Label(window, text='Select a phone')
lbl_phone.grid(row=0,column=0,padx=5,pady=5,sticky=W)

lbl_accessories=Label(window, text='Select accessories:')
lbl_accessories.grid(row=0,column=1,padx=5,pady=5,sticky=W)

phone_var= IntVar()

rd_phone16=Radiobutton(window,text='iphone 16 ($2000)',variable=phone_var,value=1,command=calculatebill)
rd_phone16.grid(row=1,column=0,padx=5,pady=5,sticky=W)

rd_phone15=Radiobutton(window,text='iphone 15 ($1500)',variable=phone_var,value=2,command=calculatebill)
rd_phone15.grid(row=2,column=0,padx=5,pady=5,sticky=W)

rd_samsung=Radiobutton(window,text='samsung fold 6 ($2500)',variable=phone_var,value=3,command=calculatebill)
rd_samsung.grid(row=3,column=0,padx=5,pady=5,sticky=W)

pen_var=BooleanVar()
chk_pen=Checkbutton(window, text='pen ($30)', variable=pen_var,command=calculatebill)
chk_pen.grid(row=1,column=1,padx=5,pady=5, sticky=W)

cover_var=BooleanVar()
chk_cover=Checkbutton(window,text='cover ($15)',variable=cover_var,command=calculatebill)
chk_cover.grid(row=2,column=1,padx=5,pady=5,sticky=W)

film_var=BooleanVar()
chk_film=Checkbutton(window,text='film ($5)',variable=film_var,command=calculatebill)
chk_film.grid(row=3,column=1,padx=5,pady=5,sticky=W)

lbl_bill=Label(window, text='total bill: $0')
lbl_bill.grid(row=4,column=0,padx=5,pady=5,sticky=W,columnspan=2)

run(window)