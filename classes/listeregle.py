from tkinter import *
from view.list import *


class Listeregle:
    def __init__(self):
        pass

    def get_regles(self):
        return self.mes_regles

    def set_regles(self, new_regles):
        self.mes_regles = new_regles
        return
