import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtCore import QObject, pyqtSignal

import sys
import os

from multiprocessing import Process, Queue
from collections import deque

import cv2
import numpy as np
import os
import sys
import time
import json
import threading
import signal

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QUrl, QTimer, QThread, pyqtSignal
