import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg

colors=['b','g','r','c','m','y','k','#FF8000','#ADFF2F','#7FFFD4','#FF1493','#FF4500','#FFD700','#F0E68C','#FFDAB9','#B0E0E6','#FFA07A','#FAEBD7','#BDB76B','#20B2AA']

# Batch Reader class
class BatchReader():
    def __init__(self,parent):
        self.parent=parent
        self.xSize = 0;
        self.ySize = 0;
        self.zSize = 0;
        self.tSize = 0;
        self.currentFrame = 0;
        self.fileSlice = 0;
        self.stack = None;
        self.fileData = None;

        self.openFile
