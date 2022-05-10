import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

from . import config
from . import utils
from . import backend
from . import gui
from . import gui_utils
from . import gui_widgets

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("PyQt5")
        self.setWindowIcon(QIcon(config.ICON_PATH))
        self.setMinimumSize(config.WINDOW_MIN_WIDTH, config.WINDOW_MIN_HEIGHT)
        self.setMaximumSize(config.WINDOW_MAX_WIDTH, config.WINDOW_MAX_HEIGHT)
