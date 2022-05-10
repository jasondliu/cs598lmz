import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import time
import os
import subprocess
import select
import re
import signal
import json

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QTreeWidgetItem, QMainWindow, QApplication, QMessageBox, QFileDialog, QInputDialog, QDialog, QLabel, QLineEdit, QComboBox, QPushButton, QCheckBox, QProgressBar

from ui.ui_mainwindow import Ui_MainWindow
from ui.ui_about import Ui_About
from ui.ui_add_from_file import Ui_AddFromFile
from ui.ui_add_from_url import Ui_AddFromUrl
from ui.ui_edit import Ui_Edit
from ui.ui_preferences import Ui_Preferences

from utils import *

from utils import _

#from utils
