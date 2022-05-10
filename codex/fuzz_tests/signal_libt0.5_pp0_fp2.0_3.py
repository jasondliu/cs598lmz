import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


import sys
import os
import time

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils.utils import *
from utils.yolo import YOLO, detect_video
from PIL import Image

from models.yolo_model import Yolo
from models.keras_model import Keras
from models.tf_model import TF

from keras import backend as K
#from keras.backend.tensorflow_backend import set_session


import tensorflow as tf
from tensor
