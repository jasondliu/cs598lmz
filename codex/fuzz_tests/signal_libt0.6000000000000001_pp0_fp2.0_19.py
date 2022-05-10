import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QPushButton,QVBoxLayout,QHBoxLayout,QTableWidget,QTableWidgetItem,QComboBox
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap
import cv2
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QPushButton,QVBoxLayout,QHBoxLayout,QTableWidget,QTableWidgetItem,QComboBox
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap
import cv2
import os
from datetime import datetime
import time
import threading
import random
