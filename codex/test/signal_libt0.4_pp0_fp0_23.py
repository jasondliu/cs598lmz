import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtWidgets

from . import mainwindow
from . import settings
from . import about
from . import help
from . import update
from . import utils
from . import constants
from . import updater
from . import updater_gui

import sys
import os
import platform
import time
import shutil
import subprocess
import re
import json
import traceback
import logging

from . import logging_config
logger = logging.getLogger(__name__)

class MainWindow(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.setWindowIcon(QtGui.QIcon(os.path.join(constants.IMAGE_DIR, 'icon.png')))

