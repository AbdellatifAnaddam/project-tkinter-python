from tkinter import *
from tkinter import messagebox
import main

window = Tk()
def focusin(event):
    Username.delete(0,END)
def focusout(event):
    if Username.get() == '':
        Username.insert(0,'Username')

def focusin_1(event):
    Password.delete(0,END)
def focusout_1(event):
    if Password.get() == '':
        Password.insert(0,'Password')

def verification():
    if Username.get() == 'Admin' and Password.get() == '12345':
        window.destroy()
        main.Home()
    elif(Username.get()!='Admin' and Password.get() == '12345') or (Username.get() =='Admin' and Password.get() != '12345') or (Username.get() !='Admin' and Password.get() != '12345'):
        messagebox.showerror('Error','invalid information')

window.geometry('1050x600+100+50')
window.config(bg='#fff')
window.resizable(False,False)
image_back = PhotoImage(file="background.png")
label_back = Label(window,image=image_back,width=1150,height=1100)
label_back.pack()
label_title = Label(window,text="Gestion\nDes Vêtements",font=(40),fg='black',).place(x=425,y=130)
log = Frame(window,bg='#fff',width=350,height=350,padx=30).place(x=323,y=230)
label_frame = Label(log, text="Login",font=(100),fg='black',bg='white').place(x=470,y=250)

Username = Entry(log,width=25,font=(11),border=0,fg='#393838')
Username.place(x=360,y=350)
Username.insert(0,'Username')
frame = Frame(log,width=280,height=1,bg='black').place(x=355,y=375)
Username.bind('<FocusIn>',focusin)
Username.bind('<FocusOut>',focusout)

Password = Entry(log,width=25,font=(11),border=0,fg='#393838',show='•')
Password.place(x=360,y=435)
Password.insert(0,'Password')
frame = Frame(log,width=280,height=1,bg='black').place(x=355,y=460)
Password.bind('<FocusIn>',focusin_1)
Password.bind('<FocusOut>',focusout_1)

buttom = Button(frame, width=39,height=2,text='Login',bg='white',fg='black',activebackground='white',command=verification).place(x=355,y=510)
window.mainloop()