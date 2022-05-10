import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4.QtGui import QApplication

import sys
import os
import webbrowser

QApplication.setGraphicsSystem("raster")
app = QApplication(sys.argv)

# Make sure that we are using QT4
os.environ['QT_API'] = 'pyqt'

# 2. Import the modules we will use

import numpy as np
from numpy import ma
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# 3. Create a subclass of FigureCanvasQTAgg as our canvas

class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
