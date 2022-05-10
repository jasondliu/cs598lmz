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
        self.setWindowTitle('MainWindow')
        self.resize(400, 300)

        self.button1 = QPushButton('Button1')
        self.button1.clicked.connect(self.on_click)

        layout = QVBoxLayout()
        layout.addWidget(self.button1)

        self.setLayout(layout)

    def on_click(self):
        self.webview = QWebEngineView()
        self.webview.load(QUrl("https://
