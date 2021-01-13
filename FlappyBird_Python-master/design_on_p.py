import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMainWindow
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
from PyQt5 import uic
import subprocess as sb
import os

test_file = "TEST.bat"
bird_file = "FlappyBird_Python-master/FLAPPY_BIRD_GAME.bat"


def test():
    sb.Popen([test_file])


def bird():
    os.startfile(r'flappy_update.py')


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMouseTracking(True)

    def initUI(self):
        self.setGeometry(0, 0, 1280, 800)
        self.setWindowTitle("КЛАССИЧЕСКИЕ ИГРЫ")

        self.title = QLabel(self)
        self.title.setText("КЛАССИЧЕСКИЕ ИГРЫ")
        self.title.setFont(QtGui.QFont("MS Shell Dlg 2", 30, QtGui.QFont.Bold))
        self.title.resize(600, 90)
        self.title.move(380, 50)

        self.copyright = QLabel(self)
        self.copyright.setText("Разработка Краснова Андрея и Кайдалова Руслана")
        self.copyright.setFont(QtGui.QFont("MS Shell Dlg 2", 8))
        self.copyright.resize(350, 15)
        self.copyright.move(10, 10)

        self.bt1 = QPushButton(self)
        self.bt1.setText("ЗМЕЙКА")
        self.bt1.resize(300, 120)
        self.bt1.move(30, 300)

        self.bt2 = QPushButton(self)
        self.bt2.setText("FLAPPY BIRD")
        self.bt2.resize(300, 120)
        self.bt2.move(495, 300)
        self.bt2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.bt3 = QPushButton(self)
        self.bt3.setText("ТЕТРИС")
        self.bt3.resize(300, 120)
        self.bt3.move(960, 300)

        self.bt1_s = QPushButton(self)
        self.bt1_s.setText("ИГРАТЬ")
        self.bt1_s.resize(300, 35)
        self.bt1_s.move(30, 385)
        self.bt1_s.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.bt1_s.clicked.connect(test)

        self.bt2_s = QPushButton(self)
        self.bt2_s.setText("ИГРАТЬ")
        self.bt2_s.resize(300, 35)
        self.bt2_s.move(495, 385)
        self.bt2_s.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.bt2_s.clicked.connect(bird)

        self.bt3_s = QPushButton(self)
        self.bt3_s.setText("ИГРАТЬ")
        self.bt3_s.resize(300, 35)
        self.bt3_s.move(960, 385)
        self.bt3_s.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.t1 = QLabel(self)
        self.t1.setText("Чтобы поиграть в одну из игр - нажмите на кнопку ИГРАТЬ под названием.")
        self.t1.setFont(QtGui.QFont("MS Shell Dlg 2", 16))
        self.t1.resize(950, 110)
        self.t1.move(180, 520)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
