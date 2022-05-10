import ctypes
ctypes.cast(None, ctypes.py_object)

# The following import is needed to make the
# "from . import _distributor_init" work in
# tensorflow/python/ops/distributions/__init__.py
import tensorflow.python._pywrap_tensorflow_internal # pylint: disable=unused-import

# pylint: disable=g-bad-import-order
from tensorflow.python import pywrap_tensorflow
from tensorflow.python.tools import component_api_helper
# pylint: enable=g-bad-import-order

_allowed_symbols = [
    'pywrap_tensorflow',
    'component_api_helper',
]
