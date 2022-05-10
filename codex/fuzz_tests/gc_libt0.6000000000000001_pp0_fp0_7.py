import gc, weakref

import numpy as np

import matplotlib
from matplotlib import verbose
from matplotlib._pylab_helpers import Gcf
from matplotlib.cbook import silent_list, is_string_like, is_writable_file_like, \
     is_numlike, _check_savefig_extra_args
from matplotlib.figure import Figure
from matplotlib.backend_bases import FigureManagerBase, FigureCanvasBase,\
     NavigationToolbar2, cursors

from matplotlib.widgets import SubplotTool
from matplotlib.backend_bases import cursors

from matplotlib.numerix import clip
from matplotlib.numerix import asarray

from matplotlib.backends.backend_mixed import MixedModeRenderer

from matplotlib.backends.backend_agg import FigureCanvasAgg, FigureManagerAgg

from matplotlib.transforms import Bbox

from matplotlib.figure import Figure

from matplotlib.patches import Rectangle, Shadow

from
