import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPalette, QColor
import pyqtgraph as pg

from mpld3 import plugins

import numpy as np

from itertools import groupby

from collections import OrderedDict

from util import *

from config import *

from strata.core import *

from strata.ui import *

from strata.ui.qt.main import *

from strata.ui.qt.plot import *

#from strata.ui.qt.color import *

from strata.ui.qt.scatter import *

from strata.ui.qt.heatmap import *

from strata.ui.qt.dendrogram import *

from strata.ui.qt.histogram import *

from strata.ui.qt.network import *

from strata.ui.qt.palette import *

