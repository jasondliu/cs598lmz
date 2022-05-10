import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QPixmap

from ui_mainwindow import Ui_MainWindow
from ui_about import Ui_About
from ui_settings import Ui_Settings
from ui_progress import Ui_Progress

from settings import Settings
from image_processor import ImageProcessor

class About(QMainWindow, Ui_About):
    def __init__(self, parent=None):
        super(About, self).__init__(parent)
        self.setupUi(self)

class SettingsWindow(QMainWindow, Ui_Settings):
    def __init__(self, parent=None):
        super(SettingsWindow, self).__init__(parent)
        self.setupUi(self)

class ProgressWindow(QMain
