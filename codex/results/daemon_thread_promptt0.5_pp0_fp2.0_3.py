import threading
# Test threading daemon
from time import sleep

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMessageBox

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QObject
from PyQt5.QtCore import QThread
from PyQt5.QtCore import QTimer

from PyQt5.QtGui import QIcon

from PyQt5.Qt import QSettings

from PyQt5.Qt import Qt

import logging

import os
import sys

from PyQt5.Qt import PYQT_VERSION_STR
