import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import random

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import matplotlib.pyplot as plt

from . import Util
from . import Nodes
from . import Canvas

from . import Events

from . import Plot

from . import Menu

from . import Style

from . import Tools

from . import Layers

from . import Graph

from . import Editor


def get_icon(path):
    return QIcon(os.path.join(os.path.dirname(__file__), 'icons', path))


class App(QMainWindow):
    def __init__(self, debug=False):
        super().__init__()
        if debug:
            self.setWindowTitle('Graph Editor - DEBUG')
        else:
            self.setWindowTitle('Graph Editor')
