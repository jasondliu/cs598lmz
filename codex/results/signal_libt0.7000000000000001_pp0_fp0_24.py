import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, QApplication, QMessageBox, QLineEdit, QFileDialog
from PyQt5.QtCore import QSize    

from torch.utils.data.dataset import Dataset
from torchvision import transforms
from torch.utils.data import DataLoader
import torch.optim as optim
import torch.nn as nn
import torch
from torch.autograd import Variable

import glob
import numpy as np
import os
from PIL import Image
import matplotlib.pyplot as plt
from time import time

from utils import *
from models import *
from data_loader import *

class MainWindow(QMainWindow, main_window.Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__
