import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys
import os
import re
import subprocess
import ConfigParser

from PyQt4 import QtCore, QtGui, QtWebKit
from PyQt4.QtGui import QMessageBox, QInputDialog, QLineEdit

from ui_mainwindow import Ui_MainWindow
from ui_about import Ui_About
from ui_add_rule import Ui_AddRule
from ui_edit_rule import Ui_EditRule
from ui_preferences import Ui_Preferences
from ui_help import Ui_Help

# Globals

# Constants
DEFAULT_DATABASE = "~/.config/dnsblocker/dnsblocker.db"
DEFAULT_CONFIG = "~/.config/dnsblocker/dnsblocker.conf"
DEFAULT_LOGFILE = "~/.config/dnsblocker/dnsblocker.log"
DEFAULT_LOGLEVEL = "INFO"

# Global variables

# Classes
class DNSBlockerMainWindow(QtGui
