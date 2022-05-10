import ctypes
# Test ctypes.CField

fields = [
    ('c', ctypes.c_char),
    ('i', ctypes.c_int),
]

class Test(ctypes.Structure):
    _fields_ = fields

class Test2(ctypes.Structure):
    _fields_ = fields

class Test3(Test):
    _fields_ = fields

# Test ctypes.CArgObject

class Test4(ctypes.Structure):
    _fields_ = [('c', ctypes.c_char),
                ('i', ctypes.POINTER(ctypes.c_int)),
                ('d', ctypes.c_double)]

class Test5(ctypes.Structure):
    _fields_ = [('c', ctypes.c_char),
                ('i', ctypes.POINTER(ctypes.c_int)),
                ('d', ctypes.c_double)]

print(Test._fields_)
print(Test2._fields_)
print(Test3._fields_)
print(Test4._fields_)
print(Test5._fields_)
