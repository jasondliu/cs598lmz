import ctypes
# Test ctypes.CField()
# 2080560 should be CField
if ctypes.CField != 2080560:
    raise Exception("This is not CField")

class POINT(ctypes.Structure):
    if ctypes.sizeof(ctypes.c_long) == ctypes.sizeof(ctypes.c_void_p):
        _fields_ = [
            ('x', ctypes.c_long),
            ('y', ctypes.c_long)
            ]
    else:
        _fields_ = [
            ('x', ctypes.c_int),
            ('y', ctypes.c_int)
            ]

if ctypes.sizeof(POINT) != 8:
    raise Exception("sizeof(POINT) == %s, should be 8" % ctypes.sizeof(POINT))

class POINTARRAY(ctypes.Array):
    _length_ = 4
    _type_ = POINT

if ctypes.sizeof(POINTARRAY) != 8 * 4:
    raise Exception("sizeof(POINTARRAY) == %s
