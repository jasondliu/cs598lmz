import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import QUrl, QObject, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtCore import QVariant

import sys
import time

class MyObject(QObject):
    @pyqtSlot(result=str)
    def get_time(self):
        return str(time.time())

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Hello World")
        self.setGeometry(200, 200, 800, 600)

        self.view = QWebEngineView()
