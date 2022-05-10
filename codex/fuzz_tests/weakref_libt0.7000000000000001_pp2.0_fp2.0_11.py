import weakref
import sys
import os

import numpy

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui


import Orange
from Orange.data import Table, Domain
from Orange.preprocess.preprocess import Preprocess
from Orange.widgets import widget, settings, gui
import Orange.widgets.utils.itemmodels
import Orange.widgets.utils.colorpalette as colorpalette
from Orange.widgets.utils import colorpalette as cp
from Orange.widgets.utils.colorpalette import ColorPaletteDlg, \
    ContinuousPalettePixmap, DiscretePalettePixmap
from Orange.widgets.utils.widgetpreview import WidgetPreview

from .. import impute

from .. import preprocess


class OWImpute(widget.OWWidget):
    name = "Impute"
    description = ""
    icon = "icons/Impute.svg"
    category = "Data"
