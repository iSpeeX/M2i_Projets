from tkinter import *
from tkinter.ttk import *
import tkinter.font as font
from classes.regle import Regle

rule = Regle()

datacreate = {} # Variable globale pour la création de règles

class Create:
    def __init__(self):
        self.cr = Tk()
        self.cr.title("Création d'une règle")
        self.Labels()
        self.Entry()
        self.Buttons()
        self.Listbox()
        self.Head()
        self.Foot()
        self.cr.mainloop()

    def Labels(self):
        tf = font.Font(size=20)
        tf2 = font.Font(size=15)

        titre = Label(self.cr, text="Créer une règle", font=tf).grid(row=0, column=2, columnspan=3, padx=10, rowspan=4)
        nomregle = Label(self.cr, text="Nom de la règle", font=tf2).grid(row=5, column=2, padx=10)
        amorce = Label(self.cr, text="Amorce").grid(row=6, column=1, padx=5)
        prefix = Label(self.cr, text="Préfixe").grid(row=6, column=2, padx=5)
        nomfich = Label(self.cr, text="Nom du fichier").grid(row=6, column=3, padx=5)
        suffix = Label(self.cr, text="Suffixe").grid(row=6, column=5, padx=5)
        extension = Label(self.cr, text="Extension concernée").grid(row=6, column=6, padx=5)
        apartir = Label(self.cr, text="A partir de").grid(row=9, column=1, padx=5)

    def Entry(self):
        self.Cnomregle = Entry(self.cr, width=20)
        self.Cnomregle.grid(row=5, column=3, padx=10)

        self.Cprefixe = Entry(self.cr, width=20)
        self.Cprefixe.grid(row=7, column=2, padx=5)

        self.Cnomfichier = Entry(self.cr, width=20)
        self.Cnomfichier.grid(row=7, column=3, padx=5)

        self.Csuffixe = Entry(self.cr, width=20)
        self.Csuffixe.grid(row=7, column=5, padx=5)

        self.Cext = Entry(self.cr, width=20)
        self.Cext.grid(row=7, column=6, padx=5)

        self.Capartirde = Entry(self.cr, width=20)
        self.Capartirde.grid(row=10, column=1, padx=5)

    def Buttons(self):
        bouton_rename = Button(self.cr, text="Créer", command=self.charge_datacreate).grid(row=6, column=7, padx=5)

    def Listbox(self):
        self.amorceSelect = StringVar()
        self.listamorce = ('Lettre', 'Chiffre')
        self.combo = Combobox(self.cr, textvariable=self.amorceSelect, values=self.listamorce)
        self.combo.grid(row=7, column=1, padx=5, rowspan=2)

    def Head(self):
        foot1 = Label(self.cr, text="")
        foot1.grid(column=0, row=1, rowspan=2)

        foot2 = Label(self.cr, text="")
        foot2.grid(column=7, row=3, rowspan=2)

    def Foot(self):
        foot1 = Label(self.cr, text="")
        foot1.grid(column=0, row=11, rowspan=2)

        foot2 = Label(self.cr, text="")
        foot2.grid(column=7, row=13, rowspan=2)

    def charge_datacreate(self):
        datacreate["CNomRegle"] = self.Cnomregle.get()
        datacreate["CNomFichier"] = self.Cnomfichier.get()
        datacreate["CPrefixe"] = self.Cprefixe.get()
        datacreate["CSuffixe"] = self.Csuffixe.get()
        datacreate["CExtension"] = self.Cext.get()
        datacreate["CApartirde"] = self.Capartirde.get()
        datacreate["CAmorce"] = self.combo.get()

        rule.createrule(datacreate)
        self.cr.destroy()