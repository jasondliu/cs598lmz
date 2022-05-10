import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtWidgets import QMessageBox

from widgets import main_window

class MainWindow(QMainWindow, main_window.Ui_MainWindow):
    """Main Window"""
    def __init__(self, parent=None):
        super().__init__(parent)
        # init
        self.setupUi(self)
        self.setWindowIcon(QIcon('icon.png'))
        self.setFixedSize(self.size())

        # QSystemTrayIcon
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon('icon.png'))
        self.
