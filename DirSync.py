# objektorientierte Version
# Programm vergleicht Ziel- und Quellordner auf unterschiedlich aktuelle Dateien 
# und gleicht die Dateien an
#
#
# 
import os
# importierte vom Modul Ordner die Klasse Ordner - für einfache Schreibweise im Programm
from Ordner import Ordner


# Quellordner festlegen
fehler = True
while fehler:
    try:
        pfadQuellOrdner = input("Geben Sie den Pfad des Quellordners ein:")
        if(os.path.isdir(pfadQuellOrdner)):
            fehler = False
        else:
            raise RuntimeError("Der angegebene Pfad war nicht korrekt!")
    except RuntimeError as e:
            print(e)


# Zielordner festlegen
fehler = True
while fehler:
    try:
        pfadZielOrdner = input("Geben Sie den Pfad des Zielordners ein:")
        if(os.path.isdir(pfadZielOrdner)):
            fehler = False
        else:
            raise RuntimeError("Der angegebene Pfad war nicht korrekt!")
    except RuntimeError as e:
        print(e)

# Später sollen die Pfade in einer Datei gespeichert werden - als Profil zur Wiedervorlage

zielOrdner = Ordner(pfadZielOrdner)
quellOrdner = Ordner(pfadQuellOrdner)

# Inhaltslisten der beiden Ordner anlegen
quellOrdner.baueListe()
zielOrdner.baueListe()

# Vergleich der beiden Liste auf Länge (Anzahl an Dateien)
# Fall 1: Mehr Dateien im Quellordner - Frage: Angleichen? 
# Fall 2: Beide Listen gleich lang - 
# Fall 3: Mehr Dateien im Zielordner - 

if(len(quellOrdner.dateiListe) > len(zielOrdner.dateiListe)):
    sollAnpassen = input("Quellordner (" + pfadQuellOrdner +") enthält mehr Dateien als Zielordner (" + pfadZielOrdner +")."
                        "\nSollen die Ordner angeglichen werden? [J] / [N] ")
    if(sollAnpassen.upper() == 'J'):
        #
        #
        #
        print ("Hier müsste man jetzt die Dateien hin und herschieben")

print("Dateien im Quellordner",quellOrdner.dateiListe)

print("Dateien im Zielordner",zielOrdner.dateiListe)

