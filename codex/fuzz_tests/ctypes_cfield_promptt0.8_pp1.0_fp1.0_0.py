import ctypes
# Test ctypes.CField
#   ctypes type, name, offset and size
#   ctypes.sizeof(type) == size
#   ctypes.addressof(type) == offset


class Foo(ctypes.Structure):
    _fields_ = [
        (
            '_bar',
            ctypes.c_int,
            1
        ),
        (
            '_baz',
            ctypes.c_int,
            2
        )
    ]


class Bar(ctypes.Structure):
    _fields_ = [
        (
            '_foo',
            ctypes.POINTER(Foo)
        ),
        (
            '_cee',
            ctypes.c_int,
            1
        )
    ]


foosize = ctypes.sizeof(Foo)
barsize = ctypes.sizeof(Bar)
f = Foo()
b = Bar()
if not b._foo:
    print('Failed to init _foo')
if not isinstance(b._cee, ctypes.c_int):
    print("F
