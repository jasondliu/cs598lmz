import ctypes

class S(ctypes.Structure):
    x = ctypes.c_short_mutex()
    _fields_ = [("a", ctypes.c_ubyte), ("x", ctypes.c_ushort_mutex)]

class S2(ctypes.Structure):
    x = ctypes.c_short_atomic()
    y = ctypes.c_int_atomic()
    _fields_ = [("a", ctypes.c_ubyte), ("x", ctypes.c_ushort_atomic), ("y", ctypes.c_uint_atomic)]

class S3(ctypes.Structure):
    _fields_ = [("y", ctypes.c_int_atomic)]
    x = ctypes.c_short_atomic()
    z = ctypes.c_uint_atomic()

with pytest.raises(TypeError):
    S.__dict__['a'].__set__(S(), 42)

try:
    S.__dict__['x'].__set__(S(), 42)
except TypeError:
    pass
else:
    assert 0

with py
