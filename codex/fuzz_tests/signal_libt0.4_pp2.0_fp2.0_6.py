import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QCheckBox, QDialog, QDialogButtonBox, QFileDialog, QMessageBox, QProgressBar, QTabWidget
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5 import QtCore

from threading import Thread
import time
import os
import sys
import subprocess

from . import utils
from .utils import *
from . import config
from .config import *
from . import logger
from .logger import *
from . import file_utils
from .file_utils import *
from . import png2ico
from .png2ico import *


class Worker(QThread):
    """
    Worker thread class
    """
    # Signals
    sig_
