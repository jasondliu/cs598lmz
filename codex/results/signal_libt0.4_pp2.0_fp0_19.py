import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import sys
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QT_VERSION_STR
from PyQt5.Qt import PYQT_VERSION_STR
from sip import SIP_VERSION_STR
from . import __version__
from .main_window import MainWindow
from .config import config
from . import logger
from . import utils
from . import qtutils
from . import resources


def excepthook(type_, value, traceback_):
    """Global function to catch unhandled exceptions.

    :param type_: exception type
    :param value: exception value
    :param traceback_: traceback object
    """
    logger.exception("Uncaught exception", exc_info=(type_, value, traceback_))


def main():
    """Main entry point into the application."""
    sys.excepthook = excepthook

    app = QApplication(sys.argv
