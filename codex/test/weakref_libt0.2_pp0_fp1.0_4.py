import weakref

from . import _core
from . import _util
from . import _errors
from . import _types
from . import _compat
from . import _constants
from . import _lib

_lib.lz4f_createCompressionContext.argtypes = [
    ctypes.POINTER(ctypes.c_void_p),
    ctypes.c_uint32
]
_lib.lz4f_createCompressionContext.restype = ctypes.c_int

_lib.lz4f_freeCompressionContext.argtypes = [
    ctypes.c_void_p
]
_lib.lz4f_freeCompressionContext.restype = None

_lib.lz4f_compressFrame.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_size_t,
    ctypes.c_void_p,
    ctypes.c_size_t
]
_lib.lz4f_compressFrame.restype = c
