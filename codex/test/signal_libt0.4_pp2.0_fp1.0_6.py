import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import subprocess

from PyQt5.QtCore import QUrl, QStandardPaths, Qt, QObject, pyqtSignal, pyqtSlot, QSize, QTimer
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog, QMessageBox, QMenu, QSystemTrayIcon, QStyle, QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, QLineEdit, QDialog, QDialogButtonBox, QGridLayout, QCheckBox, QListWidget, QListWidgetItem, QAbstractItemView, QComboBox, QGroupBox, QTabWidget, QShortcut, QKeySequenceEdit
from PyQt5.QtNetwork import QNetworkRequest, QNetworkReply, QNetworkAccessManager

from . import config
from . import utils
from . import about
from . import settings
