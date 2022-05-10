import socket
import sys
import time

from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget

from ui.main_window import Ui_MainWindow
from ui.settings_window import Ui_SettingsWindow
from ui.about_window import Ui_AboutWindow

from ui.settings import Settings
from ui.logger import Logger
from ui.server import Server
from ui.client import Client
from ui.utils import Utils

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_start.clicked.connect(self.start_server)
        self.ui.btn_stop.clicked.connect(self.stop_server)
        self.ui.btn_settings.clicked.connect(self.open_settings)
        self.ui.btn_about.clicked
