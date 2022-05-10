import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtWidgets, QtGui, Qt

from . import utils
from . import resources
from . import settings
from . import __version__
from . import __author__
from . import __email__

from . import mainwindow
from . import preferences
from . import about

# PyQt5 modules
from PyQt5.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QFileDialog, QMainWindow, QMessageBox, QApplication

# QGIS modules
from qgis.core import QgsApplication

# initialize resources
resources.init_resources()


class MainWindow(QMainWindow):
    """MainWindow class for the application."""

    def __init__(self, parent=None):
        """Constructor for the main window."""
        super().__init__(parent
