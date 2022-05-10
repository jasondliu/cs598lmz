import gc, weakref
import logging
from logging.handlers import RotatingFileHandler
import os
import platform
import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from . import __version__
from . import config
from . import message
from . import models
from . import utils
from . import views


logger = logging.getLogger(__name__)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f'{config.NAME} {__version__}')
        self.setWindowIcon(QtGui.QIcon(config.ICON_PATH))
        self.setMinimumSize(config.MIN_WIDTH, config.MIN_HEIGHT)
        self.resize(config.DEFAULT_WIDTH, config.DEFAULT_HEIGHT)

        self._view = views.MainView(self)
        self.setCentralWidget(self._view)

        self._status_bar = Qt
