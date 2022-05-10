import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QMessageBox
from PyQt5.QtCore import pyqtSlot

from PyQt5.QtCore import QThread, pyqtSignal

import sys
import time
import os
import json
import requests
import re
import random
import string
import base64
import hashlib
import hmac
import urllib.parse

from bs4 import BeautifulSoup

import configparser

import logging
logging.basicConfig(level=logging.INFO)

class MyThread(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def __
