import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import threading
import time
import subprocess
import re

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile

import configparser
import json
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class MainWindow(QWebEngineView):
    def __init__(self, url, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QtWebEngineView: %s" % url)
        self.setWindowIcon(QIcon(os.path.join(os.path.dirname(__file__), "icon.svg")))
        self.setUrl(QUrl(url))
        self.set
