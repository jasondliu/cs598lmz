import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QMessageBox, QAction, QFileDialog, QDialog, QGridLayout, QGroupBox, QCheckBox, QListWidget, QListWidgetItem, QAbstractItemView, QTableWidget, QTableWidgetItem, QHeaderView, QTabWidget, QTextEdit
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import pyqtSlot, Qt, QThread, pyqtSignal, QObject
import os
import subprocess
import re
import time
import shutil
import json
import requests
import threading
import webbrowser
import win32com.client as win32
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32com.client
