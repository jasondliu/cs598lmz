import ctypes
# Test ctypes.CFieldMarker existence to avoid
# "AttributeError: type object 'ctypes.CFieldMarker' has no attribute '__dict__'"
# when running on Python 2.5 without ctypes patches
if hasattr(ctypes, 'CFieldMarker'):
  ctypes.CFieldMarker.__dict__ = {}

from ctypes import (
  CFieldMarker,
  CDLL,
  CFUNCTYPE,
  CHAR,
  POINTER,
  Structure,
  Union,
  c_bool,
  c_char_p,
  c_double,
  c_float,
  c_int,
  c_long,
  c_longdouble,
  c_short,
  c_ubyte,
  c_uint,
  c_ulong,
  c_ushort,
  c_void_p,
  sizeof,
  )
from ctypes.util import find_library

import h2o
from . import H2OResponse
from .backend import H2OLocalServer
from .clustering.kme
