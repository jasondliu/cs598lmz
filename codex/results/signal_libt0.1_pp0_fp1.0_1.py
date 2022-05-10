import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('PyQt5 WebEngine example')
        self.setGeometry(5, 30, 1355, 730)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Create a button, change the text, connect it to a new callback
        self.button = QPushButton('Click me')
        self.button.clicked.connect(self.on_button_clicked)
        self.layout.addWidget(self.button)

        # Create a webview to display the web page
        self
