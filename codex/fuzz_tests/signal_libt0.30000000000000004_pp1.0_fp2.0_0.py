import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

class Communicate(QObject):
    signal = pyqtSignal(str)

class Browser(QWebEngineView):
    def __init__(self):
        self.app = QApplication(sys.argv)
        QWebEngineView.__init__(self)
        self._loadFinished = False
        self.loadFinished.connect(self._loadFinished)
        self.c = Communicate()
        self.c.signal.connect(self.evaluateJavaScript)
        self.setHtml('''
        <!DOCTYPE html>
        <html>
        <head>
        <meta charset="utf-8">
        <title>ECh
