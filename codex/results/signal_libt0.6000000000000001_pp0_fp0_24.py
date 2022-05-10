import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import (QMainWindow, QWidget, QToolTip, QPushButton, QApplication, QLabel, QLineEdit, 
                             QGridLayout, QAction, QFileDialog, QMessageBox, QDesktopWidget, QMenuBar, QMenu,
                             QCheckBox, QComboBox, QListWidget, QTableWidget, QTableWidgetItem, QAbstractItemView,
                             QFrame, QTextEdit)
from PyQt5.QtGui import QFont, QIcon, QIntValidator, QDoubleValidator
from PyQt5.QtCore import QCoreApplication, Qt, QTimer, QDate, QDateTime, QThread, pyqtSignal, QObject

from functools import partial
from datetime import date, datetime, timedelta

import os
import sys
import shutil
import subprocess
import math
import time
import re
import platform

from matplotlib.backends.backend_qt5
