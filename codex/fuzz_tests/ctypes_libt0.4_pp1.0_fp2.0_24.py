import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import sys
import os
import time
import threading
import queue
import socket
import json
import pickle
import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QApplication, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtCore import QSize, QTimer, Qt
from PyQt5.QtGui import QIcon, QPixmap, QImage

from PIL import Image
from PIL.ImageQt import ImageQt

import cv2

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
