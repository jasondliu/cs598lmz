import ctypes
import ctypes.util
import threading
import sqlite3

from datetime import datetime
from time import sleep

from PyQt5 import QtCore, QtGui, QtWidgets

from . import lib
from . import config

from . import main_ui
from . import settings_ui
from . import add_ui
from . import edit_ui
from . import about_ui

from . import database

from . import config

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = main_ui.Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("NPC")

        self.ui.action_Quit.triggered.connect(self.close)
        self.ui.action_Settings.triggered.connect(self.show_settings)
        self.ui.action_About.triggered.connect(self.show_about)

        self.ui.add_button.clicked.connect(self.show_add_dialog)
        self
