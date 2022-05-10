import weakref
import logging
import warnings
import numpy as np

from ._backend_utils import (_BackendUtilBase, _BackendUtilMixin,
                             BACKEND_NAME, LOCAL_FONT_DIR,
                             get_icon_fname, get_image_fname)
from .backends.backend_qt5agg import (
    FigureCanvasQTAggBase, FigureCanvasQTAgg,
    NavigationToolbar2QT as NavigationToolbar, TimerQT,
    _create_qApp)
from .backend_qt5 import (
    FigureManagerQT, FigureCanvasQT, show, draw_if_interactive,
    backend_version)

from PyQt5 import QtCore, QtGui, QtWidgets

from matplotlib.backend_bases import _Backend, FigureCanvasBase, FigureManagerBase, FigureManagerHelper
from matplotlib.backends._backend_agg import FigureCanvasAgg

from matplotlib import rcParams

from matplotlib.cbook import is_string_like
