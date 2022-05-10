import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import QUrl, QTimer
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebKit import QWebSettings
from PyQt5.QtWebKitWidgets import QWebView

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebKitWidgets import QWebView

class Browser(QWebView):

    def __init__(self):
        self.view = QWebView.__init__(self)
        self._loadFinished = False
        self.loadFinished.connect(self._loadFinished)

    def open(self, url):
        self.url = QUrl(url)
        self.load(self.url)

    def _loadFinished(self, result):
        self._loadFinished = True

app = QApplication(sys.argv)


