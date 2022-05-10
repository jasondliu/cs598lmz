import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
import sys
import time

from PyQt5.QtCore import QTimer, QThread, pyqtSignal, QCoreApplication
from PyQt5.QtGui import QFont, QFontMetrics
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QMainWindow, QPushButton, QLineEdit, QMessageBox, QDesktopWidget, QDialog, QDialogButtonBox

# Import PyQt5.QtWebKitWidgets as web
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings

# Import QWebEngineView

import PyQt5.QtNetwork as net

from PyQt5.QtCore import *

import threading

import socket

import json

import requests

import ast

import hashlib

import base64

import urllib

import hmac
