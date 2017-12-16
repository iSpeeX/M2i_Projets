import os
from tkinter import messagebox


class Rename:
    def __init__(self):
        test = 1

    def renom(self, data):
        """
            Fonction qui lance la procédure de renommage du ou des fichiers
        """

        pm = os.listdir(data["NomRep"])
        pre = data["Prefixe"]
        suf = data["Suffixe"]
        apa = data["Apartirde"]
        t1 = data["NomNewCheck"]
        ext = data["Extension"]
        lis = data["Amorce"]
        sufi = suf.replace("\n", "")
        exte = ext.split(", ")
        alert = 1
        cpt = 0

        for element in pm:
            list = os.path.splitext(element)
            onlyext = list[1]

            if t1 == 1:
                self.non = data["NomNew"]
            elif t1 == 0:
                self.non = list[0]

            for i in exte:
                if i == onlyext:
                    if lis == "Chiffre":
                        os.rename(data["NomRep"] + "/" + element, data["NomRep"] + "/" + str(apa) + pre + self.non + sufi + list[1])
                        alert = 0
                        apa = int(apa) + 1
                    elif lis == "Lettre":
                        apa = chr(ord(apa))
                        os.rename(data["NomRep"] + "/" + element, data["NomRep"] + "/" + str(apa) + pre + self.non + sufi + list[1])
                        alert = 0
                        apa = chr(ord(apa) + 1)
                cpt = cpt + 1

        if alert == 1:
            self.alert()

    def alert(self):
        """
            Petite fenêtre pour alerter sur le manque de fichier avec l'extension
        """
        messagebox.showwarning("Attention !", "Aucun fichier correspondant à l'extension.")