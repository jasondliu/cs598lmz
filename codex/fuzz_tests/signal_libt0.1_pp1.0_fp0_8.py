import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('Example')

        self.view = QWebEngineView()
        self.view.load(QUrl('http://www.google.com'))

        self.button = QPushButton('Click me')
        self.button.clicked.connect(self.button_clicked)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.view)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

    def button_clicked(self):
        self.
