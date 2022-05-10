import weakref

import numpy as np

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.collections import LineCollection
from matplotlib.colors import colorConverter
from matplotlib.cbook import iterable, is_string_like
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle
from matplotlib.transforms import Bbox

from matplotlib.artist import Artist
from matplotlib.mlab import dist_point_to_segment
from matplotlib.path import Path
from matplotlib.text import Text
from matplotlib.widgets import SubplotTool
from matplotlib.image import AxesImage
from matplotlib.collections import RegularPolyCollection
from matplotlib.collections import CircleCollection
from matplotlib.collections import PolyCollection
from matplotlib.collections import LineCollection
from matplotlib.collections import PathCollection
from matplotlib.collections import QuadMesh
from matplotlib.collections import Polygon
from matplotlib
