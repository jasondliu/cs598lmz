import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QCheckBox, QFileDialog, QMessageBox, QProgressBar, QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView, QComboBox
from PyQt5.QtCore import QThread, pyqtSignal
import sys
import os
import json
import re
import time
import subprocess
import traceback
import shutil
import threading
from pathlib import Path
from os.path import expanduser

from . import utils
from . import config
from . import log
from . import version
from . import update
from . import settings

# from . import update

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.logger = log.get_logger
