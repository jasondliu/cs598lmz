import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt5 WebEngine Demo')
        self.setGeometry(5, 30, 1355, 730)

        self.webView = QWebEngineView()
        self.webView.load(QUrl('https://www.google.com'))

        self.btn1 = QPushButton('Load URL')
