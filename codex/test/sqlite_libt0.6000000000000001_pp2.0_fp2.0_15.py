import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import sys

# from http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/html/
# pyqt4ref.html#pyqt4ref-QtGui.QPixmap
from PyQt4.QtCore import (QObject, QSize, QTimer, Qt)
from PyQt4.QtGui import (
    QApplication, QIcon, QPixmap, QSystemTrayIcon, QWidget)

from . import constants
from . import db
from . import util


def set_libnotify_icon_path(icon_path):
    """
    libnotify.notify() will look for an icon at
    /usr/share/icons/hicolor/scalable/apps/gtd.svg, but if the icon is not
    installed to that location, we can tell libnotify where to find it.
    """
    libnotify = ctypes.cdll.LoadLibrary(ctypes.util.find_library('notify'))
    libnotify
