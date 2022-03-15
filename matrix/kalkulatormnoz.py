import sys
import numpy as np
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QSize, Qt

class Kalkulatormnoz(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        #ustawianie parametrow okna
        self.setMinimumSize(QSize(500, 500))
        self.setMaximumSize(QSize(500, 500))
        self.setWindowTitle("Matrix - Kalkulator Mnoz")
        self.setWindowIcon(QtGui.QIcon("icon.png"))

        #tworzenie napisu "MacierzA"
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("Macierz A")
        self.label1.setMaximumHeight(71)
        self.label1.setMaximumWidth(119)
        self.label1.move(105,75)

        #tworzenie tabelki macierzy A
        self.table = QtWidgets.QTableWidget(self)
        self.table.setColumnCount(3)
        self.table.setRowCount(3)
        self.table.horizontalHeader().hide()
        self.table.verticalHeader().hide()
        self.table.setMaximumHeight(71)
        self.table.setMaximumWidth(119)
        self.table.setStyleSheet("border: 1px solid black;")
        self.table.move(70,100)

        #tworzenie napisu "Macierz B"
        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText("Macierz B")
        self.label2.setMaximumHeight(71)
        self.label2.setMaximumWidth(119)
        self.label2.move(343,75)

        #tworzenie tabelki macierzy B
        self.table2 = QtWidgets.QTableWidget(self)
        self.table2.setColumnCount(3)
        self.table2.setRowCount(3)
        self.table2.horizontalHeader().hide()
        self.table2.verticalHeader().hide()
        self.table2.setMaximumHeight(71)
        self.table2.setMaximumWidth(119)
        self.table2.setStyleSheet("border: 1px solid black;")
        self.table2.move(308,100)

        #tworzenie napis "Macierz AB"
        self.label3 = QtWidgets.QLabel(self)
        self.label3.setText("Macierz AB")
        self.label3.setMaximumHeight(71)
        self.label3.setMaximumWidth(119)
        self.label3.move(225,225)

        #tworzenie tabelki macierzy AB
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
                self.table2.setItem(i,j, QtWidgets.QTableWidgetItem(str(0)))
                self.wyniktable.setItem(i,j, QtWidgets.QTableWidgetItem(str(0)))

        #dostosowanie rozmiaru komorek tabeli do zawartosci
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()
        self.table2.resizeColumnsToContents()
        self.table2.resizeRowsToContents()
        self.wyniktable.resizeColumnsToContents()
        self.wyniktable.resizeRowsToContents()
        
        #tworzenie przycisku wywołującego funkcje obliczajaca
        oblicz = QtWidgets.QPushButton(self)
        oblicz.setText("Oblicz")
        oblicz.setMinimumSize(QSize(119,50))
        oblicz.move(190,375)
        oblicz.clicked.connect(self.mnozenie_macierzy)

    #funkcja wykonujaca mnozenie macierzy
    def mnozenie_macierzy(self):
        #deklaracja oraz wypelnienie macierzy zerami
        macierzA = np.zeros((3,3))
        macierzB = np.zeros((3,3))
        macierzAB = np.zeros((3,3))

        #pobieranie wartosci z tabelek do macierzy oraz wysrodkowanie zawartosci komorek
        for i in range(3):
            for j in range(3) :
                macierzA[i,j]=self.table.item(i, j).text()
                macierzB[i,j]=self.table2.item(i,j).text()
                self.table.item(i,j).setTextAlignment(Qt.AlignHCenter)
        
        #mnozenie macierzy

        #otwarcie pliku txt oraz zapisanie macierzy poczatkowych
        wyniki = open("wyniki.txt", "w")
        wyniki.write("Macierz A\n")
        np.savetxt(wyniki,macierzA,fmt='%s')

        wyniki.write("\nMacierz B\n")
        np.savetxt(wyniki,macierzB,fmt='%s')

        macierzAB = macierzA.dot(macierzB)    

        #wypelnienie tabelki macierzAB wynikiem oraz wysrodkowanie zawartosci komorek
        for i in range(3):
            for j in range(3):
                self.wyniktable.setItem(i,j, QtWidgets.QTableWidgetItem(str(int(macierzAB[i,j]))))
                self.wyniktable.item(i,j).setTextAlignment(Qt.AlignHCenter)    

        #zapisanie macierzy koncowej oraz zamkniecie pliku txt
        wyniki.write("\nMacierz AB\n")
        np.savetxt(wyniki,macierzAB,fmt='%s')
        wyniki.close()

        return macierzA