import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMessageBox, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot, QSize, Qt
from PyQt5.Qt import QThread, pyqtSignal

from PIL import Image
import numpy as np
import cv2
import os
import sys

from src.utils import get_image_size
from src.utils import get_image_size_from_file
from src.utils import get_image_size_from_url
from src.utils import get_image_size_from_base64
from src.utils import get_image_size_from_array
from src.utils import get_image_size_from_bytes
from src.utils import get_image_size_from_pil
from src.utils
