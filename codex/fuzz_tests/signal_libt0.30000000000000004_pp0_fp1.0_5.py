import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout

from PyQt5.QtCore import QCoreApplication

from PyQt5.QtCore import QObject, pyqtSignal

import sys

class Communicate(QObject):
    closeApp = pyqtSignal()

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Emit signal')
        self.show()

    def mousePressEvent(self, event):
        self.c.closeApp.
