import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QAction, QLabel, QLineEdit, QPushButton, QMessageBox,
                             QTableWidget, QTableWidgetItem, QFrame, QHBoxLayout, QVBoxLayout, QSizePolicy)
from PyQt5.QtGui import QIcon, QFont, QPalette, QColor
from PyQt5.QtCore import Qt

import random

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = '猜数字游戏'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

