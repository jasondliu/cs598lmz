import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
"""

from sys import argv
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import numpy as np
import rospy

from std_msgs.msg import String, Float64

from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

from qt_gui_py_common.worker_thread import WorkerThread
from qt_gui_py_common.console_formatter import ConsoleFormatter
from qt_gui_py_common.plugin import Plugin

from python_qt_binding import loadUi
from python_qt_binding.QtWidgets import QWidget

import cv2
import os

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2Q
