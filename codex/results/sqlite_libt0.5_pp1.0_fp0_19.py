import ctypes
import ctypes.util
import threading
import sqlite3
from sqlite3 import Error
import datetime
import time
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import QVariant, QModelIndex
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from PyQt5.QtCore import QObject, pyqtSignal
import subprocess
import os
import re
from subprocess import Popen, PIPE, STDOUT
import subprocess
import os
import re
from subprocess import Popen, PIPE, STDOUT
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
import sys
from PyQt5
