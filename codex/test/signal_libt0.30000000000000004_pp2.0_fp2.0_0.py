import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import QUrl, QObject, pyqtSlot, pyqtSignal, QTimer
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtWebChannel import QWebChannel

from PyQt5.QtCore import QUrl, QObject, pyqtSlot, pyqtSignal, QTimer
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtWebChannel import QWebChannel

import sys
import os
import datetime
import time
import json
import urllib.request
import urllib.parse
import urllib.error
import socket
import threading
import re
import traceback
import subprocess
import requests
import random
