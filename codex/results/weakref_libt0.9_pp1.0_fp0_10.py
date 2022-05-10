import weakref
import os

if sys.platform == "win32":
    # make sure we use bundled PyQt5 on windows
    # (bundled version does not contain ugly console window)
    sys.path.insert(0, "C:/Program Files (x86)/GNS3")
    from .qt import sip
    sip.setdestroyonexit(False)
else:
    from .qt import sip

try:
    from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QFileDialog
    from PyQt5.QtCore import pyqtSignal, QObject, QTimer, QProcessEnvironment
    from PyQt5.QtGui import QFontDatabase, QFont
except ImportError:
    sys.exit("Cannot import from PyQt5: Do \"pip3 install pyqt5\"")

from . import consts
from .config import Config
from .local_server_config import LocalServerConfig
from .update_manager import UpdateManager
from .main_window import MainWindow
from .logger import logger
from .t
