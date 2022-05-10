import types
types.ModuleType.__repr__ = lambda self: self.__name__

import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.patches as patches
import matplotlib.colors as colors
import matplotlib.cm as cmx
import matplotlib.colorbar as colorbar
import matplotlib.gridspec as gridspec

from . import plot_utils
from . import plot_config

def plot_summary(
        data_dict,
        fig_name,
        fig_title,
        fig_size,
        x_label,
        y_label,
        x_lim,
        y_lim,
        x_tick_spacing,
        y_tick_spacing,
        x_tick_decimals,
        y_tick_decimals,
        x_tick_pad,
        y_tick_pad,
        x_tick_rotation,
        y_tick_rotation,
        x_tick_minor
