import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtCore import QTimer

import sys

class Browser(QWebEngineView):
    def __init__(self):
        self.view = QWebEngineView.__init__(self)
        self.setWindowTitle('Loading...')
        self.titleChanged.connect(self.adjustTitle)
        self.loadFinished.connect(self.adjustTitle)
        self.load(QUrl("http://localhost:8080"))
        self.show()

    def adjustTitle(self):
        self.setWindowTitle(self.title())
        self.show()

    def disableJS(self):
        settings = QWebEngineSettings.globalSettings()
        settings.setAttribute(QWebEngineSettings.JavascriptEnabled, False)

if __name__ == '
