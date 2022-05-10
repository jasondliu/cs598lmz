import weakref
import re
import os
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from . import utils
from . import settings
from . import resources
from . import dialogs
from . import commands
from . import widgets
from . import model
from . import view


class MainWindow(QMainWindow):
    """Main window for the application."""

    def __init__(self, app, **kwargs):
        super(MainWindow, self).__init__(**kwargs)

        self.app = weakref.ref(app)
        self.model = None
        self.view = None
        self.settings = None
        self.recent_files = []

        self.setWindowTitle("Pympress")
        self.setWindowIcon(QIcon(":/icons/pympress.svg"))

        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        self.create_actions()
