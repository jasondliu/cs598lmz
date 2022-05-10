import weakref
import cv2
from time import time
import serial
from datetime import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#--------------------------------------------------------------------------------
#----------------------------PACKAGE IMPORTS-------------------------------------
#--------------------------------------------------------------------------------

from PyQt5.QtCore import Qt, QThread, pyqtSignal, QObject
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout, QGroupBox,
                             QHBoxLayout, QLabel, QLineEdit, QMainWindow, QPushButton,
                             QSizePolicy, QSlider, QSpinBox, QVBoxLayout, QWidget, QStackedWidget,
                             QFileDialog, QDialog, QAction, QMenu, QMessageBox, QInputDialog, QRadioButton)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtSql import *
import numpy as np

#--------------------------------------------------------------------------------
#----------------------------GLOBAL VARIABLES
