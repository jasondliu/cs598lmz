import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon

import sys
import os

from ui_mainwindow import Ui_MainWindow
from ui_settings import Ui_Dialog
from ui_about import Ui_Dialog as Ui_Dialog_about
from ui_help import Ui_Dialog as Ui_Dialog_help

import settings
from settings import Settings
from settings import SettingsError
from settings import SettingsFileError
from settings import SettingsFileNotFoundError
from settings import SettingsFileNotWritableError

from settings import SettingsFileNotFoundError
from settings import SettingsFileNotWritableError

from settings import SettingsNotFoundError
from settings import SettingsNotWritableError

from settings import SettingsNotFoundError
from settings import SettingsNotWritableError

from settings
