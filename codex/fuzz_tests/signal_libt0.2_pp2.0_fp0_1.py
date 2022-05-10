import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QThread, pyqtSignal

from ui_main import Ui_MainWindow
from ui_about import Ui_AboutWindow
from ui_settings import Ui_SettingsWindow
from ui_progress import Ui_ProgressWindow
from ui_log import Ui_LogWindow

from settings import Settings
from log import Log
from progress import Progress
from about import About
from utils import Utils

from os import path, makedirs, listdir, remove
from shutil import copyfile
from datetime import datetime
from time import sleep

class Main(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(Main, self).__init
