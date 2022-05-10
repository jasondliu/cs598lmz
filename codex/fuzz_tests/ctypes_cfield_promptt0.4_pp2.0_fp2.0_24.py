import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

    class b(ctypes.CField):
        def __init__(self):
            ctypes.CField.__init__(self, ctypes.c_int)
        def __get__(self, obj, cls):
            return obj.b + 1
        def __set__(self, obj, value):
            obj.b = value - 1

x = X()
x.a = 1
x.b = 2

print x.a, x.b
x.b = 3
print x.a, x.b

# Test ctypes.CField with union

class X(ctypes.Union):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

    class b(ctypes.CField):
        def __init__(self):
            ctypes.CField.__init__(self, ctypes.c
