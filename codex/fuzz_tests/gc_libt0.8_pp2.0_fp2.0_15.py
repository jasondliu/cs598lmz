import gc, weakref
import config
from utils.dialog import message
from utils.text import fill, dedent

import scipy.interpolate

import matplotlib.cm as cm
import matplotlib.colors as colors
import matplotlib.transforms as transforms

from tools.plot.figure import Figure, update_figures
from tools.plot.window import PlotWindow
from tools.plot.common import _

from tools.plot.types import (
    BasicPlotType, DataPlotType, PlotType, CombiningPlotType
)
from tools.plot.colors import cycle_cmap
from tools.plot.formatter import formatter
from tools.plot.style import create_style

from tools.plot.dataset import DataSet, DataSetException
from tools.plot.dataset.datasets import (
    PointDataSet, GridDataSet, ConstantDataSet, FunctionDataSet
)
from tools.plot.dataset.combine import DatasetCombiner, SimpleCombiner
from tools.plot.dataset.transform import TransformDataSet

import tools.plot
