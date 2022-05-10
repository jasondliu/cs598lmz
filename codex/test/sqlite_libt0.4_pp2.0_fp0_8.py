import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys
import os

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QObject, pyqtSignal, QThread

from ui_mainwindow import Ui_MainWindow
from ui_about import Ui_About
from ui_settings import Ui_Settings

from settings import Settings

from version import version

import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')

# TODO:
# - add a "last used" column to the database
# - add a "last used" column to the database
# - add a "last used" column to the database
# - add a "last used" column to the database
# - add a "last used" column to the database
# - add a "last used" column to the database
# - add a "last used" column to the
