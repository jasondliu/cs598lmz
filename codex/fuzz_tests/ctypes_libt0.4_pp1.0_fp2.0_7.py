import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import sys
import os
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QLineEdit
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap, QImage, QPainter, QPen, QBrush, QColor, QFont
from PyQt5.QtMultimedia import QSound

from PIL import Image
from PIL.ImageQt import ImageQt

from random import randint

from collections import deque
from collections import namedtuple

from pygame import mixer

from threading import Thread

from multiprocessing import Process

import cv2

#from keras.models import load_model

#from keras.applications.mobilen
