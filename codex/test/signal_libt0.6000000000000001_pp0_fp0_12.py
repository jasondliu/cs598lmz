import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import (QCoreApplication, QObject, QRunnable, QThread,
                          QThreadPool, pyqtSignal)

from PyQt5.QtWidgets import (QApplication, QSizePolicy, QWidget, QVBoxLayout,
                             QHBoxLayout, QLineEdit, QPushButton, QLabel,
                             QGridLayout, QComboBox, QSpinBox)

from PyQt5.QtGui import QIntValidator, QDoubleValidator

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation
from matplotlib import style
from matplotlib.ticker import MaxNLocator
from matplotlib.patches import Polygon
import matplotlib.dates as mdates
