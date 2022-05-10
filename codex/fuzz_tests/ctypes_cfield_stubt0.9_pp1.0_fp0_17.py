import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class S1(ctypes.Structure):
    _fields_ = [('x', ctypes.c_char * 3)]

ctypes.CArrayType = type(S1.x)

try:
    del ctypes.CArrayType
except AttributeError:
    pass

class NoLength(ctypes.Structure):
    _fields_ = [(x, ctypes.c_int) for x in "abcdefghijklmnopqrstuvwxyzz"]

class NoLengthSub(NoLength):
    _fields_ = [(x, ctypes.c_int) for x in "abcdefghijklmnopqrstuvwxyzz"]

class C:
    pass

C.x = 1

int_field = S.x
char3_field = S1.x
no_length_field = NoLength.a
no_length_array = NoLength.x
no_length_sub_field = NoLengthSub.a
no_length_sub_array = NoLengthSub.x

class CTypeTestCase(unitt
