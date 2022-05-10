import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Browser(QWebEngineView):
    def __init__(self):
        self.view = QWebEngineView.__init__(self)
        self.setWindowTitle('Loading...')
        self.titleChanged.connect(self.adjustTitle)
        self.load(QUrl("http://www.google.com"))
        self.show()

    def adjustTitle(self):
        self.setWindowTitle(self.title())

