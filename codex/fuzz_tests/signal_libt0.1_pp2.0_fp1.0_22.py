import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtCore import QEventLoop, QTimer
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest

from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWebChannel import QWebChannel

from PyQt5.QtCore import QObject, pyqtSlot

import sys
import time
import json
import os

class Bridge(QObject):
    def __init__(self, parent=None):
        super(Bridge, self).__init__(parent)

    @pyqtSlot(str)
    def log(self, msg):
        print(msg)

    @pyqtSlot(str)
    def save(self, msg):
        print(msg)
       
