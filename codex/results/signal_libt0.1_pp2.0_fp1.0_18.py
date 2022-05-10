import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtWidgets import QWidget, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt5 WebEngine Demo')
        self.setGeometry(5, 30, 1355, 730)
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.google.com'))
        self.browser.loadFinished.connect(self._on_load_finished)
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        self.setLayout(layout)

    def _on_load_finished(self):
        self.browser.page().runJavaScript('document.
