import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from .ui.welcome_ui import Ui_Welcome

from . import config
from . import utils

class Welcome(QDialog, Ui_Welcome):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.parent = parent

        self.btn_new.clicked.connect(self.new_file)
        self.btn_open.clicked.connect(self.open_file)
        self.btn_recent.clicked.connect(self.open_recent)
        self.btn_settings.clicked.connect(self.open_settings)

