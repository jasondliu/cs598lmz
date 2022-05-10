import weakref
import warnings
from collections import defaultdict
from copy import deepcopy
from functools import partial
from itertools import product
from math import ceil, floor
from operator import itemgetter
from typing import Any, Callable, Dict, Iterable, List, Optional, Sequence, Tuple, Union

import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components

from . import _utils, utils
from .core import DataFrame, Series
from .core.arrays import CategoricalArray, SparseArray
from .core.common import (
    _get_block_manager_and_items,
    _maybe_box_datetimelike,
    _maybe_box_datetimelikes_in_column,
    _maybe_box_datetimelikes_in_index,
    _maybe_box_datetimelikes_in_series,
    _maybe_box_datetimelikes_in_values,
    _maybe_
