# Class Ordner - als Modul für Import

import os
import shutil

class Ordner: 
    __dateiListe = []
    
    # Konstruktor für Ordner mit Übergabe des Pfades 
    def __init__(self,pfad):
        self.pfad = pfad
        
       

    # Listet alle Dateien im Verzeichnis auf und fügt sie der Liste hinzu
    def baueListe(self):

        self.dateiListe = os.listdir(self.pfad)

    # Gleicht Inhalt mit übergebenem Ordner ab  
    def Sync (self, ordner):
        #TODO
        # Kontrolle auf Datei.Länge und Datei.EditDate 
        # Aktuell wird nur geschaut, ob Dateien im Ordner sind - falls nicht, werden sie verschoben
        # Sollte die Datei aber im Ordner sein, nur veraltet - würde das nicht bemerkt werden 
        
        for datei in ordner.dateiListe:
            if (os.path.isfile(ordner.pfad + os.path.sep + datei)):
                if (datei in self.dateiListe):
                    print("*")
                    continue
                else:
                    quellpfad = ordner.pfad + os.path.sep + datei
                    shutil.copy(quellpfad, self.pfad)
                    print("*")
            else:
                continue
        print ("100%")

    # Prüfe ob im angebenen Ordner Unterordner vorhanden sind:
    def getSubDir (self):
        enthaeltSubDir = False
        for datei in self.dateiListe:
            if (os.path.isfile(self.pfad + os.path.sep + datei)):
                continue
            elif (os.path.isdir(self.pfad + os.path.sep + datei)):
                enthaeltSubDir = True
                break
        return enthaeltSubDir






        
     

