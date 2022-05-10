import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CDataMeta(type(ctypes.c_int)):
    def __getattr__(self, attr):
        return getattr(ctypes.c_int, attr)

class CDataOwnedMeta(type(ctypes.pointer(S()))):
    def __getattr__(self, attr):
        return getattr(ctypes.pointer(S()), attr)

class CDataSubtype(ctypes.c_int):
    __metaclass__ = CDataMeta

from_param = CDataSubtype.from_param
from_address = CDataSubtype.from_address
from_buffer = CDataSubtype.from_buffer
from_buffer_copy = CDataSubtype.from_buffer_copy

_subclass_cache = {}
def memset(s, c, size):
    """memset() implementation."""
    if not isinstance(s, type(ctypes.pointer(S()))):
        s = s._subtype_from_mem_addr(s._mem_addr)
    ctypes.mem
