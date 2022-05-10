import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

ctypes.FFI = __getattr__(ctypes.c_int, '__ctype_ffi__')

_cffi_backend_cdata = __getattr__(ctypes.c_int, '__cffi_backend_cdata')
CDataOWN = __getattr__(_cffi_backend_cdata, 'CDataOWN')

ctypes.c_int._ffi = ctypes.FFI()
ctypes.c_int._ffi.cast_int = __getattr__(ctypes.c_int._ffi, '_cast_primitive')
ctypes.c_int._ffi.from_handle = __getattr__(ctypes.c_int._ffi, '_from_handle')

from _cffi_backend import new_primitive_type, new_pointer_type, new_array_type
from _c
