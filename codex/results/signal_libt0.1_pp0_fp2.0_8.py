import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtWidgets import QWidget, QVBoxLayout

class WebEngineView(QWebEngineView):
    def createWindow(self, QWebEnginePage_WebWindowType):
        new_webview = WebEngineView()
        new_window = QWidget.createWindowContainer(new_webview)
        new_window.setWindowTitle("Loading...")
        new_window.resize(800, 600)
        new_window.show()
        return new_webview

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("WebEngineView")
        self.resize(800, 600)
        self.webview = WebEngineView()
        self.web
