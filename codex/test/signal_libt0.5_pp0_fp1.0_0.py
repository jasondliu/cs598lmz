import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import Qt

from .Ui_MainWindow import Ui_MainWindow
from .AboutDialog import AboutDialog
from .ImportDialog import ImportDialog
from .ExportDialog import ExportDialog

from . import util
from . import config
from . import database
from . import settings
from . import search
from . import files
from . import sync
from . import tag
from . import template
from . import settings
from . import log
from . import report
from . import image

import os
import sys
import json
import time
import shutil
import traceback
import webbrowser
import subprocess
import platform
import threading
import queue
import datetime

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        Qt
