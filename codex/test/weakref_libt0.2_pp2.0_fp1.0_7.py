import weakref

import numpy as np

from . import _base
from . import _data_obj
from . import _utils
from . import _var
from . import groupby
from . import indexing
from . import ops
from . import variable
from .common import AbstractDataStore, BackendArray, DataStorePickleMixin
from .pycompat import iteritems, OrderedDict, basestring, dask_array_type
from .utils import Frozen, SortedKeysDict, _get_fill_value, _maybe_promote, _validate_axis

# TODO: remove when we drop support for numpy < 1.7
try:
    from numpy.lib.stride_tricks import as_strided
except ImportError:
    from .utils import as_strided


