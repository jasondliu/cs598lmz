import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double)

class Function(object):
    def __init__(self, code, funtype=FUNTYPE, **kwargs):
        self.funtype = funtype
        self.func = funtype(code)
        self.__dict__.update(kwargs)

    def __call__(self, x):
        return self.func(x)

import re
import os
import sys
import ctypes
import unicodedata
import platform
import subprocess
from ctypes import c_double, c_int, c_void_p, c_char_p, c_char, c_bool, c_size_t, py_object
import numpy as np

try:
    unicode
except NameError:
    unicode=str

def _get_ctypes_type(t):
    return {bool: c_bool,
            int: c_int,
            float: c_double,
            complex: c_double,
            str: c_char_p,
            unicode: c_char_p,
            type(None):
