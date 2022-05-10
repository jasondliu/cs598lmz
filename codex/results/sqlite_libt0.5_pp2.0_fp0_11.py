import ctypes
import ctypes.util
import threading
import sqlite3
import hashlib
import os
import time
import datetime
import sys
from pprint import pprint
import json

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *
from PyQt4.QtNetwork import *

from lib.config import Config

config = Config()

class Browser(QWebView):
    def __init__(self, display=True, clear_cache=False, clear_cookies=False, clear_history=False, proxy=None, user_agent=None, wait=0, js_profile=None, ignore_ssl_errors=False, script=None, html=None, logger=None, html_logger=None):
        #QtGui.QApplication.setGraphicsSystem('raster')
        self.app = QApplication(sys.argv)
        QWebView.__init__(self)
        if js_profile:
            self.profile = QWebProfile()
            self.profile.setPersistentStoragePath(js_
