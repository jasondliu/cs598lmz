import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal

from main_ui import Ui_MainWindow
from batch_ui import Ui_BatchWindow
from about_ui import Ui_AboutWindow
from about_qt_ui import Ui_AboutQtWindow
from help_ui import Ui_HelpWindow
from preferences_ui import Ui_PreferencesWindow

from . import utils
from . import preferences
from . import batch
from . import about
from . import help
from . import qt_utils
from . import validate
from . import settings
from . import log

from . import version

logger = log.get_logger(__name__)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):

