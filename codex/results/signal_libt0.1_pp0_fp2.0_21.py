import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtWidgets import QWidget, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("WebEngineView")
        self.setGeometry(0, 0, 800, 600)

        self.webView = QWebEngineView()
        self.webView.load(QUrl("http://www.google.com"))

        layout = QVBoxLayout()
        layout.addWidget(self.webView)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
