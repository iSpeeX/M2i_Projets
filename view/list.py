from tkinter import *
from tkinter.messagebox import *

datalist = {} # Variable globale pour la liste de règles

class List:
    def __init__(self):
        self.t = Tk()
        self.t.title("Liste des règles")
        self.list()
        self.Buttons()
        self.t.mainloop()

    def list(self):
        self.listbox2 = Listbox(self.t, height=15, width=50)

        with open("./RenIT.ini", "r") as fichier:
            i = 0
            lines = fichier.readlines()
            for char in lines:
                self.listbox2.insert(END, lines[i])
                i = i + 1
            fichier.close()
        self.listbox2.grid(row=1, column=1, padx=5, rowspan=2, columnspan=2)

    def Buttons(self):
        Button(self.t, text="Utiliser", command=self.use).grid(row=0, column=1, padx=5)
        Button(self.t, text="Supprimer", fg='red', command=self.delete).grid(row=0, column=2, padx=5)


    def use(self):

        li = self.listbox2.get(self.listbox2.curselection())
        lit = li.split(";")

        datalist["Rule"] = self.listbox2.get(self.listbox2.curselection())
        datalist["LNomRegle"] = lit[0]
        datalist["LNomFichier"] = lit[5]
        datalist["LPrefixe"] = lit[3]
        datalist["LSuffixe"] = lit[6]
        datalist["LExtension"] = lit[4]
        datalist["LApartirde"] = lit[2]
        datalist["LAmorce"] = lit[1]
        datalist["LIndex"] = int(0)
        self.t.destroy()
        self.info()
        return datalist

    def info(self):
        showinfo("Règle chargée", "La règle "+ datalist["LNomRegle"] +" a bien été chargée.\nAppuyez sur le bouton 'Insérer règle' pour l'utiliser.")

    def delete(self):
        """
            Permet de supprimer une règle dans le fichier .ini
        """
        chaine = self.listbox2.get(self.listbox2.curselection())
        contenu = ""

        fichier = open("./RenIT.ini", "r")
        for ligne in fichier:
            if not (chaine in ligne):
                contenu += ligne
        fichier.close()

        fichier = open("./RenIT.ini", 'w')
        fichier.write(contenu)
        fichier.close()
        self.list()