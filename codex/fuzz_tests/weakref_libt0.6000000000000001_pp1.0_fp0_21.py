import weakref

import numpy as np

import matplotlib
import matplotlib.pyplot as plt

from . import opt_einsum
from . import utils


def _get_fig_ax(fig=None, ax=None):
    """
    Get the figure and axes for a plot.

    Parameters
    ----------
    fig : None or matplotlib.figure.Figure
        The figure for the plot. If None, the current figure is used.
    ax : None or matplotlib.axes._subplots.AxesSubplot
        The axes for the plot. If None, a new axes is created.

    Returns
    -------
    fig : matplotlib.figure.Figure
        The figure for the plot.
    ax : matplotlib.axes._subplots.AxesSubplot
        The axes for the plot.
    """
    if fig is None:
        fig = plt.gcf()
    if ax is None:
        ax = fig.add_subplot(111)
    return fig, ax


def plot_tensors(t
