import sys
import numpy as np
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QSize, Qt

class Kalkulatorwyz(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        #ustawianie parametrow okna
        self.setMinimumSize(QSize(500, 500))
        self.setMaximumSize(QSize(500, 500))
        self.setWindowTitle("Matrix - Kalkulator Wyz")
        self.setWindowIcon(QtGui.QIcon("icon.png"))

        #tworzenie tabelki macierzy
        self.table = QtWidgets.QTableWidget(self)
        self.table.setColumnCount(3)
        self.table.setRowCount(3)
        self.table.horizontalHeader().hide()
        self.table.verticalHeader().hide()
        self.table.setMaximumHeight(71)
        self.table.setMaximumWidth(119)
        self.table.setStyleSheet("border: 1px solid black;")
        self.table.move(190,50)

        #ustawianie domyslnych wartosci komorek w obu tabelkach na 0 
        for i in range(3):
            for j in range(3) :
                self.table.setItem(i, j, QtWidgets.QTableWidgetItem(str(0)))

        #dostosowanie rozmiaru komorek tabeli do zawartosci
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()
        
        #tworzenie przycisku wywołującego funkcje obliczajaca
        oblicz = QtWidgets.QPushButton(self)
        oblicz.setText("Oblicz")
        oblicz.setMinimumSize(QSize(119,50))
        oblicz.move(190,250)
        oblicz.clicked.connect(self.oblicz)

        #tworzenie napisu "Wyznacznik: --" oraz miejsca na wynik
        self.wynik=QtWidgets.QLabel(self)
        self.wynik.setText("Wyznacznik: --")
        self.wynik.move(210,150)
        
    #funkcja wykonujaca mnozenie macierzy
    def oblicz(self):
        #deklaracja oraz wypelnienie macierzy zerami
        macierz = np.zeros((3,3))

        #pobieranie wartosci z tabelek do macierzy oraz wysrodkowanie zawartosci komorek
        for i in range(3):
            for j in range(3) :
                macierz[i,j]=self.table.item(i, j).text()
                self.table.item(i,j).setTextAlignment(Qt.AlignHCenter)

        #obliczanie wyznacznika
        wyznacznik=np.around(np.linalg.det(macierz),5)

        #ustawienie wyniku we wczesniej przygotowanym napisie         
        self.wynik.setText("Wyznacznik: "+str(wyznacznik))
        self.wynik.adjustSize()

        #otwarcie i zamkniecie pliku txt wraz z zapisaniem wyznacznika
        wyniki = open("wyniki.txt", "w")
        wyniki.write("Wyznacznik: "+str(wyznacznik))
        #np.savetxt(wyniki,wyznacznik)
        wyniki.close()

        return macierz
