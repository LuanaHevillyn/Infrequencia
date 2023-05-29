from tkinter import *
from tkinter import ttk
from tkinter import messagebox

corRoxo = "#8A2BE2"

def inserir():
    if vnmr.get()=="" or vnome.get()=="" or vpres.get()=="":
        messagebox.showinfo(title="ERRO", message="digite todos os dados")
        return
    tv.insert("","end", values=(vnmr.get(), vnome.get(), vpres.get(), vturno.get()))
    vnmr.delete(0, END)
    vnome.delete(0, END)
    vpres.delete(0, END)
    vturno.delete(0, END)
    vnmr.focus()
    
def deletar():
    try:
        itemSelecionado = tv.selection()[0]    
        tv.delete(itemSelecionado)
    except:
         messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser deletado")
    
    
def obter():
    try: 
        itemSelecionado = tv.selection()[0]
        valores= tv.item(itemSelecionado, "values")
        print("ID......: " + valores[0])
        print("Nome......: " + valores[1])
        print("Presente......: " + valores[2])
        print("Turno......: " + valores[3])
    except:
        messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser mostrado")
        
app = Tk()
app.title("Sistema Infrequencia")
app.geometry('550x350')


lbnmr =Label(app, text="Número")
vnmr= Entry(app)

lbnome=Label(app, text="Nome")
vnome= Entry(app)

lbpres=Label(app, text="Presença")
vpres = Entry(app)

lbturno=Label(app, text="Turno")
vturno = Entry(app)

tv = ttk.Treeview(app, columns=('numero', 'nome', 'presente', 'turno'), show='headings')
tv.column('numero', minwidth=0, width=60)
tv.column('nome', minwidth=0, width=250)
tv.column('presente', minwidth=0, width=100)
tv.column('turno', minwidth=0, width=100)


tv.heading('numero', text="Número")
tv.heading('nome', text="Nome")
tv.heading('presente', text="Presença")
tv.heading('turno', text="Turno")

btn_inserir = Button(app, text="Inserir", command= inserir)
btn_deletar = Button(app, text="Deletar", command= deletar)
btn_obter = Button(app, text="Obter", command= obter)

lbnmr.grid(column=0, row=0, stick='w')
vnmr.grid(column=0, row=1)

lbnome.grid(column=1, row=0, stick='w')
vnome.grid(column=1, row=1)

lbpres.grid(column=2, row=0, stick='w')
vpres.grid(column=2, row=1, stick='w')

lbturno.grid(column=3, row=0, stick='w')
vturno.grid(column=3, row=1)

tv.grid(column=0, row=3, columnspan=4, pady=5)

btn_inserir.grid(column=0, row=4)
btn_deletar.grid(column=1, row=4)
btn_obter.grid(column=2, row=4)

app.mainloop()