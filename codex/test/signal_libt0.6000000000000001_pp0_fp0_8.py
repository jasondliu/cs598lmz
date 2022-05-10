import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.Qt import QTimer
import sys
from cv2 import cv2
import numpy as np
from uuid import uuid4
import random
from datetime import datetime
import threading
from time import sleep

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from PyQt5.QtCore import QDate, QDateTime, QTime
from PyQt5.QtWidgets import QApplication, QComboBox, QDateTimeEdit, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QGridLayout, QLabel, QSizePolicy, Q
