import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import re
import time
import datetime
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import QApplication, QMainWindow, QWidget, QFileDialog, QMessageBox, QProgressDialog
from PyQt4.QtCore import QThread, SIGNAL, QObject, QString, pyqtSignal, QTimer, QVariant, QDir, QFileInfo, QDateTime
from PyQt4.Qt import QDir, QFileInfo, QDateTime
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.Qt import *
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSignal, pyqtSlot
from PyQt4.QtGui import QApplication, QMainWindow, QWidget, QFileDialog, QMessageBox, QProgressDialog
from PyQ
