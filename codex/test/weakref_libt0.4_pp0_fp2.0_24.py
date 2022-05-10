import weakref

import numpy as np

from . import _base
from . import _data_obj
from . import _utils
from . import _var_obj
from . import encoding
from .common import AbstractDataStore, BackendArray
from .conventions import decode_cf_variable, encode_cf_variable
from .pycompat import basestring, iteritems, OrderedDict, unicode_type
from .utils import Frozen, FrozenOrderedDict, SortedKeysDict, close_on_error


def _infer_fill_value(dtype):
    """Infer a fill value from a dtype."""
    if dtype.kind == 'i':
        fill_value = np.iinfo(dtype).min
    elif dtype.kind == 'f':
        fill_value = np.finfo(dtype).min
    elif dtype.kind == 'u':
        fill_value = np.iinfo(dtype).max
    elif dtype.kind == 'S':
        fill_value = b''
