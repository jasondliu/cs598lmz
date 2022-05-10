import weakref

from matplotlib import rcParams

from matplotlib import docstring, rcsetup
from matplotlib.backend_bases import (
    _Backend, FigureCanvasBase, FigureManagerBase, GraphicsContextBase,
    RendererBase, TimerBase, cursors)
from matplotlib.backend_managers import ToolManager, Toolbar
from matplotlib.figure import Figure
from matplotlib.path import Path
from matplotlib.transforms import Bbox, TransformedBbox, IdentityTransform, \
    TransformedPath

from matplotlib.backends._backend_agg import RendererAgg

from matplotlib.widgets import SubplotTool

from matplotlib.backend_bases import key_press_handler

from matplotlib.backends.backend_mixed import MixedModeRenderer

from matplotlib.backends.backend_gtk3 import _BackendGTK3, FigureCanvasGTK3, \
    FigureManagerGTK3, GraphicsContextGTK3, RendererGTK3

from matplotlib
