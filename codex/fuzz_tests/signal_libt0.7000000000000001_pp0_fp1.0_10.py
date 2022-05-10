import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui

import pyqtgraph as pg

import sys
import os
import argparse

from sklearn.externals import joblib

import numpy as np
import pandas as pd

from cnmodel.util import h


class PlottingWidget(QtWidgets.QWidget):
    def __init__(self, parent=None, app=None):
        super(PlottingWidget, self).__init__(parent)
        self.app = app
        self.setWindowTitle('Example Plotting Application')
        self.init_ui()
        self.show()

    def init_ui(self):
        self.setLayout(QtWidgets.QVBoxLayout())
        self.plot_widget = pg.PlotWidget(self)
        self.layout().addWidget(self.plot_widget)

        self.plot_widget.set
