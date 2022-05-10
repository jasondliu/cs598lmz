import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

import sys
import os
import subprocess
import time
import threading
import queue
import re
import json
import shutil
import glob

from datetime import datetime

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import cv2

from PIL import Image

import tensorflow as tf
from tensorflow.keras.models
