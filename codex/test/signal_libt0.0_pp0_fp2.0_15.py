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
        new_window.setWindowTitle("QWebEngineView inside a QWidget")
        layout = QVBoxLayout()
        layout.addWidget(new_webview)
        new_window.setLayout(layout)
        new_window.show()
        return new_webview

if __name__ == '__main__':
    app = QApplication(sys.argv)
    webview = WebEngineView()
    webview.load(QUrl("http://www.google.com"))

