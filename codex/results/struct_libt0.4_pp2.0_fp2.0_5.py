import _struct

import numpy as np

from . import _cffi_utils
from . import _types
from . import _utils
from . import _utils_np
from . import _utils_py
from . import _utils_str
from . import _utils_validate
from . import _utils_var


def _get_dtype_and_shape(
        dtype,
        shape,
        dtype_is_set=False,
        shape_is_set=False):
    """
    Get a dtype and shape.

    Args:
        dtype: A dtype.
        shape: A shape.
        dtype_is_set: Whether the dtype is set.
        shape_is_set: Whether the shape is set.

    Returns:
        A tuple of dtype and shape.

    Raises:
        TypeError: If the dtype is not a dtype.
        TypeError: If the shape is not a shape.
        ValueError: If the dtype is not compatible with the shape.

    """
    # dtype
    if dtype_is
