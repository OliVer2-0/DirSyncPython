# Class Ordner - als Modul für Import

import os

class Ordner: 
    

    # Konstruktor für Ordner mit Übergabe des Pfades 
    def __init__(self,pfad):
        self.pfad = pfad
        self.dateiListe = []
       

    # Listet alle Dateien im Verzeichnis auf und fügt sie der Liste hinzu
    def baueListe(self):

        self.dateiListe = os.listdir(self.pfad)
        
        
        
        

