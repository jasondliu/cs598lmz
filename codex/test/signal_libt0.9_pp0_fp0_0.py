import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os.path
from parseUI import loadUIs

from qt import QMainWindow, QTabWidget, QAction, QApplication, QFrame, QDockWidget, QUndoGroup, \
                QToolBar, QFont, QIcon
from qt import SIP_VERSION_STR
from qt import PYQT_VERSION_STR
from qt import QT_VERSION_STR
from qt import QT_VERSION
from qt import pyqtSignature

from pydispatch import dispatcher
from dialogs import *
from frame import *
from undoredo import *
from actions import *
from block import *
from dock import *
from parameter import *
from utilities import *
from palettes import *



from model import Model
from widgets import CrumbWidget
from widgets import ModelProvider
from _version import __version__
from _version import QT_VERSION as _QT_VERSION
from uic import getVersion
__version__ = __version__ + '/' + get
