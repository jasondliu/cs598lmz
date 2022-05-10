import weakref

import numpy as np
import pandas as pd

from . import _utils
from . import _indexing
from . import _np_utils
from . import _vindex
from . import ops
from .pycompat import dask_array_type, dask_dataframe_type
from .utils import (
    Frozen,
    SortedKeysDict,
    _maybe_promote,
    _maybe_wrap_array,
    _maybe_unwrap_array,
    _unwrap_index,
    as_variable,
    either_dict_or_kwargs,
    either_dict_or_positional_args,
    ensure_dict,
    ensure_positional_args_dict,
    is_dict_like,
    is_scalar,
    is_valid_numpy_dtype,
    is_valid_var_name,
    is_valid_dtype,
    overlaps,
    pop_to,
    safe_cast_to_index,
    safe_cast_to_index_dtype,
    safe_cast
