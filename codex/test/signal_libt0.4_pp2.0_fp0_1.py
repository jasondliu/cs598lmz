import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import QUrl, QObject, pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage

from PyQt5.QtWebChannel import QWebChannel

import sys

class CallHandler(QObject):
    @pyqtSlot(result=str)
    def get_data(self):
        return "Hello World!"

class WebEnginePage(QWebEnginePage):
    def __init__(self, *args, **kwargs):
        super(WebEnginePage, self).__init__(*args, **kwargs)
        self.loadFinished.connect(self._on_load_finished)

    def _on_load_finished(self):
        self.loadFinished.disconnect(self._on_load_finished)
        #self.runJavaScript("alert('Hello');")
