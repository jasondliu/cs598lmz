import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtWidgets import QWidget, QVBoxLayout

from PyQt5.QtCore import QTimer

from PyQt5.QtCore import QEventLoop
from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot

import sys
import time
import json

class MyWebEngineView(QWebEngineView):
    def __init__(self, parent=None):
        super(MyWebEngineView, self).__init__(parent)
        self.loadFinished.connect(self.on_loadFinished)

    def on_loadFinished(self):
        print("on_loadFinished")
        self.
