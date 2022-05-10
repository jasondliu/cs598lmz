import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtWidgets import QWidget, QVBoxLayout

from PyQt5.QtCore import QTimer

import sys

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('PyQt5 WebEngine Demo')
        self.setGeometry(5, 30, 1355, 730)

        self.webView = QWebEngineView()
        self.webView.load(QUrl('https://www.google.com'))

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.webView)

        self.setLayout(self.mainLayout)

        self.timer = QTimer()
        self
