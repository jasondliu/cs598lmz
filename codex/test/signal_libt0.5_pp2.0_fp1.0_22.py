import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Import the Qt libraries and use the Qt5Agg backend
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np

# Create the main window class
class App(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.left = 10
        self.top = 10
        self.title = 'Matplotlib and PyQt5 integration'
        self.width = 640
        self.height = 400
        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowTitle(self.title)
