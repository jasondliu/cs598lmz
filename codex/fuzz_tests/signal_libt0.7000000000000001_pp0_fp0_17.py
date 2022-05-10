import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib import cm
from matplotlib import rcParams
from matplotlib import pyplot
from matplotlib import pylab

from numpy import *
from numpy import linalg

from scipy import *
from scipy import linalg
from scipy.linalg import eig
from scipy.linalg import eigvalsh
from scipy.linalg import svd
from
