import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Int(ctypes.c_int):
    _type_ = "I"

class UInt(ctypes.c_uint):
    _type_ = "I"

class Long(ctypes.c_long):
    _type_ = "l"

class ULong(ctypes.c_ulong):
    _type_ = "l"

class LongLong(ctypes.c_longlong):
    _type_ = "q"

class ULongLong(ctypes.c_ulonglong):
    _type_ = "q"

class Float(ctypes.c_float):
    _type_ = "f"

class Double(ctypes.c_double):
    _type_ = "d"

class Char(ctypes.c_char):
    _type_ = "c"

class UChar(ctypes.c_ubyte):
    _type_ = "B"

class Short(ctypes.c_short):
    _type_ = "h"

class UShort(ctypes.c_
