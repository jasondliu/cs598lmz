import weakref
import warnings

from . import utils
from . import events

from .utils import deprecated

__all__ = ['FigureCanvasBase', 'FigureCanvasGTK', 'FigureCanvasGTKAgg',
           'FigureCanvasGTKCairo', 'FigureCanvasGTK3Agg',
           'FigureCanvasGTK3Cairo', 'FigureCanvasAgg', 'FigureCanvasCairo',
           'FigureCanvasPS', 'FigureCanvasPDF', 'FigureCanvasSVG',
           'FigureManagerBase', 'FigureManagerGTK', 'FigureManagerGTK3',
           'FigureManagerTkAgg', 'FigureManagerWx', 'FigureManagerWxAgg',
           'show', 'draw_if_interactive', 'new_figure_manager',
           'backend_version', 'backend_version_re', '_Backend',
           '_BackendMacOSX', '_BackendQt4', '_BackendQt5',
           '_BackendTk', '_BackendWx']

_log = logging.getLogger(__name__)

