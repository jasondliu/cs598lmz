import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import pyqtSlot, QSize, Qt, QUrl, QTimer
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QAction
from PyQt5.QtWebEngineWidgets import QWebEngineView

from ui.mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('icon.png'))

        # Create a QWebEngineView
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://127.0.0.1:5000/"))
        self.browser.setMinimumSize(QSize(800, 600))

