import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QMessageBox
from PyQt5.QtCore import Qt

from PyQt5.QtGui import QIcon

from PyQt5.QtCore import QTimer

import sys
import os
import json
import time
import datetime
import random
import requests
import re
import threading

from bs4 import BeautifulSoup

import urllib.request
import urllib.parse
