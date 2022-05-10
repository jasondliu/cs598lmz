import gc, weakref
import os
import time

from numpy.random import randint

from numpy.testing import assert_array_almost_equal
import numpy as np

import traits
from traits.api import HasTraits, Instance, setup_instance_traits
from traits.util.weak_ref import ref
from traits.util.testing import unittest

from enable.tools.resize_tool import ResizeTool

from chaco.api import ColorBar, DataRange1D, Plot, ArrayPlotData, \
                                 PlotAxis, create_line_plot, \
                                 create_scatter_plot, PlotLabel, \
                                 Legend
from chaco.tools.api import PanTool, ZoomTool, RectZoomTool, MoveTool, \
                                    DragZoom, DataViewPosition


def _gc_and_do_a_samba(pause=0.05):
    # Allow the gc to delete all circular references, then dance
    # to distract it from collecting our variables.
    gc.collect()
    time.sleep(pause)
    gc.collect()
