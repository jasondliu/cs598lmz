import socket
import time
import traceback

import numpy as np

import pyqtgraph_karl as pg
from PyQt5 import QtNetwork
from PyQt5.QtCore import Qt, QTimer, pyqtSignal, QSettings
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QVBoxLayout,
                             QPushButton, QHBoxLayout, QLineEdit, QCheckBox)

from bsread.data.control_data import ControlMessage

from .frame import Frame
from .decoding import decode
from .profiling import Profile
from .version import __version__


class Subscription:
    """
    Manage a BSREAD subscription.
    """
    connected = pyqtSignal()
    disconnected = pyqtSignal()

