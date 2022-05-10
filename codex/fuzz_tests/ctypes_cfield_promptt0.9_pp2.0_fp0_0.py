import ctypes
# Test ctypes.CField (formerly PyCField)

# Tests both CField and the format parser
# by taking an empty struct, asking which memory is used to store it,
# then adding a field and checking that more memory is used

class C(ctypes.Structure):
    _fields_ = [
    ]

c = C()
s = ctypes.string_at(ctypes.addressof(c), ctypes.sizeof(c))
m = ctypes.memmove(0, ctypes.addressof(c), ctypes.sizeof(c))

assert s == b'\x00' * ctypes.sizeof(c)
assert m == b'\x00' * ctypes.sizeof(c)

C._fields_ = [('a', ctypes.c_char)]

c = C()
s = ctypes.string_at(ctypes.addressof(c), ctypes.sizeof(c))
m = ctypes.memmove(0, ctypes.addressof(c), ctypes.sizeof(c))

assert s[:1] ==
