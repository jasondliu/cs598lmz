import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit, QFileDialog, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal

from PyQt5.QtGui import QIcon

import sys
import os
import time
import json
import re
import requests
import urllib.request
import urllib.parse
import urllib.error
import threading
import queue
