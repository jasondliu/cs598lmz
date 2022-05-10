import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import time
import os
import subprocess
import platform
import shutil

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtMultimedia import QSound
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QLineEdit, QMessageBox, QPushButton, QComboBox, QFileDialog, QFrame, QTextEdit, QCheckBox, QGroupBox, QGridLayout
from PyQt5.QtWidgets import QAction, QMenuBar, QMenu, qApp, QFrame, QLabel, QVBoxLayout
from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QAbstractItemView, QTableWidgetItem, QTableWidget, QDialog, QDialogButtonBox
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette, QBrush
