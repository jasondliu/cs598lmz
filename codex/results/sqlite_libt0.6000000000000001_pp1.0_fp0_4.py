import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys
import os
import signal
import socket
import subprocess
import traceback
from collections import deque

from PyQt5.QtCore import Qt, QSize, QRect, QUrl, QTimer, QEvent, QPoint, pyqtSignal
from PyQt5.QtGui import QKeySequence, QIcon, QPixmap, QImage, QPalette, QColor, QDesktopServices
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QMenu, QLabel, QAbstractItemView, QFrame,
                             QApplication, QShortcut, QAction, QToolTip, QSystemTrayIcon, QMenuBar, QStyle, QDialog,
                             QGridLayout, QLineEdit, QListWidget, QListWidgetItem, QMessageBox, QProgressBar, QTextEdit,
                             QDialogButtonBox, QComboBox, QCheckBox, QTabBar, QSizePolicy)

from galacteek import ensure, logUser, logDebug, log
