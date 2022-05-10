import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QMessageBox, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtCore import Qt

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from datetime import datetime
from os import path

from image_processing import image_processing
from image_processing import image_processing_params
from image_processing import image_processing_params_default
from image_processing import image_processing_params_help
from image_processing import image_processing_params_help_default

from image_processing_utils import image_processing_utils

from image_processing_gui_utils import image_processing_gui_utils

class image_processing_gui(QWidget):
    def __init__(self):
        super().__
