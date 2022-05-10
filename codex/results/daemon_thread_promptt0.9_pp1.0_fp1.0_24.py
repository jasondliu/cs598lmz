import threading
# Test threading daemon
from random import random

import definitions as defs
import datetime

from matplotlib.backends import qt_compat
use_pyside = qt_compat.QT_API == qt_compat.QT_API_PYSIDE

if use_pyside:
    from PySide import QtGui, QtCore
    from matplotlib.figure import Figure
    from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
else:
    from PyQt4 import QtGui, QtCore
    from matplotlib.figure import Figure
    from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
    from matplotlib.backend_bases import key_press_handler
    
class ApplicationWindow(QtGui.QMainWindow):
    
    """
    The application class
    """

    def __init__(self):
        """
        Initialization
        """
        logger.debug("Initializing UI.")
        %gui q
