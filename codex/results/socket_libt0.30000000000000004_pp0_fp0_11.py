import socket
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QThread, pyqtSignal

from ui.main_window import Ui_MainWindow
from ui.about_window import Ui_AboutWindow
from ui.settings_window import Ui_SettingsWindow
from ui.progress_window import Ui_ProgressWindow

from settings import Settings
from client import Client
from server import Server
from utils import Utils


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.settings = Settings()
        self.settings.load()
        self.settings.save()

        self.setWindowTitle(self.settings.app_name)
        self.setWindowIcon(QIcon(self.settings.app_icon))

        self.client = Client()
       
