import sys
from PyQt5 import QtCore, QtGui, QtWidgets,Qt
import kalkulatorwyz as kw
import kalkulatortrans as kt
import kalkulatorodw as ko
import kalkulatormnoz as km


class Window_rodzic(QtWidgets.QMainWindow): #Klasa definujaca wspolne funkcje oraz zmienne pozostalych okien
    #funkcja zmieniajaca okno w zaleznosci od podanego sygnalu
    sygnal = QtCore.pyqtSignal(str)
    def idz(self, nazwa):
        self.sygnal.emit(nazwa)
    
    #funckja powrotu do glownego okna
    def wroc_Main(self):
        self.idz("main")

class MainWindow(Window_rodzic):    #Klasa definiujaca glowne okno
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Matrix")

        #tworzenie przyciskow menu w oknie glownym 
        self.wyz = QtWidgets.QPushButton("Wyznacznik Macierzy", self)
        self.wyz.setGeometry(0,0,200,100)
        self.wyz.clicked.connect(self.tworzenie_wyboru("wyznacznik"))

        self.trans = QtWidgets.QPushButton("Macierz transponowana",self)
        self.trans.setGeometry(0,100,200,100) 
        self.trans.clicked.connect(self.tworzenie_wyboru("transponowana"))

        self.odw = QtWidgets.QPushButton("Macierz odwrotna",self)
        self.odw.setGeometry(0,200,200,100)
        self.odw.clicked.connect(self.tworzenie_wyboru("odwrotna"))

        self.mnoz = QtWidgets.QPushButton("Mnożenie dwóch macierzy",self)
        self.mnoz.setGeometry(0,300,200,100)
        self.mnoz.clicked.connect(self.tworzenie_wyboru("mnozenie"))

    #funkcja nadajaca odpowiedni sygnal zalezny od przycisku i przechodzaca na dane okno 
    def tworzenie_wyboru(self, przycisk):
        def wybor():
            if przycisk == "wyznacznik":
                self.idz("wyznacznik")
            if przycisk == "transponowana":
                self.idz("transponowana")
            if przycisk == "odwrotna":
                self.idz("odwrotna")
            if przycisk == "mnozenie":
                self.idz("mnozenie")
        return wybor

class Wyznacznik(Window_rodzic):   #klasa definujaca podstrone wyznacznik macierzy
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Matrix - wyznacznik")
        
        #tworzenie przycisku powrot do otworzenia okna main
        self.powrot = QtWidgets.QPushButton("Powrót", self)
        self.powrot.setGeometry(0,0,200,100)
        self.powrot.clicked.connect(self.wroc_Main)

        #tworzenie miejsca na slajd z teoria
        self.teoria2 = QtWidgets.QLabel(self)
        self.teoria2.setStyleSheet("border: 2px solid black;")
        self.teoria2.resize(800,600)
        self.teoria2.move(200,0)

        #tworzenie przycisku otwierajacego slajd z teoria
        self.teoria = QtWidgets.QPushButton("Teoria", self)
        self.teoria.setGeometry(0,100,200,100)
        self.teoria.clicked.connect(self.obrazy)

        #tworzenie przycisku otwierajacego kalkulator
        self.wiz = QtWidgets.QPushButton("Kalkulator", self)
        self.wiz.setGeometry(0,200,200,100)
        self.wiz.clicked.connect(self.otworz_kw)

    #funkcja otwierajaca kalkulator
    def otworz_kw(self):
        self.w = kw.Kalkulatorwyz()
        self.w.show()

    #funkcja wyswietlajaca slajd z teoria
    def obrazy(self):
        pixma= QtGui.QPixmap('wyznacznik.png')
        self.teoria2.setPixmap(pixma)
        self.resize(pixma.width(),pixma.height())

class Transponowana(Window_rodzic):    #klasa definujaca podstrone transponowana macierz
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Matrix - transponowana")
        
        #tworzenie przycisku powrot do otworzenia okna main
        self.powrot = QtWidgets.QPushButton("Powrót", self)
        self.powrot.setGeometry(0,0,200,100)
        self.powrot.clicked.connect(self.wroc_Main)

        #tworzenie przycisku otwierajacego slajd z teoria
        self.teoria = QtWidgets.QPushButton("Teoria", self)
        self.teoria.setGeometry(0,100,200,100)
        self.teoria.clicked.connect(self.obrazy)

        #tworzenie przycisku otwierajacego kalkulator
        self.wiz = QtWidgets.QPushButton("Kalkulator", self)
        self.wiz.setGeometry(0,200,200,100)
        self.wiz.clicked.connect(self.otworz)

        #tworzenie miejsca na slajd z teoria
        self.teoria2 = QtWidgets.QLabel(self)
        self.teoria2.setStyleSheet("border: 2px solid black;")
        self.teoria2.resize(800,600)
        self.teoria2.move(200,0)

    #funkcja wyswietlajaca slajd z teoria
    def obrazy(self):
        pixma= QtGui.QPixmap('transponowana.png')
        self.teoria2.setPixmap(pixma)
        self.resize(pixma.width(),pixma.height())

    #funkcja otwierajaca kalkulator
    def otworz(self):
        self.okno = kt.Kalkulatortrans()
        self.okno.show()

class Odwrotna(Window_rodzic):     #klasa definujaca podstrone odwrotna macierz
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Matrix - odwrotna")

        #tworzenie przycisku powrot do otworzenia okna main
        self.powrot = QtWidgets.QPushButton("Powrót", self)
        self.powrot.setGeometry(0,0,200,100)
        self.powrot.clicked.connect(self.wroc_Main)

        #tworzenie przycisku otwierajacego slajd z teoria
        self.teoria = QtWidgets.QPushButton("Teoria", self)
        self.teoria.setGeometry(0,100,200,100)
        self.teoria.clicked.connect(self.obrazy)

        #tworzenie miejsca na slajd z teoria
        self.teoria2 = QtWidgets.QLabel(self)
        self.teoria2.setStyleSheet("border: 2px solid black;")
        self.teoria2.resize(800,600)
        self.teoria2.move(200,0)

        #tworzenie przycisku otwierajacego kalkulator
        self.wiz = QtWidgets.QPushButton("Kalkulator", self)
        self.wiz.clicked.connect(self.otworz)
        self.wiz.setGeometry(0,200,200,100)

    #funkcja wyswietlajaca slajd z teoria 
    def obrazy(self):
        pixma= QtGui.QPixmap('odwrotna.png')
        self.teoria2.setPixmap(pixma)
        self.resize(pixma.width(),pixma.height())
    
    #funkcja otwierajaca kalkulator
    def otworz(self):
        self.okno = ko.Kalkulatorodw()
        self.okno.show()

class Mnozenie(Window_rodzic):     #klasa definujaca podstrone mnozenie macierzy
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Matrix - mnożenie")
        
        #tworzenie przycisku powrot do otworzenia okna main
        self.powrot = QtWidgets.QPushButton("Powrót", self)
        self.powrot.setGeometry(0,0,200,100)
        self.powrot.clicked.connect(self.wroc_Main)

        #tworzenie przycisku otwierajacego slajd z teoria
        self.teoria = QtWidgets.QPushButton("Teoria", self)
        self.teoria.setGeometry(0,100,200,100)
        self.teoria.clicked.connect(self.obrazy)

        #tworzenie miejsca na slajd z teoria
        self.teoria2 = QtWidgets.QLabel(self)
        self.teoria2.setStyleSheet("border: 2px solid black;")
        self.teoria2.resize(800,600)
        self.teoria2.move(200,0)

        #tworzenie przycisku otwierajcego kalkulator
        self.wiz = QtWidgets.QPushButton("Kalkulator", self)
        self.wiz.setGeometry(0,200,200,100)
        self.wiz.clicked.connect(self.otworz)

    #funkcja wyswietlajaca slajd z teoria 
    def obrazy(self):
        pixma= QtGui.QPixmap('mnozenie.png')
        self.teoria2.setPixmap(pixma)
        self.resize(pixma.width(),pixma.height())
    
    #funkcja otwierajaca kalkulator
    def otworz(self):
        self.okno = km.Kalkulatormnoz()
        self.okno.show()

class Window(QtWidgets.QMainWindow): #głowna klasa odpowiadajaca za nawigowanie pomiedzy stronami
    def __init__(self):
        super().__init__()
        #ustawianie parametrow okna glownego
        self.setWindowIcon(QtGui.QIcon("icon.png")) 
        self.setGeometry(500,200,1000,600)
        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        #deklaracja zbioru na strony 
        self.strony = {}

        #zapisanie wszystkich podstron
        self.zapisz(MainWindow(), "main")
        self.zapisz(Wyznacznik(), "wyznacznik")
        self.zapisz(Transponowana(), "transponowana")
        self.zapisz(Odwrotna(), "odwrotna")
        self.zapisz(Mnozenie(), "mnozenie")

        #otworzenie okna main
        self.idz("main")

    #funkcja rejestrujaca wszystkie inne okna
    def zapisz(self, strona, nazwa):
        self.strony[nazwa] = strona
        self.stacked_widget.addWidget(strona)
        if isinstance(strona, Window_rodzic):
            strona.sygnal.connect(self.idz)

    #funkcja odpowiedzialna za sprawdzanie czy dane okno istnieje oraz zmienienie go na aktualna 
    @QtCore.pyqtSlot(str)
    def idz(self, nazwa):
        if nazwa in self.strony:
            strona = self.strony[nazwa]
            self.stacked_widget.setCurrentWidget(strona)
            self.setWindowTitle(strona.windowTitle())

app = QtWidgets.QApplication(sys.argv)
w = Window()
w.show()
app.exec()