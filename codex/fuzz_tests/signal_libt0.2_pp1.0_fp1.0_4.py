import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Пример главного окна")
        self.resize(300, 300)
        self.init_ui()

    def init_ui(self):
        self.label = QLabel("Привет, мир!", self)
        self.label.move(50, 50)
        self.label.setAlignment(Qt.AlignCenter)

        self.button = QPushButton("Нажми меня", self)
        self.button.move(50, 100)

