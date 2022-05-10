import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from src.gui.gui import MainWindow

def main():
    app = QApplication([])
    app.setApplicationName("CryptoTracker")
    app.setApplicationVersion("0.0.1")
    app.setOrganizationDomain("cryptotracker.org")
    app.setOrganizationName("CryptoTracker")

    view = QWebEngineView()
    view.setUrl(QUrl("https://www.google.com"))
    view.show()

    window = MainWindow()
    window.show()

    app.exec_()

if __name__ == "__main__":
    main()
