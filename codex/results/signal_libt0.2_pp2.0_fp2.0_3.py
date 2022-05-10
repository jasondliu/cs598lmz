import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import QUrl, QObject, pyqtSlot, pyqtSignal, QThread, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox, QFileDialog
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineCore import QWebEngineUrlRequestInterceptor, QWebEngineUrlRequestInfo
from PyQt5.QtNetwork import QNetworkRequest

import sys
import os
import json
import time
import re
import requests
import urllib.parse
import hashlib
import base64
import random
import string
import threading
import traceback

from bs4 import BeautifulSoup

from . import config
from . import utils
from . import logger
from . import database
from . import downloader
from . import uploader
from .
