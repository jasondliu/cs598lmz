import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFrame, QAction, QLabel, QLineEdit, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor

import sys, os
import math
import random
import time
import json
import numpy as np
import cv2
import argparse
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path

from skimage import io
from collections import deque
from scipy.misc import imread
from scipy.misc import imresize

from keras.models import model_from_json
from keras.optimizers import SGD

# ##############################
# #############################
