import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

from os import environ
from sys import platform

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt, QSize, QThread, pyqtSignal, QObject
from PyQt5.QtGui import QIcon, QPixmap, QImage

from PIL import Image
from PIL.ImageQt import ImageQt

import imutils
import cv2

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

from picamera.array import PiRGBArray
from picamera import PiCamera

import time
import numpy as np

from threading import Thread

import queue

####################################################################################################

class PiVideoStream:
    def __init
