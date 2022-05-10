import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl, QObject, pyqtSlot, pyqtSignal, QThread
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QIcon
from PyQt5.QtNetwork import QNetworkRequest

import os
import sys
import json
import time
import logging
import threading
import subprocess
import traceback

from .utils import *
from .config import *
from .browser import *
from .fetcher import *
from .parser import *
from .downloader import *
from .video_converter import *
from .db import *

# import qdarkstyle

logger = logging.getLogger(__name__)

class MainWindow(QMainWindow):
    def __init__(self, parent=None, **kwargs):
        super(MainWindow, self).__init__(
