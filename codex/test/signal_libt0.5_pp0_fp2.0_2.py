import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
import sys
import time
import argparse
import threading

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFontDatabase

from . import __version__
from .mainwindow import MainWindow
from . import config
from . import util
from . import cli
from . import updater
from . import updater_qt
from . import log


def main():
    parser = argparse.ArgumentParser(
        prog='nvim-qt',
        description='Neovim client GUI based on PyQt5')
    parser.add_argument(
        '-v', '--version', action='version',
        version='%(prog)s {0}'.format(__version__))
    parser.add_argument(
        '-c', '--config', metavar='FILE',
        help='config file')
