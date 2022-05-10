import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtWidgets import QWidget, QVBoxLayout

from PyQt5.QtCore import QTimer

import time

import json

class WebPage(QWebEngineView):
    def __init__(self):
        self.app = QApplication(sys.argv)
        QWebEngineView.__init__(self)
        self._loaded = False
        self.loadFinished.connect(self._loadFinished)

    def load(self, url):
        self.setUrl(QUrl(url))
        while not self._loaded:
            self.app.processEvents()
        self._loaded = False

    def _loadFinished(self, result):
        self._loaded = True

    def evaluate
