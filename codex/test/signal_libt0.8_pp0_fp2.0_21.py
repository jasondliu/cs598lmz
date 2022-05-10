import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Import PyQt5 classes
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebKit import *
from PyQt5.QtWebKitWidgets import QWebPage
from PyQt5.QtNetwork import *
from PyQt5.QtCore import QUrl

# Get path of current directory
import inspect, os
filename = inspect.getframeinfo(inspect.currentframe()).filename
path = os.path.dirname(os.path.abspath(filename))

# Import module classes
import configuration
import navigation


class Renderer(QWebPage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
