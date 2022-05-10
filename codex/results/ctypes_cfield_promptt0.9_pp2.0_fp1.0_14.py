import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int)]
    ctypes.cfield('b', ctypes.c_int, 0)

print C.b.__doc__                                            # doctest: +ELLIPSIS
# <type 'int'>
print C.b.offset                                             # doctest: +ELLIPSIS
# 4
print C.b.size                                               # doctest: +ELLIPSIS
# 4
print C().a                                                  # doctest: +ELLIPSIS
# 0
print C().b                                                  # doctest: +ELLIPSIS
# 0
C().b = 3
print C().b                                                  # doctest: +ELLIPSIS
# 3
C().a = 4
print C().b                                                  # doctest: +ELLIPSIS
# 4
# Test the base type of a CField
# This currently does not work because the CField does not by
# itself express the type.
class Bitfield(ctypes.Structure):
    _fields_ = [('flag1
