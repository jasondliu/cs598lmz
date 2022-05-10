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
        super(WebEngineView, self).contextMenuEvent(event)

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.view = WebEngineView()
        self.view.load(QUrl("http://www.google.com"))
        self.view.show()
        self.button = QPushButton("Click me")
