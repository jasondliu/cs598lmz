import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import pyqtgraph as pg

from . import utils


class ImageView(QWidget):
    def __init__(self, parent=None):
        super(ImageView, self).__init__(parent)

        self.image_item = None
        self.image_data = None
        self.image_view = None
        self.image_hist = None
        self.image_roi = None
        self.image_roi_hist = None
        self.image_roi_data = None
        self.image_roi_mask = None
        self.image_roi_mask_data = None
        self.image_roi_mask_data_index = 0
        self.image_roi_mask_data_index_max = 0
        self.image_
