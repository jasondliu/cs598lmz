import weakref

import numpy as np

import matplotlib
from matplotlib import _pylab_helpers, cbook
from matplotlib.backend_bases import (
    _Backend, FigureCanvasBase, FigureManagerBase, NavigationToolbar2,
    TimerBase, cursors)
from matplotlib.backends import _macosx
from matplotlib.backends.backend_mixed import MixedModeRenderer
from matplotlib.backends.backend_macosx import (_BackendMac,
                                                FigureCanvasMac,
                                                FigureManagerMac,
                                                NavigationToolbar2Mac,
                                                TimerMac, cursors as _mac_cursors,
                                                RendererMac)
from matplotlib.backends.backend_webagg_core import (
    FigureCanvasWebAggCore, FigureManagerWebAgg, NavigationToolbar2WebAgg,
    TimerWebAgg, cursors as _webagg_cursors,
    RendererWebAgg, _BackendWebAggCore)
