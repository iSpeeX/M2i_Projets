import tkinter as tk
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.ttk import *
import tkinter.font as font
from view.list import *
from view.create import Create
from classes.renommage import *

Rename = Rename()

data = {} # Variable globale pour le renommage
fenetre = Tk()

class Interface(Frame):
    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=800, height=300, **kwargs)
        fenetre.title('RenIT')
        self.Labels()
        self.Entry()
        self.Buttons()
        self.Menu()
        self.Logo()
        self.Cases()
        self.Listbox()
        self.Foot()

    def Logo(self):
        self.photo = PhotoImage(file="./logo.gif")
        espace_image = Canvas(fenetre, width=160, height=160)
        espace_image.grid(row=1, columnspan=2, column=6, padx=10, pady=10)
        espace_image.create_image(85, 85, image=self.photo)

    def Labels(self):
        tf = font.Font(size=20, family="Colibri", weight="bold")
        tf2 = font.Font()

        titre = Label(fenetre, text="Renommer en lot", font=tf)
        titre.grid(row=0, column=2, columnspan=3, padx=10, rowspan=4)

        nom_rep = Label(fenetre, text="Sélection du répertoire", font=tf2)
        nom_rep.grid(row=5, column=0, padx=10, columnspan=2)

        amorce = Label(fenetre, text="Amorce")
        amorce.grid(row=6, column=1, padx=5)

        prefix = Label(fenetre, text="Préfixe")
        prefix.grid(row=6, column=2, padx=5)

        nomfich = Label(fenetre, text="Nom d'origine")
        nomfich.grid(row=6, column=4, padx=5)

        suffix = Label(fenetre, text="Suffixe")
        suffix.grid(row=6, column=5, padx=5)

        extension = Label(fenetre, text="Extension concernée")
        extension.grid(row=6, column=6, padx=5)

        apartir = Label(fenetre, text="A partir de")
        apartir.grid(row=9, column=1, padx=5)

    def Entry(self):

        self.SVprefixe = StringVar(value=" ")
        self.prefixe = Entry(fenetre, width=20, textvariable=self.SVprefixe)
        self.prefixe.grid(row=7, column=2, padx=5)

        self.SVnomnew = StringVar(value=" ")
        self.nomnew = Entry(fenetre, width=20)
        self.nomnew.grid(row=7, column=4, padx=5)

        self.SVsuffixe = StringVar(value=" ")
        self.suffixe = Entry(fenetre, width=20)
        self.suffixe.grid(row=7, column=5, padx=5)

        self.SVext = StringVar(value=" ")
        self.ext = Entry(fenetre, width=20)
        self.ext.grid(row=7, column=6, padx=5)

        self.SVapartirde = StringVar(value=" ")
        self.apartirde = Entry(fenetre, width=20)
        self.apartirde.grid(row=10, column=1, padx=5)

    def Buttons(self):
        choix = Button(fenetre, text="Choisir...", command=self.browse)
        choix.grid(row=5, column=2, padx=10)

        rename = Button(fenetre, text="Renommer", command=self.recup)
        rename.grid(row=6, column=7, padx=5)

        rename = Button(fenetre, text="Insérer règle", command=self.insert)
        rename.grid(row=7, column=7, padx=5)

    def Cases(self):

        self.nom_o = IntVar()
        self.nom_ori = Checkbutton(fenetre, variable=self.nom_o)
        self.nom_ori.grid(row=6, column=3)

        self.nom_n = IntVar()
        self.nom_new = Checkbutton(fenetre, variable=self.nom_n)
        self.nom_new.grid(row=7, column=3)

    def Listbox(self):
        self.amorceSelect = StringVar()
        self.listamorce = ('Lettre', 'Chiffre')
        self.combo1 = Combobox(fenetre, textvariable=self.amorceSelect, values=self.listamorce)
        self.combo1.grid(row=7, column=1, padx=5, rowspan=2)

    def Menu(self):
        menubar = tk.Menu(fenetre)

        menu1 = Menu(menubar, tearoff=0)
        menu1.add_command(label="Lister", command=List)
        menu1.add_command(label="Créer", command=Create)
        menu1.add_separator()
        menu1.add_command(label="Quitter", command=self.quit)
        menubar.add_cascade(label="Règles", menu=menu1)

        menu2 = Menu(menubar, tearoff=0)
        menu2.add_command(label="A propos", command=self.apropos)
        menubar.add_cascade(label="?", menu=menu2)

        fenetre.config(menu=menubar)

    def Foot(self):
        foot1 = Label(fenetre, text="")
        foot1.grid(column=0, row=11, rowspan=2)

        foot2 = Label(fenetre, text="")
        foot2.grid(column=7, row=13, rowspan=2)

    def recup(self):

        try:
            data["NomRep"] = self.filename
            data["Prefixe"] = self.prefixe.get()
            data["Suffixe"] = self.suffixe.get()
            data["Extension"] = self.ext.get()
            data["Apartirde"] = self.apartirde.get()
            data["NomNew"] = self.nomnew.get()
            data["NomNewCheck"] = self.nom_n.get()
            data["Amorce"] = self.combo1.get()
            Rename.renom(data)
        except:
            showerror("Renommage Impossible", "Il semblerait que l'un des champs ne soit pas correctement remplis.\nVérifiez puis réessayez.")

    def browse(self):
        """
            Fonction pour la sélection du dossier dans lequel se trouvent les ficheirs
        """
        self.filename = askdirectory()
        Label(fenetre, text=self.filename).grid(row=5, column=3, padx=10, columnspan=12)

    def apropos(self):
        """
            Petite fenêtre de la section A Propos du software
        """
        showinfo("A propos", "Nom : RenIT\nVersion : 1.0\nConcepteur : Mathieu FOUCHER")

    def info(self):
        """
            Petite fenêtre sur les fonctions manquantes
        """
        showinfo("Bienvenue sur RenIT", " ")

    def insert(self):
        """
            Injecte les éléments d'une règle sélectionnée dans les champs de texte de la fenetre principale
        """
        self.prefixe.delete(0, END)
        self.prefixe.insert(0, datalist["LPrefixe"])

        self.apartirde.delete(0, END)
        self.apartirde.insert(0, datalist["LApartirde"])

        self.suffixe.delete(0, END)
        self.suffixe.insert(0, datalist["LSuffixe"])

        self.nomnew.delete(0, END)
        self.nomnew.insert(0, datalist["LNomFichier"])

        self.ext.delete(0, END)
        self.ext.insert(0, datalist["LExtension"])

        self.nom_n.set(1)

        if datalist["LAmorce"] == "Lettre":
            #self.listbox.selection_set(first=0)
            self.combo1.current(0)
        elif datalist["LAmorce"] == "Chiffre":
            #self.listbox.selection_set(first=1)
            self.combo1.current(1)