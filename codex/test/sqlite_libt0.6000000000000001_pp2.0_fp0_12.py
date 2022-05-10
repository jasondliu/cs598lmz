import ctypes
import ctypes.util
import threading
import sqlite3
import logging
import time
import os
import sys
import argparse

from pyqt_settings import *
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSlot, QTimer
from PyQt5.QtGui import QIcon
from pyqt_settings import *


logger = logging.getLogger('root')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('/home/pi/nfc_rfid/logs/nfc_rfid.log')
fh.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger
