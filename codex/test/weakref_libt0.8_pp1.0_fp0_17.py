import weakref

import numpy as np

import matplotlib
from matplotlib import rcParams
from matplotlib.axes import (Axes, SubplotBase, subplot_class_factory,
                             _subplots_adjust, _process_plot_format)
import matplotlib.artist as martist
from matplotlib.artist import Artist
from matplotlib.axes_grid1 import AxesGrid, Grid
from matplotlib.axis import XAxis, YAxis
from matplotlib.cbook import is_string_like, iterable
from matplotlib.collections import RegularPolyCollection
from matplotlib.contour import ContourSet
from matplotlib.image import AxesImage
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle, CirclePolygon
from matplotlib.path import Path
from matplotlib.ticker import Formatter, FixedLocator, NullLocator
from matplotlib.transforms import Affine2D, Bbox, BlendMode, IdentityTransform, Transform, TransformWrapper
