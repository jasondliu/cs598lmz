import gc, weakref

from . import _lazy_import

_lazy_import.lazy_module("numpy")

_lazy_import.lazy_module("tensorflow")

# pylint: disable=g-direct-tensorflow-import
from tensorflow.python import pywrap_tensorflow
from tensorflow.python.framework import ops
# pylint: enable=g-direct-tensorflow-import

from tensorflow.python.framework import dtypes as _dtypes
from tensorflow.python.framework import ops as _ops
from tensorflow.python.framework import tensor_shape as _tensor_shape
from tensorflow.python.ops import array_ops as _array_ops
from tensorflow.python.ops import math_ops as _math_ops
from tensorflow.python.ops import resource_variable_ops as _resource_variable_ops
from tensorflow.python.ops import state_ops as _state_ops
from tensorflow.python.ops import variables as _variables
from tensorflow.python.ops import
