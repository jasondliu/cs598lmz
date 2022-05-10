import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My Browser')
        self.setGeometry(300, 300, 800, 600)

        self.layout = QVBoxLayout()
        self.web_view = QWebEngineView()
        self.web_view.load(QUrl('https://www.google.com'))
        self.layout.addWidget(self.web_view)
        self.setLayout(self.layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.
