import types
types.ModuleType.__repr__ = lambda self: self.__name__

import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.patches as patches
import matplotlib.colors as colors
import matplotlib.cm as cmx
import matplotlib.colorbar as colorbar
import matplotlib.gridspec as gridspec

from . import plot_utils
from . import plot_config

