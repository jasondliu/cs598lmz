import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Import PyQt5 classes
from PyQt5 import QtCore, QtGui, QtNetwork, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebKit import *
from PyQt5.QtWebKitWidgets import QWebPage
from PyQt5.QtWebKitWidgets import QWebView
from PyQt5.QtNetwork import QNetworkAccessManager
from PyQt5.QtNetwork import QNetworkRequest

from bs4 import BeautifulSoup
import sys
import os

# This class is responsible for drawing the graphs using QPainter
class Painter(QWidget):
    def __init__(self, parent = None):
        super(Painter, self).__init__(parent)
        self.setGeometry(0, 0
