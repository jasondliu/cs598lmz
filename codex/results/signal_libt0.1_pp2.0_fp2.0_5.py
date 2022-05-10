import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

class WebEngineView(QWebEngineView):
    def createWindow(self, QWebEnginePage_WebWindowType):
        new_webview = WebEngineView()
        new_webview.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        new_webview.show()
        return new_webview

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('WebEngineView')
        self.setGeometry(5
