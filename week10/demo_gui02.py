from tkinter import *
from tkinter import messagebox as msb

def btn_show_vietnamese():
    lbl_vietnam= Label(window, text='Ỉa 1 lần bạn sẽ bị cười,Ỉa 10 lần bạn sẽ bị đặt tên là Ỉa,Ỉa 100 lần mọi người trong lớp bắt đầu sợ và xa lánh,Ỉa 1000 lần trong mắt mọi người chỉ còn 1 sự sợ hãi, không ai dám trêu chọc vì họ biết rất có thể,hôm sau chỗ họ sẽ có 1 bãi cứt')

window = Tk()
window.title ('demo gui 02') 
window.geometry('500x200')
lbl_hello = Label(window, text='hello, world')
lbl_hello.grid(row=0, column=0, sticky=W)

btn_vietnam = Button(window, text='vietnamese,')
btn_vietnam.grid(row=0, column=1, sticky=W)
btn_french= Button(window, text='Bonjour, je suis un Français très fier de mon pays. Je n’aime pas les Anglais, les Allemands, lesAméricains ou les autres pays qui nous ont envahi ou insulté.',)
btn_french.grid(row=0, column=2,sticky=W)


window.mainloop()