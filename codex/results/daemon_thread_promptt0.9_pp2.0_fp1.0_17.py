import threading
# Test threading daemon.
import urllib2
import webbrowser

# Hack so that all modules can be imported from PySide dir.
import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir)

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebKit import *

import views
from views import utils
import models
from config import *


class BrowserWindow(QMainWindow):

  def __init__(self, app):
    super(BrowserWindow, self).__init__()

    app.addActiveWindow(self)
    self._app = app 

    self.setAcceptDrops(True)
    self.setAttribute(Qt.WA_DeleteOnClose)
    self.setAttribute(Qt.WA_NativeWindow)

    self.setWindowTitle('SGBrowse')
    self.setWindowIcon(QIcon('./static/icons/logo.png'))

   
