import subprocess
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

def bird():
    subprocess.Popen(['python', 'flappy_update.py'])


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('form.ui', self)  # Загружаем дизайн
        self.setMouseTracking(True)
        self.flappy_button.clicked.connect(bird)
        self.flappy_button.setStyleSheet("background-image : url('data/background.png'); border-radius: 8px;")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
