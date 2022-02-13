import os
import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter import *

from executor import executeSelectedScenarios
from executor import executeAllScenarios



class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.createWidgets()
        App.geometry(self, '350x150')
        App.title(self, 'CSVnario')

    def createWidgets(self):
        
        #Przyciski na master
        
        sc_button        = tk.Button(self, text="Scenario Creator", command=self.openCreator)
        sc_folder_button = tk.Button(self, text="Import Scenarios", command=self.importScenarios)
        scenario_start   = tk.Button(self, text="Execute scenarios", command=executeSelectedScenarios())
        scenario_listbox = tk.Listbox(self, selectmode="multiple")



        sc_button.grid(row = 0, column = 0, padx=5, pady = 2)
        sc_folder_button.grid(row = 0, column = 1, padx=5, pady = 2)
        scenario_start.grid(row=0, column = 2, padx=5, pady=2)
        scenario_listbox.grid(row = 1, column = 0, padx=5, pady = 15)


    # OTWIERAMY KREATOOOR
    def openCreator(self):
        c = Creator(self)
        c.wait_window()


    # OTWORZ SE FOLDEREK ZE SCENARIUSZAMI
    def importScenarios(self):
        filetypes = (
            ('csv files', '*.csv'),
        )

        filenames = fd.askopenfilenames(
            title='Open files',
            initialdir= str(os.getcwd()) + "\\app\\scenarios\\",
            filetypes=filetypes
        )

        showinfo(
            title='Selected Scenarios have been imported',
            message=filenames
        )
        print(filenames)
        
        arr = filenames

        return arr 

        # tutaj filenames wyrzuca liste sciezek do wybranych scenariuszy
        # musze zrobic scenario_listbox.insert(nazwa pliku, sciezka), ale zeby sie wyswietlala tylko nazwa (czyli ostatnie po backslashu bez .csv, czyli example, example2, example3)
        # koniecznie musza byc zapamietane sciezki ktore beda podane dalej jako arr do executeSelectedScenarios(arr)
        

    


class Creator(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()


    def create_widgets(self):
        tk.Label(self, text='Welcome to the creator!').pack(padx=20, pady=50)



        

if __name__ == '__main__':
    app = App()
    app.mainloop()
