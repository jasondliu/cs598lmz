import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication

from PyQt5.QtCore import QUrl, QFileInfo
from PyQt5.QtGui import QDesktopServices

from mainwindow import MainWindow
from config import Config

# from PyQt5.QtWebKitWidgets import QWebView
# from PyQt5.QtWebKit import QWebSettings

import sys

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Sudoku")
    app.setOrganizationName("Sudoku")
    app.setOrganizationDomain("Sudoku")

    config = Config()

    window = MainWindow()
    window.show()

    # webview = QWebView(window)
    # webview.setFixedSize(800, 600)
    # webview.setWindowTitle("Sudoku")
    # webview.settings().setAttribute(QWebSettings.PluginsEnabled, True
