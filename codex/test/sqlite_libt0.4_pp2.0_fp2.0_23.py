import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import datetime
import traceback

from PyQt5.QtCore import QObject, pyqtSignal, QTimer, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon

from . import config
from . import utils
from . import settings
from . import db
from . import ui
from . import bt
from . import version

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.ui = ui.Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle(version.APPNAME)
        self.setWindowIcon(QIcon(config.ICON_PATH))

        self.ui.actionSettings.triggered.connect(self.on_settings)
