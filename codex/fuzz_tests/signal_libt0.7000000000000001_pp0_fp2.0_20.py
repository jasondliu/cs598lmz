import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QItemSelectionModel

from . import app_info
from . import csv_handler
from . import excel_handler
from . import image_handler
from . import setting_handler
from . import about_dialog
from . import export_dialog
from . import import_dialog
from . import setting_dialog
from . import model_manager
from . import selection_manager
from . import main_view
from . import main_window_ui


class MainWindow(QtWidgets.QMainWindow):
    """
    Main window of the application.
    """

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)

        self.ui = main_window_ui.Ui_MainWindow()

