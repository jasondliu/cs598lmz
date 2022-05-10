import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

import os
import sys
import subprocess
import json
import time
import threading
import requests
import urllib
import re

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Youtube Downloader'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
        self.download_thread = None
        self.download_process = None
        self.download_progress = None
        self.download_progress_value = 0
        self.download_progress_max = 0
