import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog

from ui_mainwindow import Ui_MainWindow
from ui_about import Ui_About
from ui_help import Ui_Help
from ui_settings import Ui_Settings

from classes import *
from functions import *

import sys
import os
import json
import time
import random
import threading

# Глобальные переменные

# Приложение
app = QApplication(sys.argv)

# Окно приложения
main_window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(main_window)

# Окно настроек
settings
