import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
import sys
import cv2
import numpy as np
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QGuiApplication, QImage, QPixmap
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtWebEngine import QtWebEngine
import time
import requests
from PyQt5.QtWebEngineCore import QtWebEngineCore
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt, QTimer

class WebView(QtWebEngineWidgets.QWebEngineView):

    # Class constructor
    def __init__(self, parent=None):
        super(WebView, self).__init__(parent)
        #
