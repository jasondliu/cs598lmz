import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
os.environ["QT_API"] = "pyqt5"

import qtpy

import pyqtgraph as pg
from pyqtgraph import QtCore, QtGui
import pyqtgraph.console

from . import __version__

from . import util
from . import config
from . import datafile
from . import datadisplay
from . import datatree
from . import datatypes
from . import dataedit
from . import dataexport
from . import datalink
from . import datawatch
from . import utilqt
from . import plugins
from . import qtutil
from . import flowchart
from . import flowchart.library
from . import flowchart.functions
from . import console
from . import fileio
from . import debug
from . import template
from . import settings
from . import icons
from . import templates
from . import treefilter
from . import report
from . import qtplot
from . import qtdesigner
from
