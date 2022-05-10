import sys, threading

def run():
    sys.stdout.write("\n")
    sys.stdout.flush()
    sys.stderr.write("\n")
    sys.stderr.flush()

threading.Thread(target=run).start()

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
from PyQt4.QtNetwork import *

from PyQt4 import QtCore, QtGui, QtWebKit
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
from PyQt4.QtNetwork import *

from PyQt4.QtCore import QUrl, QTimer
from PyQt4.QtGui import QApplication
from PyQt4.QtWebKit import QWebPage
from PyQt4.QtNetwork import QNetworkAccessManager

import sys, thread
