import ctypes
import ctypes.util
import threading
import sqlite3
from collections import namedtuple
import os
import sys
from decimal import Decimal
from queue import Queue
from datetime import datetime
import json

from bitcoinrpc.authproxy import AuthServiceProxy

from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtCore import Qt, QTimer, QThread
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton, QLabel, QFrame, QTextEdit, QMessageBox, QFileDialog)
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PyQt5.QtSql import QSqlDatabase

CLib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('c'))
CLib.strnlen.argtypes = [ctypes.c_char_p, ctypes.c_size_t]
CLib.strnlen.restype = ctypes.c_size_t
