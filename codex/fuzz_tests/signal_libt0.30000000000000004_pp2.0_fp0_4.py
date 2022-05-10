import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import QUrl, QObject, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtWebChannel import QWebChannel

import sys
import json
import os

class Bridge(QObject):
    def __init__(self, parent=None):
        super(Bridge, self).__init__(parent)

    @pyqtSlot(str, str)
    def log(self, level, message):
        print(level + ": " + message)

    @pyqtSlot(str)
    def on_message(self, message):
        print("message: " + message)

class WebPage(QWebEnginePage):
    def __init__(self, parent=None):
        super(WebPage, self).__init__(parent)

    def javaScriptConsoleMessage(
