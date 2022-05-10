import weakref

from PyQt5.QtCore import QObject, QThread, QTimer, pyqtSlot, pyqtSignal, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QAction, QApplication, QDialog,
                             QHBoxLayout, QLabel, QLineEdit, QPushButton,
                             QVBoxLayout, QWidget)

from . import utils
from .utils import log, log_traceback
from .i18n import tr
from .qt import *


class Worker(QObject):
    ''' Thread that does the work. '''

    sig_done = pyqtSignal(object)
    sig_error = pyqtSignal(object)

    def __init__(self, fn, *args, on_done=None, on_error=None, parent=None):
        QObject.__init__(self, parent)
        self.fn = fn
        self.args = args
        self.on_done = on_done
