import ctypes
# Test ctypes.CField
#
# This test case works if the following are satisfied:
#   - the offsetof(m) == m[0]
#
# .. note:: We could also use [(x+y).value for x in self.m]
class FIELD(ctypes.Structure):
    _fields_ = [("b", ctypes.c_byte * 1), ("s", ctypes.c_short * 1), ("i", ctypes.c_int * 1), ("l", ctypes.c_long * 1), ("q", ctypes.c_longlong * 1)]


print(ctypes.sizeof(FIELD))
print(tuple(f[0] for f in FIELD._fields_))


class CHILD(ctypes.Structure):
    _fields_ = [("parent", FIELD), ("c", ctypes.c_char * 1)]


print(ctypes.sizeof(CHILD))
print([(x+y).value for x in CHILD._fields_ for y in FIELD._fields_])


# Test ctypes.Structure child
class CHILD2(FIELD
