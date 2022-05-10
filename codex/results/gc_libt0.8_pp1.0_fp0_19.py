import gc, weakref
from . import ffi, lib
from .util import *
from .gc import MemMgr, MemStats
from .objects import *
from .enums import *


LAYER_VERSION = ( ffi.cast("uint32_t", lib.LAYER_VERSION_MAJOR) << 24
                | ffi.cast("uint32_t", lib.LAYER_VERSION_MINOR) << 16
                | ffi.cast("uint32_t", lib.LAYER_VERSION_PATCH) )

# VERY IMPORTANT: Do not perform any expensive operations in __init__,
# because the backend module's CFFI lib object is not yet initialized.
# All such expensive operations must be performed in _init,
# which is called AFTER the library has been initialized.

# class LAYER_cffi_lib(object):
# 
#     def __init__(self):
#         super(LAYER_cffi_lib, self).__init__()
# 
#     def _init(self, ffi):
#         self._ffi
