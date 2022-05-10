import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtCore import QTimer

import sys

class WebEnginePage(QWebEngineView):
    def __init__(self, parent=None):
        super(WebEnginePage, self).__init__(parent)
        self.loadFinished.connect(self._on_load_finished)
        self.load(QUrl("https://www.google.com"))

    def _on_load_finished(self):
        self.page().runJavaScript("document.getElementsByName('q')[0].value = 'Hello World!'")
        self.page().runJavaScript("document.getElementsByName('btnK')[0].click()")

if __name__ == '__main__':
    app = QApplication(sys.argv)

