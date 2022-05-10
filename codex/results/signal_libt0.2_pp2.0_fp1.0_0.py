import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtCore import QEventLoop
from PyQt5.QtCore import QTimer

from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSlot

from PyQt5.QtCore import QByteArray
from PyQt5.QtCore import QDataStream
from PyQt5.QtCore import QIODevice

from PyQt5.QtNetwork import QTcpServer
from PyQt5.QtNetwork import QHostAddress

from PyQt5.QtCore import QCoreApplication

import sys
import os
import time
import json

class WebPage(QWebEngineView):
    def __init__(self):
        QWebEngineView.__init
