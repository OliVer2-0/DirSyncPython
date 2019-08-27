# objektorientierte Version
# Programm vergleicht Ziel- und Quellordner auf unterschiedlich aktuelle Dateien 
# und gleicht die Dateien an
#
#
# 

# importierte vom Modul Ordner die Klasse Ordner - für einfache Schreibweise im Programm
from Ordner import Ordner

# Quellordner festlegen
pfadQuellOrdner = input("Geben Sie den Pfad des Quellordners ein:")

# Zielordner festlegen
pfadZielOrdner = input("Geben Sie den Pfad des Zielordners ein:")

# Später sollen die Pfade in einer Datei gespeichert werden 

zielOrdner = Ordner(pfadZielOrdner)
quellOrdner = Ordner(pfadQuellOrdner)

# Inhaltslisten der beiden Ordner anlegen
quellOrdner.baueListe()
zielOrdner.baueListe()

print("Dateien im Quellordner",quellOrdner.dateiListe)

print("Dateien im Zielordner",zielOrdner.dateiListe)

