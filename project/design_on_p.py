import subprocess
import os
import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication

scriptDir = os.path.dirname(os.path.realpath('data/background.png'))  # Загружаем иконку приложения


def bird():
    subprocess.Popen(['python', 'flappy_update.py'])


def snake():
    subprocess.Popen(['python', 'snake_game.py'])


def tetris():
    subprocess.Popen(['python', 'tetris_game.py'])


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('form.ui', self)  # Загружаем дизайн
        self.setStyleSheet("background-color:rgb(10, 10, 10)")
        self.setWindowTitle('КЛАССИЧЕСКИЕ ИГРЫ')
        self.title_label.setStyleSheet("background-color:rgb(10, 10, 10)")
        self.setMouseTracking(True)
        self.flappy_button.clicked.connect(bird)
        self.flappy_button.setStyleSheet("background-image : url('data/background.png'); border-radius: 8px;")
        self.snake_button.clicked.connect(snake)
        self.snake_button.setStyleSheet("background-image : url('data/background.png'); border-radius: 8px;")
        self.tetris_button.clicked.connect(tetris)
        self.tetris_button.setStyleSheet("background-image : url('data/background.png'); border-radius: 8px;")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
