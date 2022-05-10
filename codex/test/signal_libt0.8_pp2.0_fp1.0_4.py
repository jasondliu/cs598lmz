import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QApplication, QMainWindow, QPainter, QPen, QColor, QBrush
from PyQt4 import QtGui
from PyQt4 import QtCore
import sys
import os
import cv2
# from picamera.array import PiRGBArray
# from picamera import PiCamera
import time
import numpy as np
# from PIL import Image

# import RPi.GPIO as GPIO
# # taken from https://www.dexterindustries.com/GoPiGo/programming/python-programming-for-the-raspberry-pi-gopigo/
# import easygopigo3 as easy
# import time
# import numpy as np
# # import Cozmo
# # import threading
# # import sys
# # import asyncio
# import requests


