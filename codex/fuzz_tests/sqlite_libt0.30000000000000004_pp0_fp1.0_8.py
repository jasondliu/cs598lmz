import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys
import subprocess

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QFileDialog, QTableWidgetItem, QTableWidget
from PyQt5.QtCore import QTimer, QThread, pyqtSignal, QObject, QDateTime, Qt
from PyQt5.QtGui import QPixmap, QIcon

from ui_mainwindow import Ui_MainWindow
from ui_about import Ui_About

from time import sleep
from datetime import datetime

from ctypes import *

# TODO:
# - Add a "don't show again" checkbox to the "no devices found" dialog
# - Add a "don't show again" checkbox to the "no devices found" dialog
# - Add a "don't show again" checkbox to the "no devices found" dialog
# - Add a "don't show again" checkbox to the "no devices found" dialog
