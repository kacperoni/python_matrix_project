import sys
import numpy as np
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QSize, Qt

class Kalkulatortrans(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        #ustawianie parametrow okna
        self.setMinimumSize(QSize(500, 500))
        self.setMaximumSize(QSize(500, 500))
        self.setWindowTitle("Matrix - Kalkulator Trans")
        self.setWindowIcon(QtGui.QIcon("icon.png"))

        #tworzenie napisu "Macierz przed"
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("Macierz przed")
        self.label1.setMaximumHeight(71)
        self.label1.setMaximumWidth(119)
        self.label1.move(210,75)

        #tworzenie tabelki dla macierzy przed transponowaniem
        self.table = QtWidgets.QTableWidget(self)
        self.table.setColumnCount(3)
        self.table.setRowCount(3)
        self.table.horizontalHeader().hide()
        self.table.verticalHeader().hide()
        self.table.setMaximumHeight(71)
        self.table.setMaximumWidth(119)
        self.table.setStyleSheet("border: 1px solid black;")
        self.table.move(190,100)

        #tworzenie napisu "Macierz Transponowana"
        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText("Macierz Transponowana")
        self.label2.setMaximumHeight(71)
        self.label2.setMaximumWidth(119)
        self.label2.move(190,225)

        #tworzenie tabelki dla wyniku macierzy transponowanej
        self.wyniktable = QtWidgets.QTableWidget(self)
        self.wyniktable.setColumnCount(3)
        self.wyniktable.setRowCount(3)
        self.wyniktable.horizontalHeader().hide()
        self.wyniktable.verticalHeader().hide()
        self.wyniktable.setMaximumHeight(71)
        self.wyniktable.setMaximumWidth(119)
        self.wyniktable.setStyleSheet("border: 1px solid black;")
        self.wyniktable.move(190,250)
        
        #ustawianie domyslnych wartosci komorek w obu tabelkach na 0 
        for i in range(3):
            for j in range(3) :
                self.table.setItem(i, j, QtWidgets.QTableWidgetItem(str(0)))
                self.wyniktable.setItem(i,j, QtWidgets.QTableWidgetItem(str(0)))

        #dostosowanie rozmiaru komorek tabeli do zawartosci
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()
        self.wyniktable.resizeColumnsToContents()
        self.wyniktable.resizeRowsToContents()
        
        #tworzenie przycisku wywołującego funkcje obliczajaca
        oblicz = QtWidgets.QPushButton(self)
        oblicz.setText("Oblicz")
        oblicz.setMinimumSize(QSize(119,50))
        oblicz.move(190,350)
        oblicz.clicked.connect(self.transponuj)

    #funkcja wykonujaca transponowanie macierzy
    def transponuj(self):
        #deklaracja oraz wypełnienie macierzy zerami
        macierz = np.zeros((3,3))
        
        #pobieranie wartosci z tabelek do macierzy oraz wysrodkowanie zawartosci komorek
        for i in range(3):
            for j in range(3) :
                macierz[i,j]=self.table.item(i, j).text()
                self.table.item(i,j).setTextAlignment(Qt.AlignHCenter)

        #otwarcie pliku txt oraz zapisanie macierzy poczatkowej
        wyniki = open("wyniki.txt", "w")
        wyniki.write("Macierz A\n")
        np.savetxt(wyniki,macierz,fmt='%s')
        
        #transponowanie macierzy
        macierz = macierz.T       

        #wypelnienie tabelki wynikiem oraz wysrodkowanie zawartosci komorek
        for i in range(3):
            for j in range(3):
                self.wyniktable.setItem(i,j, QtWidgets.QTableWidgetItem(str(int(macierz[i,j]))))
                self.wyniktable.item(i,j).setTextAlignment(Qt.AlignHCenter)    
        
        #zapisanie macierzy koncowej oraz zamkniecie pliku txt
        wyniki.write("\nMacierz A Transponowana\n")
        np.savetxt(wyniki,macierz,fmt='%s')
        wyniki.close()

        return macierz