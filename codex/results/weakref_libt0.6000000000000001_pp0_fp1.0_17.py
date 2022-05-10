import weakref

try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None

from .abstract_plotter import AbstractPlotter
from .plot_interface import PlotInterface
from .plot_canvas import PlotCanvas
from .plot_item import PlotItem
from .plot_item_proxy import PlotItemProxy
from .plot_canvas_proxy import PlotCanvasProxy
from .plot_window import PlotWindow
from .plot_window_proxy import PlotWindowProxy

from .plot_item import PlotItem
from .plot_canvas import PlotCanvas
from .plot_window import PlotWindow

from .plot_data_item import PlotDataItem
from .plot_curve_item import PlotCurveItem
from .plot_bar_graph_item import PlotBarGraphItem
from .plot_image_item import PlotImageItem
from .plot_histogram_item import PlotHistogramItem
from .plot_label_item import PlotLabelItem

from .plot_data_item import PlotDataItemProxy
from .plot_curve_item import PlotCurveItemProxy
