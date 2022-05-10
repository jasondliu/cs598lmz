import _struct
from functools import partial
from six.moves import xrange

from tensorflow.python.framework import dtypes
from tensorflow.python.framework import ops
from tensorflow.python.framework import tensor_shape
from tensorflow.python.ops import array_ops
from tensorflow.python.ops import control_flow_ops
from tensorflow.python.ops import math_ops
from tensorflow.python.ops import random_ops


def _validate_args(shape, minval, maxval, dtype, seed, name):
  """Helper function to validate input arguments."""
  # Check dtype.
  if dtype is None or dtype.base_dtype is dtypes.float32:
    pass
  elif dtype.base_dtype is dtypes.float64:
    minval = math_ops.cast(minval, dtypes.float64)
    maxval = math_ops.cast(maxval, dtypes.float64)
  elif dtype.base_dtype.is_integer:
    minval = math
