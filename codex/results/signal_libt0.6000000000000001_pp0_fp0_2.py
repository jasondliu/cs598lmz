import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtWidgets import QLineEdit, QLabel
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication

from game import *

class GameWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Puzzle')
        self.setGeometry(400, 400, 500, 500)

        self.game = Game()
        self.game.newGame(4)

        self.font = QFont('SansSerif', 12)

        self.cells = [[]]

        for i in range(0, 4):
            self.cells.append([])

