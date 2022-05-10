import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os, os.path
import json
import time

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl

# QWebEnginePage
from PyQt5.QtWebEngineWidgets import QWebEnginePage

# QWebEngineView
from PyQt5.QtWebEngineWidgets import QWebEngineView

# QWebEngineSettings
from PyQt5.QtWebEngineWidgets import QWebEngineSettings

# QWebEngineProfile
from PyQt5.QtWebEngineWidgets import QWebEngineProfile

# QWebEngineScript
from PyQt5.QtWebEngineWidgets import QWebEngineScript

