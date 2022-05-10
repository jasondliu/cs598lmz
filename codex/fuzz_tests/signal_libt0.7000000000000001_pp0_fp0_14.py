import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

#from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtGui import QPixmap, QPainter, QColor, QBrush, QFont
from PyQt5.QtCore import Qt, QTimer, QThread, pyqtSignal, pyqtSlot
from random import randint, choice
import json
from playsound import playsound

class Communicate(QObject):
    closeApp = pyqtSignal()

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.start()

    def start(self):
        self.setGeometry(0, 0, 1280, 720)
        self.setWindowTitle("Эпидемия")
        self.
