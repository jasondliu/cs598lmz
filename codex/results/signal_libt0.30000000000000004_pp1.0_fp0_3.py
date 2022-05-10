import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

import sys

class Browser(QWebEngineView):
    def __init__(self):
        self.view = QWebEngineView.__init__(self)
        self.setWindowTitle('Loading...')
        self.titleChanged.connect(self.adjustTitle)
        self.loadFinished.connect(self.adjustTitle)
        self.setUrl(QUrl("http://google.com"))

    def adjustTitle(self):
        self.setWindowTitle(self.title())
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())
</code>

