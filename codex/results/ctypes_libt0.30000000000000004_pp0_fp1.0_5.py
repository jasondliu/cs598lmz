import ctypes
ctypes.windll.user32.SetProcessDPIAware()

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

import os
import sys

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://google.com"))

        self.setCentralWidget(self.browser)

        self.show()

        self.setWindowTitle("PyQt5 WebBrowser")
        self.setGeometry(100,100,1280,720)


app = QApplication(sys.argv)

window = MainWindow()

app.exec_()
</code>

