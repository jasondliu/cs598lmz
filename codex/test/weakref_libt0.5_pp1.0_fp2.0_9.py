import weakref
import warnings

import numpy as np

from matplotlib import rcParams
from matplotlib.artist import Artist
from matplotlib.cbook import silent_list, is_string_like, is_numlike, \
    iterable, maxdict
from matplotlib.cbook import warn_deprecated
from matplotlib.collections import Collection
from matplotlib.colors import colorConverter
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle
from matplotlib.transforms import Bbox, BboxBase, TransformedBbox, \
    blended_transform_factory, Affine2D
from matplotlib import _api

from matplotlib.offsetbox import AnchoredOffsetbox, AuxTransformBox, VPacker,\
    HPacker, TextArea, DrawingArea
from matplotlib.offsetbox import DraggableOffsetBox
from matplotlib.legend_handler import HandlerBase, HandlerLine2D, \
    HandlerPatch, HandlerCircle, HandlerRegularPolyCollection, \
    HandlerLineCollection, HandlerPathCollection, Handler
