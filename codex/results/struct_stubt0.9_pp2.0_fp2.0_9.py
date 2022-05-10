from _struct import Struct
s = Struct.__new__(Struct)
print(s)
# <_struct.Struct object at 0x7f2fbb6a0250>
print(s.size)
# 32
print(s.format)
# 'P'

import ctypes, _ctypes
s = ctypes.CFuncPtr.__new__(ctypes.CFuncPtr)
print(s)
# <CFuncPtr object at 0x7fe5a2c49710>
print(s.argtypes)
# (<class 'ctypes._Pointer_Type_'>,)


class Point:
    pass
pt = Point.__new__(Point)
print(pt)
pt.x = 10
print(pt.x)
