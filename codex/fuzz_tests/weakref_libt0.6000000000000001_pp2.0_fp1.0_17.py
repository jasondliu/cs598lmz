import weakref
import functools
import itertools
import copy
import operator

import numpy as np

from . import meta, utils, types, ops, proxy, dtypes, config
from .core import _SymData, _SymDataProxy, _FuncData
from .core import _parse_slice, _parse_index, _parse_indices
from .core import _parse_indices_as_slice
from .core import _is_empty, _is_scalar, _is_empty_or_scalar
from .core import _is_slice, _is_index, _is_indices
from .core import _is_indices_as_slice, _is_scalar_index
from .core import _is_1d_slab, _is_1d_contiguous_slab, _is_1d_slice
from .core import _is_1d_index, _is_1d_indices
from .core import _is_1d_indices_as_slice, _is_1d_scalar_index
from .core import _is
