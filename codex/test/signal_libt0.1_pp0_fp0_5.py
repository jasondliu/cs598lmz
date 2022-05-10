import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtWidgets import QWidget, QVBoxLayout

from PyQt5.QtCore import QTimer

import sys

class WebView(QWebEngineView):
    def __init__(self, parent=None):
        super(WebView, self).__init__(parent)
        self.loadFinished.connect(self._result_available)

    def _result_available(self, ok):
        frame = self.page().mainFrame()
        print('text', frame.toPlainText())
        print('html', frame.toHtml())

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.view = WebView()
