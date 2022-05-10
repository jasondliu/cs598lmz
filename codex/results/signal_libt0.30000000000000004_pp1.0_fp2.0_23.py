import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLabel, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

from os import path

from . import config
from . import utils
from . import __version__

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("{} v{}".format(config.APP_NAME, __version__))
        self.setWindowIcon(QIcon(path.join(config.APP_DIR, "icon.png")))
        self.setMinimumSize(400, 200)
        self.setMaximumSize(400, 200)
        self.setFixedSize(400, 200)
        self.setStyleSheet(config.STYLE_SHEET)

        self.centralWidget = Q
