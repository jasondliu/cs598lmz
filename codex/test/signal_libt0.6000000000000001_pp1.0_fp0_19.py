import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtPrintSupport import *

import os
import sys

from UI.mainwindow import Ui_MainWindow
from UI.search import Ui_search_dialog
from UI.bookmark import Ui_bookmark_dialog
from UI.history import Ui_history_dialog
from UI.download import Ui_download_dialog
from UI.setting import Ui_setting_dialog


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.initUI()
        self.show()

