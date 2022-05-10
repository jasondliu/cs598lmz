import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg

import numpy as np

#import roslib
#roslib.load_manifest('rqt_graph')
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

import cv2

class ImageViewer(QtGui.QWidget):
    def __init__(self, parent=None):
        super(ImageViewer, self).__init__(parent)

        #self.image = QtGui.QImage()
        #self.setAttribute(QtCore.Qt.WA_OpaquePaintEvent)

        self.plot = pg.PlotWidget(self)
        self.plot.setAspectLocked(True)
        self.plot.showGrid(x=True, y=True)

        self.curves = []

        self.image = QtGui.QImage()
        self.
