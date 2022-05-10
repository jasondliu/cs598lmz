import ctypes
ctypes.windll.user32.SetProcessDPIAware()
from PIL import Image as im 
import numpy as np
from scipy.linalg import sqrtm
from skimage import io 
import time 

from MeshNormal import MeshNormal
from MeshCurvature import MeshCurvature
from GC_dial import GC_dial
from PC_dial import PC_dial
from MP_dial import MP_dial
from HKS_dial import HKS_dial
from SHS_dial import SHS_dial
from WKS_dial import WKS_dial
from ShapeDistance import ShapeDistance
import pyqtgraph as pg


from PyQt5.QtWidgets import *


from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QPlainTextEdit, QFileDialog
#from
