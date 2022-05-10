import ctypes
ctypes.windll.user32.SetProcessDPIAware()

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QLabel, QProgressBar, QDialog
from PyQt5.QtCore import Qt, QTimer, QThread, pyqtSignal, QSettings
from PyQt5.QtGui import QIcon, QPixmap

from ui_mainwindow import Ui_MainWindow
from ui_settings import Ui_Dialog
from ui_about import Ui_Dialog as Ui_About
from ui_donate import Ui_Dialog as Ui_Donate
from ui_progress import Ui_Dialog as Ui_Progress

from settings import Settings
from about import About
from donate import Donate
from progress import Progress
from worker import Worker

import os
import sys
import subprocess
import re
import time
import requests
import json
import shutil
import platform
import webbrowser

from pathlib import Path

from PyQt5.QtCore import QObject, pyqt
