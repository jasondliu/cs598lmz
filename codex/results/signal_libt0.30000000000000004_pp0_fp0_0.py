import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest

from PyQt5.QtCore import QUrl

from PyQt5.QtCore import QFile, QTextStream

from PyQt5.QtCore import QEventLoop, QTimer

from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal

import sys
import os
import time
import json
import re
import socket
import threading
import urllib.request
import urllib.parse
import urllib.error
import http.cookiejar
import ssl
import traceback
import codecs

import logging
import logging.handlers
