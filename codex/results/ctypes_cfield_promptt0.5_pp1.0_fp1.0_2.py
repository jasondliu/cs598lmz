import ctypes
# Test ctypes.CField

class Test(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char),
                ("b", ctypes.c_int)]

class Test2(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char),
                ("b", ctypes.CField)]

class Test3(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char),
                ("b", ctypes.CField(ctypes.c_int))]

for cls in Test, Test2, Test3:
    print cls
    obj = cls()
    print obj.a, obj.b, repr(obj.b)
    obj.b = 1
    print obj.a, obj.b, repr(obj.b)
    print

# Test ctypes.CField.from_param

class Test4(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char),
                ("b", ctypes.CField(ctypes.c_
