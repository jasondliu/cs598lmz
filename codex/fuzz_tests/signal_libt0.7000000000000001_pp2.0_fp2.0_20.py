import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Qt5 backend
import sys
from PyQt5 import QtWidgets

# Matplotlib figure object
from matplotlib.figure import Figure

# Matplotlib canvas object, that draws on the figure
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas)

# Navigation toolbar
from matplotlib.backends.backend_qt5agg import (
    NavigationToolbar2QT as NavigationToolbar)

# Matplotlib axes object, that plots on the canvas
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas)

# Navigation toolbar
from matplotlib.backends.backend_qt5agg import (
    NavigationToolbar2QT as NavigationToolbar)

# Matplotlib axes object, that plots on the canvas
from matplotlib import pyplot as plt

# PyQt5 Designer generated code
from pyqt_design
