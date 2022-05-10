import ctypes
# Test ctypes.CField.from_address()

import_struct = ctypes.cdll.LoadLibrary(
    ctypes.util.find_library("c")).import_struct

class S(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]

class S2(ctypes.Structure):
    _fields_ = [("s", S), ("c", ctypes.c_char)]

# This is the offset of 'c' in S2
offset = ctypes.sizeof(S)

s = S2()
s.s.a = 0x1234
s.s.b = 0x5678
s.c = 0x41

a = ctypes.addressof(s)
a = ctypes.addressof(s)
p = ctypes.c_void_p.from_address(a)

# Test that this works with a void pointer
assert p.value == a

f = ctypes.CField.from_address(a + offset, ctypes.c_char
