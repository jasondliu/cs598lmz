import ctypes
import ctypes.util
import threading
import sqlite3
from datetime import datetime
from typing import Optional

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import pyqtSignal, QThreadPool
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QMainWindow, QHBoxLayout,
                             QWidget, QDesktopWidget, QAction, QFileDialog)

from my_lib import ScanThread
from my_ui import Ui_MainWindow, MyQWidgetItem


class MyQMainWindow(QMainWindow, Ui_MainWindow):
    data_file_name = 'data.db'
    mach_loc = os.path.join(os.getcwd(), 'machines.py')

    def __init__(self, parent=None):
        super(MyQMainWindow, self).__init__(parent)
        self.setupUi(self)
