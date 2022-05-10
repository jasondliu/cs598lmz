import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

import sys
import json
import os
import subprocess
import threading
import time

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit,
                             QCheckBox, QVBoxLayout, QHBoxLayout, QMessageBox,
                             QFileDialog, QPlainTextEdit, QListWidget, QListWidgetItem,
                             QProgressBar, QSpacerItem, QSizePolicy, QAction, QMenu,
                             QSystemTrayIcon, QStyle, QStyleFactory)
from PyQt5.QtGui import QIcon, QPixmap, QFont, QColor, QPalette
from PyQt5.QtCore import Qt, pyqtSignal, QThread, QObject

from gui import Ui_MainWindow
from gui_settings import Ui_Settings
from gui_about import Ui_About
from gui_log import Ui_Log
from gui_custom_preset import
