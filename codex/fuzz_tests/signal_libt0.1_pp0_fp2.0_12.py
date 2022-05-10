import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('PyQt5 WebEngine example')
        self.setGeometry(5, 30, 1355, 730)

        self.layout = QVBoxLayout()

        self.webview = QWebEngineView()
        self.webview.load(QUrl('https://www.google.com'))

        self.layout.addWidget(self.webview)
        self.setLayout(self.layout)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
