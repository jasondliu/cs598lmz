import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

class WebEngineView(QWebEngineView):
    def contextMenuEvent(self, event):
        print("contextMenuEvent")

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My Browser')

        self.browser = WebEngineView()
        self.browser.setUrl(QUrl("http://google.com"))

        self.button = QPushButton('Back')
        self.button.clicked.connect(self.on_button_clicked)
