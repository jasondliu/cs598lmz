import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtCore import QThread, pyqtSignal, QSize, Qt, QTimer
from PyQt5.QtGui import QIcon

from gui.main_window import Ui_MainWindow
from gui.help_dialog import Ui_HelpDialog

from app import MainApp
from utils import get_absolute_path


class HelpDialog(Ui_HelpDialog):

    def __init__(self, dialog):
        Ui_HelpDialog.__init__(self)
        self.setupUi(dialog)


class MainWindow(Ui_MainWindow):

    def __init__(self, window):
        Ui_MainWindow.__init__(self)
        self.setupUi(window)

        self.main_app = MainApp()

        self.help_dialog = QtW
