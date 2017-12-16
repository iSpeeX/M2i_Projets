class Regle:
    def __init__(self):
        pass

    def createrule(self, datacreate):
        """
            Ajoute une ligne correspondant aux 7 éléments qui constitue une règle, dans le fichier .ini
        """
        tx = str(datacreate["CNomFichier"])
        ap = str(datacreate["CApartirde"])
        pr = str(datacreate["CPrefixe"])
        su = str(datacreate["CSuffixe"])
        li = str(datacreate["CAmorce"])
        ex = str(datacreate["CExtension"])
        nr = str(datacreate["CNomRegle"])
        rule = nr + ";" + li + ";" + ap + ";" + pr + ";" + ex + ";" + tx + ";" + su
        mon_ini = open("../RenIT.ini", "a")
        print(rule, file=mon_ini)
        mon_ini.close()


    def get_amorce(self):

        return self.mon_amorce

    def get_apartirde(self):

        return self.mon_apartirde

    def get_prefixe(self):

        return self.mon_prefixe

    def get_nomfichier(self):

        return self.mon_nomfichier

    def get_suffixe(self):

        return self.mon_suffixe

    def get_extension(self):

        return self.mon_extension

    def set_amorce(self, new_amorce):
        self.mon_amorce = new_amorce
        return

    def set_apartirde(self, new_apartirde):
        self.mon_apartirde = new_apartirde
        return

    def set_prefixe(self, new_prefixe):
        self.mon_prefixe = new_prefixe
        return

    def set_nomfichier(self, new_nomfichier):
        self.mon_nomfichier = new_nomfichier
        return

    def set_suffixe(self, new_suffixe):
        self.mon_suffixe = new_suffixe
        return

    def set_extension(self, new_extension):
        self.mon_extension = new_extension
        return


    def __str__(self):
        return "{};{};{};{};{};{};{}".format(self.mon_nomregle, self.mon_amorce, self.mon_apartirde, self.mon_prefixe, self.mon_suffixe, self.mon_extension, self.mon_nomfichier)
