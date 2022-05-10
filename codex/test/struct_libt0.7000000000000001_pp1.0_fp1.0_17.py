import _struct
from collections import defaultdict
from ctypes import create_string_buffer, c_int, c_uint, c_uint8, c_float, c_double, c_void_p, c_char_p, sizeof, c_bool, c_size_t
from ctypes.util import find_library
from math import sqrt, ceil

from . import ml_logger
from .ml_config import ml_config

logger = ml_logger.get_ml_logger()


def _load_libmxnet():
    """Load libmxnet.so by finding it in system library path.
    Returns
    -------
    libmxnet : CDLL
        Loaded libmxnet
    """
    lib_path = find_library('mxnet')
    if lib_path is None:
        lib_path = find_library('libmxnet')
    if lib_path is None:
        lib_path = find_library('libmxnet.so')
