import ctypes
# Test ctypes.CField.
cfuncs.TestStruct1._fields_ = [
    ('i', ctypes.c_int),
    ('f', cfuncs.TestStruct1),
    ('d', ctypes.c_double)
]

cfuncs.TestStruct1.f = ctypes.CField('f', 'i')

class X(ctypes.Structure):
    pass
cfuncs.TestStruct1.f = ctypes.CField('f', X)

# This is a very different way to initialize a ctypes.Structure
cfuncs.TestStruct1._fields_ = [
    ('f', X),
    ('d', ctypes.c_double)
]

# Test ctypes.CField.
class Y(ctypes.Structure):
    pass
Y._fields_ = [
    ('x', ctypes.c_int),
    ('y', ctypes.c_int),
]

class Z(ctypes.Structure):
    pass
Z._fields_ = [
    ('z1', ctypes.c_int),
    ('z
