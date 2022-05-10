import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# from PySide import QtCore, QtGui
# from PySide.QtCore import *
# from PySide.QtGui import *

# from PySide.QtGui import QApplication, QMainWindow
# from PySide.QtCore import QFile
# from PySide.QtUiTools import QUiLoader

import sys
import os

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from PyQt4.QtGui import QApplication, QMainWindow
from PyQt4.QtCore import QFile
from PyQt4.uic import loadUi

import json

import numpy as np
import cv2

import matplotlib.pyplot as plt

import time

# import cv2

# import numpy as np

# import matplotlib.pyplot as plt

import py
