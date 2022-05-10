import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import subprocess
import time

try:
    from PyQt4 import QtGui, QtCore
    from PyQt4 import QtSvg
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
except:
    from PyQt5 import QtGui, QtCore
    from PyQt5 import QtSvg
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    from PyQt5.QtWidgets import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

