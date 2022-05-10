import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtGui, QtCore

import os
import sys

import utils

from ui.mainwindow import Ui_MainWindow
from ui.aboutdialog import Ui_Dialog
from ui.settingsdialog import Ui_Dialog as Ui_SettingsDialog
from ui.datadialog import Ui_Dialog as Ui_DataDialog

from ui.loginwindow import Ui_LoginWindow

from ui.main_widget import Ui_MainWidget
from ui.settings_widget import Ui_SettingsWidget
from ui.data_widget import Ui_DataWidget
from ui.logout_widget import Ui_LogoutWidget

from settings import Settings
from data import Data
from logout import Logout
from main import Main

from ui.settingsdialog import Ui_Dialog as Ui_SettingsDialog

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGu
