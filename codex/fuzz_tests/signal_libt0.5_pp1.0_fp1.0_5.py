import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import time

import numpy as np
import pandas as pd

from PyQt5 import QtGui, QtWidgets, QtCore

import PyQtGraph as pg
pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')

import pyqtgraph.exporters

from . import utils

class ImageViewer(pg.ImageView):
    def __init__(self, parent, image, title=None, image_name=None,
                 show_roi=False, show_crosshair=True, show_histogram=True,
                 show_contrast=True, show_roi_histogram=True,
                 show_roi_contrast=True, show_color_histogram=True,
                 show_color_contrast=True, show_color_roi_histogram=True,
                 show_color_roi_contrast=True,
                 show_roi
