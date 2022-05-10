import ctypes
ctypes.windll.user32.SetProcessDPIAware()

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

import sys

class Browser(QWebEngineView):
    def __init__(self):
        self.view = QWebEngineView.__init__(self)
        self.setWindowTitle('Loading...')
        self.titleChanged.connect(self.adjustTitle)
        self.load(QUrl("https://www.google.com"))
        self.show()

    def adjustTitle(self):
        self.setWindowTitle(self.title())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = Browser()
    sys.exit(app.exec_())
</code>

