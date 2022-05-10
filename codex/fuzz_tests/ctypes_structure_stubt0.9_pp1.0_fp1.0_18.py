import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint64()
    y = ctypes.c_uint64()

class L(ctypes.Structure):
    size = ctypes.c_uint16()
    data = ctypes.ARRAY(ctypes.c_uint8, size)

class Bar(ctypes.Structure):
    a = ctypes.c_uint16()
    b = ctypes.ARRAY(ctypes.c_uint8, 10)

class Foo(ctypes.Structure):
    kind = ctypes.c_uint16()
    data = ctypes.Union()
    data.value = S()
    data.array = L()
    data.bar = Bar()

foo = cast(data, POINTER(Foo)).contents
</code>

