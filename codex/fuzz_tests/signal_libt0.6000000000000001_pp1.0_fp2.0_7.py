import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QWidget, QGridLayout, QPushButton, QFileDialog
from PyQt5.QtCore import QUrl, QThreadPool, QObject, pyqtSignal, QRunnable, pyqtSlot, QThread
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget

from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize

import os
import sys
import shutil
import subprocess

import time
import datetime
import hashlib

from threading import Lock

import urllib.request
import threading

from os.path import basename
from urllib.parse import urlsplit

from queue import Queue

from multiprocessing import Process, Value, Array

import atexit
