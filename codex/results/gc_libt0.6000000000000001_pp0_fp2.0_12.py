import gc, weakref
import copy
import numpy as np

import matplotlib.cbook as cbook
import matplotlib.transforms as mtransforms
import matplotlib.artist as artist
import matplotlib.colors as mcolors
import matplotlib.backend_bases as backend_bases
import matplotlib.path as mpath
import matplotlib.mlab as mlab
import matplotlib.cbook as cbook
import matplotlib.collections as mcoll
import matplotlib.ticker as ticker
import matplotlib.text as mtext
import matplotlib.lines as mlines

from matplotlib.cbook import is_string_like, is_numlike
from matplotlib.artist import allow_rasterization
from matplotlib.mlab import dist_point_to_segment


def _process_plot_var_args(*args):
    """
    Process variable length argument lists for plot commands.

    The positional and kwarg strings are assumed to have been
    pre-processed to be in the following form:

    - Remaining positional
