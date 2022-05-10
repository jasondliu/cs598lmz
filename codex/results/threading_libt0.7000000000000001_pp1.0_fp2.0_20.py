import threading
threading.stack_size(67108864)

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from PyQt5 import QtCore, QtGui, QtWidgets

import threading
import sys
import time
import os
import sys
import errno
import signal
import platform
import logging
import json
import uuid
import socket
import base64

from pydispatch import dispatcher

import utils
import loader

logger = utils.get_logger(__name__)

class Ui_mw(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowIcon(QIcon('icon/icon.png'))
        self.setWindowTitle("Krunker.ioLoader")

class QHLine(QFrame):
    def __init__(self):
        super(QHLine, self).__init
