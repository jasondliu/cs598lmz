import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import time
import subprocess
import re
import json

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWebChannel import *

from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication

from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal

from PyQt5.QtCore import QTimer

from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication

from PyQt5.QtCore import QObject
