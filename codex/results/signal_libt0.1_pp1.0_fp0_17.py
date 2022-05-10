import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle('My Browser')

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://google.com"))

        self.button = QPushButton('Click me')
        self.button.clicked.connect(self.handleButton)

        layout = QVBoxLayout(self)
        layout.addWidget(self.browser)
        layout.addWidget(self.button)

        self.show()

    def handleButton(self):
        self.browser.set
