import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import os
import sys
import time
from collections import namedtuple
import argparse
import json

from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QFileDialog, QTreeWidgetItem
from PySide2.QtWidgets import QListWidgetItem
from PySide2.QtCore import Qt, QFile, QObject, Slot, QDate
from PySide2.QtGui import QPixmap, QPalette, QColor
from PySide2.QtWidgets import QMainWindow, QMessageBox, QAction, QStyleFactory
from PySide2.QtUiTools import QUiLoader
from test import highlight_text, get_full_name

class MainWindow(QMainWindow):
    """Main Window"""

    def __init__(self, ui_file, parent=None):
        super(MainWindow, self).__init__(parent)
        ui_file = QFile("main_window.ui")

