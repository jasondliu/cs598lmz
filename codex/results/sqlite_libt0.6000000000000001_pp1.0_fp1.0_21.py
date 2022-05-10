import ctypes
import ctypes.util
import threading
import sqlite3
import os
import re
import datetime
import time
import subprocess
from subprocess import Popen, PIPE

#from PyQt5 import QtCore
#from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QThread, QObject
from PyQt5.QtWidgets import QApplication, QMessageBox

#from PyQt5.QtWidgets import QWidget, QApplication
#from PyQt5.QtGui import QPainter, QColor, QFont
#from PyQt5.QtGui import QIcon
#from PyQt5.QtCore import Qt
#from PyQt5.QtCore import QTimer
#from PyQt5.QtCore import pyqtSlot
#from PyQt5.QtCore import pyqtSignal
#from PyQt5.QtWidgets import QMainWindow
#from PyQt
