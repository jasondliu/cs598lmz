import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QMainWindow
from Xlib import display, X
from PyQt5.QtCore import QThread, QTimer, pyqtSignal, Qt
from PyQt5.Qt import QApplication
from subprocess import Popen
from common import printc
import time
from variables import STARTING_SCREEN_CHANGE_DELAY
from windows import *
from common import set_wallpaper, get_screen_resolution, get_screen_dimensions
from load_resource import load_resource

import sys
import os.path


def loadQtResource(name):
    return load_resource(name, "qt")


class CheckScreenSize(QThread):
    sig_change_dimensions = pyqtSignal(float, float, int)

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

