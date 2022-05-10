import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication

import sys
import os
import subprocess
import time
import threading
import re
import json
import datetime
from datetime import datetime
import shutil
import glob
import requests
import urllib.request
import urllib
