import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt5 WebEngine example')
        self.setGeometry(5, 30, 1355, 730)

        self.webView = QWebEngineView()
        self.webView.load(QUrl('https://www.google.com'))

        self.btn1 = QPushButton('Load URL')
        self.btn1.clicked.connect(self.btn1_clicked)

        self.btn2 = QPushButton('Load HTML')
        self.
