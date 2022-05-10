import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

from ui import Ui_MainWindow
from image_processor import ImageProcessor
from image_player import ImagePlayer
from image_loader import ImageLoader


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.image_processor = ImageProcessor()
        self.image_player = ImagePlayer()
        self.image_loader = ImageLoader()

