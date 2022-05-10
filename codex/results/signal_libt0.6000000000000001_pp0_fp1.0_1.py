import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtCore, QtGui

import pyqtgraph as pg
pg.setConfigOption('background', '#f0f0f0')
pg.setConfigOption('foreground', 'k')

import numpy as np

from lib import flowchart
from lib.pyqtgraph.flowchart import Node
from lib.pyqtgraph.flowchart.library.common import CtrlNode
import lib.pyqtgraph.flowchart.library as fclib
from lib.pyqtgraph.Qt import QtGui, QtCore
import lib.pyqtgraph as pg
import scipy
import scipy.ndimage

import cv2
import scipy.ndimage

class ImageViewer(QtGui.QWidget):
    def __init__(self, parent=None):
        super(ImageViewer, self).__init__(parent)

        # 1) INITIALIZE FLOWCHART
        self.fc = flowchart
