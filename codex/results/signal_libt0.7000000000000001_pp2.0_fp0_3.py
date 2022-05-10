import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtCore import QTimer

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from matplotlib import gridspec
import numpy as np

from pyqtgraph.parametertree import Parameter, ParameterTree

from animations import Animations
from colors import colors
from utilities import print_exception
from utilities import info_message, warning_message
from utilities import file_load, file_save
from colors import color_options

from detect import Detect
from detect_cfg import DetectCfg
from detect_params import DetectParams
from detect_panel import DetectPanel

from spect
