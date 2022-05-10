import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import QUrl, QEvent, QTimer, QSize, Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QMessageBox, QSystemTrayIcon, QMenu, QAction, QStyle
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEngineSettings

from downloader import Downloader
from settings import Settings

class MainWindow(QWidget):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.settings = Settings()
        self.downloader = Downloader(self.settings)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Youtube Music Downloader')
        self.setWindowIcon(
