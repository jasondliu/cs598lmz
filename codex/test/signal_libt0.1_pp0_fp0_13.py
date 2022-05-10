import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtCore import QEventLoop, QTimer
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest

import sys

class Render(QWebEngineView):
    def __init__(self, url):
        self.html = None
        self.app = QApplication(sys.argv)
        QWebEngineView.__init__(self)
        self.loadFinished.connect(self._loadFinished)
        self.load(QUrl(url))
        while self.html is None:
            self.app.processEvents(QEventLoop.ExcludeUserInputEvents |
                                   QEventLoop.ExcludeSocketNotifiers |
                                   QEventLoop.WaitForMoreEvents)
        self.app.quit()

