import types
types.ClassType

# Standard library imports
import os
import sys
import time

# Major package imports
from numpy import array, float64, linspace, ones, zeros

# Enthought library imports
from enthought.traits.api import Bool, Float, HasTraits, Instance, List, \
    Property, Range, Str
from enthought.traits.ui.api import Group, HGroup, Item, VGroup
from enthought.traits.ui.menu import OKCancelButtons

# Local imports
from enthought.chaco.api import ArrayDataSource, ArrayPlotData, DataRange1D, \
    GridDataSource, GridMapper, LinearMapper, Plot, PlotGrid
from enthought.chaco.tools.api import PanTool, ZoomTool
from enthought.chaco.tools.cursor_tool import CursorTool, BaseCursorTool

#-------------------------------------------------------------------------------
#  Trait definitions:
#-------------------------------------------------------------------------------

# Value to use when a data point is undefined:
