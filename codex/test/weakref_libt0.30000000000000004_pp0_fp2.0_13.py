import weakref

import numpy as np

from . import _base
from . import _data_obj
from . import _widgets_core
from . import _widgets_styles
from . import _widgets_utils
from . import _widgets_comms


class _BasePlot(object):
    """
    Base class for all plot types.
    """

    def __init__(self, figure, axes, plot_type):
        self._figure = figure
        self._axes = axes
        self._plot_type = plot_type
        self._plot_handles = []
        self._plot_data = []
        self._plot_styles = []
        self._plot_data_objs = []
        self._plot_data_objs_ref = []
        self._plot_data_objs_ref_cnt = []
        self._plot_data_objs_ref_cnt_max = 1
        self._plot_data_objs_ref_cnt_max_default = 1
        self._plot_data_objs_ref_cnt_max_
