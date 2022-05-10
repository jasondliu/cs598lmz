import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, \
    QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QFont

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Virtual Clock')
        self.setFixedSize(500, 150)
        self.move(500, 300)
        self.createGrid()
        self.createButtons()
        self.createTimer()

    def createGrid(self):
        self.grid = QGridLayout()
        self.grid.setSpacing(10)
        self.setLayout(self.grid)

    def createButtons(self):
        btnStart = QPush
