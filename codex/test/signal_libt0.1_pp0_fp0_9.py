import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtWidgets import QWidget, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('PyQt5 WebEngine demo')
        self.setGeometry(5, 30, 1355, 730)

        self.webView = QWebEngineView()
        self.webView.load(QUrl('https://www.google.com'))

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.webView)
        self.setLayout(self.layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
