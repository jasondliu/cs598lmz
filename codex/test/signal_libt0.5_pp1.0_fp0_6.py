import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtWebChannel import QWebChannel

import os
import sys
import json
import threading
import logging
import time

from . import server
from . import mqtt
from . import config
from . import utils

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle('Raspi-Monitor')
        self.setGeometry(0, 0, 800, 480)

        self.webview = QWebEngineView()
        self.setCentralWidget(self.webview)

