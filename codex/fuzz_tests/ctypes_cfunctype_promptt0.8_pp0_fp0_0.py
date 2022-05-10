import ctypes
# Test ctypes.CFUNCTYPE(c_int)(lambda: 42)()
module = types.ModuleType('foo')
module.c_int = ctypes.c_int
module.CFUNCTYPE = ctypes.CFUNCTYPE
module.CFUNCTYPE(module.c_int)(lambda: 42)()

# Issue #4041: test __cinit__
class X(ctypes.c_int):
    def __cinit__(self, *args, **kwargs):
        pass
X()

# Issue #4030: test ctypes.create_struct_proxy()
import struct
struct.pack("h", ctypes.c_short(123).value)
struct.pack("i", ctypes.c_int(-123).value)
struct.pack("q", ctypes.c_longlong(123456789).value)

# Issue #4093: test _ctypes.Array
class X(ctypes.Array):
    _length_ = 5
    _type_ = ctypes.c_ubyte
ctypes.memset(ctypes.addressof(X
