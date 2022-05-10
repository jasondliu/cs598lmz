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
        super().__init__()
        self.setWindowTitle("WebEngineView")
        self.setGeometry(0, 0, 800, 600)

        self.webview = QWebEngineView()
        self.webview.load(QUrl("http://www.google.com"))

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.webview)
        self.setLayout(self.layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.on_timeout)
       
