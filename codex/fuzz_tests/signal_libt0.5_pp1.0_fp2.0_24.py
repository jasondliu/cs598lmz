import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QThread, QTimer

import sys
import os

from ui_mainwindow import Ui_MainWindow
from ui_about import Ui_About
from ui_preferences import Ui_Preferences
from ui_image import Ui_Image
from ui_video import Ui_Video
from ui_settings import Ui_Settings
from ui_settings_image import Ui_Settings_Image
from ui_settings_video import Ui_Settings_Video

from image import Image
from video import Video

