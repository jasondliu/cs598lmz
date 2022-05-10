import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('mycompany.myproduct.subproduct.version')

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSignal
from mainwindow import MainWindow
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMessageBox

from updater import Updater
from resources import R, ui, db

class App(QApplication):
    def __init__(self, *args):
        super(App, self).__init__(*args)
        self.main_window = None
        self.check_for_updates()

    def check_for_updates(self):
        self.updater = Updater(R.app_version)
        self.updater.available.connect(self.update_available)
        self.updater.update_downloaded.connect(self.update_downloaded)
        self.updater.update_error.connect(self.update_error
