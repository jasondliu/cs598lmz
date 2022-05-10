import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

import matplotlib as mpl
mpl.use("Agg")
mpl.rc('font', **{'family': 'serif'})
mpl.rc('text', usetex=True)
mpl.rc('xtick', labelsize=15)
mpl.rc('ytick', labelsize=15)
mpl.rc('legend', fontsize=12)

import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

import numpy as np
np.seterr(divide='raise', invalid='raise')

import graph_tool as gt
import graph_tool.centrality
from graph_tool import load_graph

from mpl_toolkits.axes_grid.parasite_axes import \
    SubplotHost, ParasiteAxesAuxTrans
from mpl_toolkits.axes_grid1 import make_axes_locatable

