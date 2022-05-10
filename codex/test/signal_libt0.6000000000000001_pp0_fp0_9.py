import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import QEventLoop
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QThread

from PyQt5.QtCore import QUrl
from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtNetwork import QNetworkAccessManager
from PyQt5.QtNetwork import QNetworkRequest

from PyQt5.QtCore import QEventLoop
from PyQt5.QtCore import QTimer

import sys
import os
import time
import json
import requests

g_app = QApplication(sys.argv)
g_app.setApplicationName("QtNetworkRequest")
g_app.setOrganizationName
