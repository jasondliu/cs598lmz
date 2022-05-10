import weakref
from collections import OrderedDict, defaultdict
from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import SubplotParams
from matplotlib.widgets import Cursor
import qtawesome as qta
from qtpy.QtCore import Qt, QSize, QTimer, QEvent, QItemSelectionModel, QItemSelection
from qtpy.QtGui import QStandardItemModel, QStandardItem, QColor, QFont
