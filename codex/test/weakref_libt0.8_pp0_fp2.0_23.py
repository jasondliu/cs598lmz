import weakref
from functools import partial
import os

# import numpy as np
# from matplotlib.cm import get_cmap
# from matplotlib.colors import BoundaryNorm

import logging

# TODO: How do we handle deleting slices?
# TODO: How do we handle updating slices?
# TODO: How do we handle updating with new data?
# TODO: Add a way to update the colorbar
# TODO: Add a way to update the colorbar, if the data is not in the plottable ranges
# TODO: Add a way of keeping the zoom level, if it is within the plottable range
# TODO: Add a way of updating the data when it is not in the plottable range.
# TODO: Add a way for updating the colorbar.
# TODO: Add callback when the user makes a new selection.
# TODO: Add a way to update the selection.

LOG = logging.getLogger(__name__)


