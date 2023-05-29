import tkinter as tk
import tkinter.ttk as ttk

class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.set_widgets()

    def set_widgets(self):
        # Inicia o Treeview com as seguintes colunas:
        self.dataCols = ('N°', 'Aluno', 'Faltas')
        self.tree = ttk.Treeview(columns=self.dataCols, show='headings')
        self.tree.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)

        self.tree.column("N°", minwidth=100)
        self.tree.column("Aluno", width=400, minwidth=500)
        self.tree.column("Faltas", width=150, minwidth=150)
        
        # Barras de rolagem
        ysb = ttk.Scrollbar(orient=tk.VERTICAL, command=self.tree.yview)
        self.tree['yscroll'] = ysb.set
        ysb.grid(row=0, column=1, sticky=tk.N + tk.S)

        # Define o textos do cabeçalho (nome em maiúsculas)
        for c in self.dataCols:
            self.tree.heading(c, text=c.title())

        # Dados:
        self.data = [
            ('01', 'Aila Vitória Braga da Silva',1), 
            ('02', 'Alex Moabe Ribeiro de Sousa',2),
            ('03','Andressa da Silva Matos',3),
            ('04','Ângelo Gabriel Vieira de Oliveira',4),
            ('05','Ashley Darwin de Souza Duarte',5),
            ('06','Bruno Henrique do Nascimento Firmino',6),
            ('07','Cauã Roberto de Souza',7),
            ('08','Cayo Madson Cardoso de Vasconcelos',8),
            ('09','Emanoell Edvan Souza da Silva',9),
            ('10','Eric do Nascimento Sousa Diniz',10),
            ('11','Fabíola Xavier FerreiraFabíola Xavier Ferreira',11),
            ('12','Felipe Freitas Vieira',12),
            ('13','Gabriel Holanda de Freitas',13),
            ('14','Guilherme Dimitri Monteiro de Brito',14),
            ('15','Heloiza Duarte Verissimo',15),
            ('16','Igor Dantas Soares',16),
            ('17','Israel do Monte Silva',17),
            ('18','Jemily Aguiar do Nascimento',18),
            ('19','Jennifer Silva Carvalho',19),
            ('20','João Victor Soares Serafim',20),
            ('21','Joinkson Laneo Moraes Nascimento',21),
            ('22','Josiel Sousa Benvindo',22),
            ('23','Juliana Ramos Lopes',23),
            ('24','Lara Evelyn de Sousa Pinto',24),
            ('25','Levi Martins Galvão',25),
            ('26','Liana Kelly Melo Silva',26), 
            ('27','Luana Hevillyn Morais da Silva',27),
            ('28','Lywan Riquelme de Oliveira Maia',28),
            ('29','Maria Eduarda Castro dos Santos',29),
            ('30','Pedro Gabriel Costa Barbosa',30),
            ('31','Pedro Lucas Portela Carlos',31),
            ('32','Raul Ramos Mendes',32),
            ('33','Samuel Maciel Paiva Neto',33),
            ('34','Sarah Vitoria Castro Costa',34),
            ('35','Victor Eduardo Evangelista da Silva',35),
            ('36','Victor Gutierrez Nunes Cavalcanti',36),
            ('37','Victória Ketley de Oliveira do Nascimento',37),
            ('38','Vinnícius Aráujo Sousa',38)
        
        ]

        # Insere cada item dos dados
        for item in self.data:
            self.tree.insert('', 'end', values=item)
            
            

if __name__ == '__main__':
    root = tk.Tk()

    app = Application(master=root)
    app.mainloop()