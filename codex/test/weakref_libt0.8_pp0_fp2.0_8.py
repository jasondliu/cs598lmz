import weakref
import functools
from collections import defaultdict
from typing import Any, Iterable, Iterator, List, Optional, Set, Type, TypeVar, Union
from typing_extensions import Literal

import matplotlib.pyplot as plt
from sgmllib import SGMLParser
from scipy.ndimage import gaussian_filter
from matplotlib.animation import FuncAnimation
from matplotlib.axes import Axes
from matplotlib.axes._subplots import SubplotBase
from matplotlib.colorbar import Colorbar
from matplotlib.figure import Figure, SubplotParams
from matplotlib.gridspec import GridSpec
from matplotlib.ticker import MaxNLocator

from .json import dthandler, JSON_TYPES, object_hook
