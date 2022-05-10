import ctypes
# Test ctypes.CField
class test(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_float),
                ("z", ctypes.c_ubyte)]

class test2(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_float),
                ("z", ctypes.c_ubyte)]

class test3(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", test),
                ("z", ctypes.c_ubyte)]

t = test()
print t._fields_[0] is test._fields_[0]
print t._fields_[1] is test._fields_[1]
print t._fields_[2] is test._fields_[2]

print test._fields_[0] is test2._fields_[0]
print test._fields_[1] is test2._fields_[1]
print test._
