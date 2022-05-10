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
        self.setWindowTitle("My Awesome App")

        layout = QVBoxLayout()

        self.webview = WebEngineView()
        self.webview.load(QUrl("https://www.google.com"))
        layout.addWidget(self.webview)

        self.setLayout(
