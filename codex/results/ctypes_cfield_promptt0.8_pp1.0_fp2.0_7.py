import ctypes
# Test ctypes.CFields

class IntFixedArrayType(ctypes.c_long):
    _type_ = "i"
    _subtype_ = ctypes.c_int32
    _length_ = 10
    _subarray_ = True

class X(ctypes.Structure):
    _fields_ = [("a", IntFixedArrayType),
                ("b", IntFixedArrayType, 1),
                ("c", IntFixedArrayType, 2)]



# This is a copy&paste from test_misc.py.  It is tested by
# tesst_CFields.
class X2(ctypes.Structure):
    _fields_ = [("data", ctypes.c_char * 17, 0),
                ("first", ctypes.c_int, 0),
                ("second", ctypes.c_int, 32),
                ("third", ctypes.c_char * 17, 64),
                ("fourth", ctypes.c_longlong, 80),
                ("fifth", ctypes.c_char * 17, 80),
                ("sixth", ctypes.c_int,
