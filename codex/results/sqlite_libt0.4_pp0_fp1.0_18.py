import ctypes
import ctypes.util
import threading
import sqlite3

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt

from . import util
from . import config
from . import ui
from . import ui_util
from . import window
from . import db
from . import plugins

class MainWindow(window.Window):
    def __init__(self, app):
        window.Window.__init__(self, app)
        self.setWindowTitle("KeePassX")
        self.setWindowIcon(QtGui.QIcon(util.find_data_file("icons/keepassx.png")))
        self.setMinimumSize(400, 300)
        self.setAcceptDrops(True)
        self.app = app
        self.db = None
        self.db_path = None
        self.db_modified = False
        self.db_lock = threading.RLock()
        self.db_timer = QtCore.QTimer(self)
        self.db_timer.timeout.connect(self.db_timer_timeout)
        self
