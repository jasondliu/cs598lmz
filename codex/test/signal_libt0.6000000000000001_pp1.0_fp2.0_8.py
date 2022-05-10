import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QVBoxLayout
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QPixmap

from PIL import Image

import dlib
import cv2
import numpy as np

from mtcnn.mtcnn import MTCNN
from keras_vggface.vggface import VGGFace
from keras_vggface.utils import preprocess_input
from keras_vggface.utils import decode_predictions

from keras.models import load_model

import os

from tqdm import tqdm

class Thread(QThread):
    changePixmap = pyqtSignal(QPixmap)
    changePixmap2 = pyqtSignal(QPixmap)
