import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel,
                             QApplication, QProgressBar)
from PyQt5.QtCore import QBasicTimer, QThread, pyqtSignal, QEventLoop
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import (QWebEnginePage, QWebEngineView)

import sys
import time
import random
from datetime import datetime

import tushare as ts
from bs4 import BeautifulSoup

class Crawler(QThread):
    # 定义信号
    signal = pyqtSignal(tuple)
    def __init__(self, parent=None):
        super(Crawler, self).__init__(parent)
