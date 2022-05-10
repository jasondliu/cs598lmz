import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import argparse

import numpy as np
import matplotlib.pyplot as plt

import pydicom

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QComboBox, QSpinBox, QDoubleSpinBox
from PyQt5.QtWidgets import QPushButton, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal

# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from dicom_tools.dicom_series_reader import DicomSeriesReader
from dicom_tools.dicom_series_viewer import D
