import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtWidgets import QWidget, QVBoxLayout

class WebEngineView(QWebEngineView):
    def createWindow(self, QWebEnginePage_WebWindowType):
        new_webview = WebEngineView()
        new_window = QWidget()
        new_window.setWindowTitle("New Window")
        new_window.resize(640, 480)
        new_window.show()
        new_window.setLayout(QVBoxLayout())
        new_window.layout().setContentsMargins(0, 0, 0, 0)
        new_window.layout().addWidget(new_webview)
        return new_webview

app = QApplication(sys.argv)
