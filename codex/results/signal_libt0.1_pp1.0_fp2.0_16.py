import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtWidgets import QWidget, QVBoxLayout

from PyQt5.QtCore import QTimer

import sys

class WebEngineView(QWebEngineView):
    def __init__(self, parent=None):
        super(WebEngineView, self).__init__(parent)
        self.loadFinished.connect(self._on_load_finished)
        self.load(QUrl("https://www.google.com"))

    def _on_load_finished(self):
        self.page().runJavaScript("document.body.style.backgroundColor = 'red'")

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle
