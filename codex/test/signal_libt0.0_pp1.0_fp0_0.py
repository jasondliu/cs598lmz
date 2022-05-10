import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtWidgets import QWidget, QVBoxLayout

class WebEngineView(QWebEngineView):
    def createWindow(self, QWebEnginePage_WebWindowType):
        new_webview = WebEngineView()
        new_webview.setWindowTitle("New Window")
        new_webview.show()
        return new_webview

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("WebEngineView")
        self.resize(800, 600)
        self.webview = WebEngineView()
        self.webview.load(QUrl("http://www.google.com"))
        layout = QVBoxLayout()
