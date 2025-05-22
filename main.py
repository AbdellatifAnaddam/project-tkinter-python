from tkinter import *
from tkinter import messagebox
import csv
import os
def Home():
    def Ajouter():
        if os.path.exists('stock.csv') and (input_1.get()!= "" and input_2.get()!= "" and input_3.get()!= "" and input_4.get()!= "" and input_5.get() != ""):
            with open('stock.csv','a',newline="\n") as file:
                csv.writer(file).writerow([input_1.get(), input_2.get(), input_3.get(), input_4.get(), input_5.get()])
            [input_1.delete(0,END), input_2.delete(0,END), input_3.delete(0,END), input_4.delete(0,END), input_5.delete(0,END)]
            messagebox.showinfo('Succes','valide information')
        elif not os.path.exists('stock.csv'):
            with open('stock.csv','w',newline="\n") as file:
                csv.writer(file).writerow(['Nom', 'Taille', 'Couleur', 'Marque', 'Prix'])
                csv.writer(file).writerow([input_1.get(), input_2.get(), input_3.get(), input_4.get(), input_5.get()])
            [input_1.delete(0,END), input_2.delete(0,END), input_3.delete(0,END), input_4.delete(0,END), input_5.delete(0,END)]
            messagebox.showinfo('Succes','valide information')
        else:
            messagebox.showerror("Errur","Remplir toutes les champs")

    def Effacer():
        [input_1.delete(0,END), input_2.delete(0,END), input_3.delete(0,END), input_4.delete(0,END), input_5.delete(0,END)]

    with open('stock.csv','r') as file:
        read = csv.reader(file,delimiter=',')
        liste = []
        for i in  read:
            liste.append(i)

    def Afficher_tout():
        list.delete(0,END)
        for i in range(1,len(liste)):
            content = "{"+liste[i][0]+"}"+"{"+liste[i][1]+"}"+"{"+liste[i][2]+"}"+"{"+liste[i][3]+"}"+"{"+liste[i][4]+"}"
            list.insert(END,content)
        list.config(height=16)

    def Supprimer():
        N= list.curselection()[0]
        print(N)
        list.delete(list.curselection())
        list.config(height=16)
        liste.pop(N)
        
    def Rechercher():
        if rechercher.get() != "":
            list.delete(0,list.size())
            for j in range(1,len(liste)):
                if liste[j][0] == rechercher.get():
                    list.insert(END,"{"+liste[j][0]+"}"+"{"+liste[j][1]+"}"+"{"+liste[j][2]+"}"+"{"+liste[j][3]+"}"+"{"+liste[j][4]+"}")
        if list.size() == 0 and rechercher.get() != "":
            messagebox.showinfo("Rechercher","Aucun résultat")
            
    window = Tk()
    window.title("Gestion Des Vêtements")
    window.config(bg="white")
    window.geometry('1050x600+100+50')
    window.resizable(False,False)

    label = Label(window,text="Gestion\nDes Vêtements",font=("Arial",20),bg='white')
    label_1 = Label(window,text='Ajouter Un Article',font=("Arial",15),bg='white')
    label.place(x=430,y=0)
    label_1.place(x=120,y=75)

    position_y = [120,170,220,270,320]
    contents_labels =["Nom:","Taille:","Couleur:","Marque:","Prix:"]

    for pos in range(len(position_y)):
        label = Label(window,text=contents_labels[pos],font=("Arial",15),bg='white').place(x=23,y=position_y[pos]+10)
        Frame(width=250,height=1,bg='black').place(x=130,y=position_y[pos]+30)

    input_1 = Entry(window,width=23,border=0,font=('Arial',15),fg='#0D0E0D')
    input_1.place(x=130,y=position_y[0]+5)

    input_2 = Entry(window,width=23,border=0,font=('Arial',15),fg='#0D0E0D')
    input_2.place(x=130,y=position_y[1]+5)

    input_3 = Entry(window,width=23,border=0,font=('Arial',15),fg='#0D0E0D')
    input_3.place(x=130,y=position_y[2]+5)

    input_4 = Entry(window,width=23,border=0,font=('Arial',15),fg='#0D0E0D')
    input_4.place(x=130,y=position_y[3]+5)

    input_5 = Entry(window,width=23,border=0,font=('Arial',15),fg='#0D0E0D')
    input_5.place(x=130,y=position_y[4]+5)

    
    button = Button(window,width=50,height=2,text='Ajouter',bg='#5FD82F',border=0,fg='white',activeforeground='#5FD82F',command=Ajouter)
    button.place(x=28,y=390)
    button_1 = Button(window,width=50,height=2,text='Effacer',bg="#DAC80B",border=0,fg='white',activeforeground='#DAC80B',command=Effacer)
    button_1.place(x=28,y=460)

    rechercher = Entry(window,width=35,font=('Arial',14),fg='#0D0E0D',border=0)
    rechercher.place(x=633,y=75)
    button_2 = Button(window,text="rechercher",bg='#2B82D8',activeforeground='#2B82D8',border=0,height=1,fg='white',command=Rechercher)
    button_2.place(y=78,x=960)
    Frame(window,width=576,height=1,bg='#2B82D8').place(x=447,y=100)

    list = Listbox(window,width=96,bg='white',font=(30),height=16,border=0)
    list.config(height=16)
    list.place(x=446,y=102)
    button_3 = Button(window,text="Supprimer",border=0,height=2,width=25,fg='white',bg='#F12222',activeforeground='#F12222',command=Supprimer)
    button_3.place(x=545,y=530)
    button_4 = Button(window,width=25,text="Afficher Tout",height=2,fg='white',bg='#4BA3B2',border=0,activeforeground='#4BA3B2',command=Afficher_tout)
    button_4.place(x=745,y=530)
        
    window.mainloop()
