from tkinter import *
from tkinter import Tk
from tkinter import messagebox


corVerde = "#00FF00"
corBranca = "#fff"
corLaranja = "#da4f1c"
corPreta = "#000000"
corRoxo = "#8A2BE2"

def Aviso():
    entry_value = email2.get()

    if entry_value:
        messagebox.showinfo ("Aviso", 'Usuário Cadastrado!')
    else:
        messagebox.showinfo("Aviso", 'Usuário e senha inválidos!')


CadastraJan = Tk()
CadastraJan.resizable(width=FALSE, height=FALSE)
CadastraJan.title("Cadastre-se")
CadastraJan.configure(background=corBranca)
CadastraJan.geometry("500x350")

global email2

frame_cima = Frame(CadastraJan, width=500, height=50, relief='flat', bg=corRoxo)
frame_cima.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

    # configurando o frame cima
cadastrar = Label(frame_cima, text='CADASTRO', anchor=NE, font=("Arial", 20, "bold"), bg=corRoxo, fg=corBranca, padx=3, pady=5)
cadastrar.place(x=170, y=3)

emailCad = Label(CadastraJan, text='E-mail', font=("Arial", 15, "bold"), fg=corRoxo, bg=corBranca)
emailCad.place(x=85, y=130)

email2 = Entry(CadastraJan, width=40, bg=corBranca, fg=corRoxo)
email2.place(in_=emailCad, x=88, y=0, height=30)

senhaCad = Label(CadastraJan, text='Senha', font=("Arial", 15, "bold"), fg=corRoxo, bg=corBranca)
senhaCad.place(x=85, y=180)


senha2 = Entry (CadastraJan, width=40, bg=corBranca, fg=corRoxo)
senha2.place(in_=senhaCad, x=88, y=0, height=30)

botaoCad = Button(CadastraJan, width=15, text='Cadastrar', font=("Arial", 10, "bold"), fg=corBranca, bg=corRoxo, command = Aviso)
botaoCad.place(x=290, y=250)

CadastraJan.mainloop()