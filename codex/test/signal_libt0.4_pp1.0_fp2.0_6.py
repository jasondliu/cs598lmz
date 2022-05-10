import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from . import config
from . import utils
from . import widgets
from . import dialogs
from . import plugins

from .widgets import *
from .plugins import *
from .dialogs import *

from . import __version__

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("QtPlayer")
        self.setWindowIcon(QIcon("icon.png"))
        self.setMinimumSize(900, 580)
        self.setMaximumSize(900, 580)
        self
