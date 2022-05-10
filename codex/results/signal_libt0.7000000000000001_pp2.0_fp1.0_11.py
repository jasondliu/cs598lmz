import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import QThreadPool
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QProgressDialog
from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import pyqtSignal

import resource

import os
import errno    
import datetime
import subprocess
import math

import custom_plot
import table_widget

import
