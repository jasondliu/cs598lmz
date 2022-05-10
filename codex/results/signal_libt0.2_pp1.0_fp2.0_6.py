import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtWidgets import QWidget, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('Example')

        self.webview = QWebEngineView()
        self.webview.load(QUrl('https://www.google.com'))

        layout = QVBoxLayout()
        layout.addWidget(self.webview)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
</code>

