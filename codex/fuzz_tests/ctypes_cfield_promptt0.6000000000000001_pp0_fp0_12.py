import ctypes
# Test ctypes.CField class

class X(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_int),
        ("b", ctypes.c_int),
        ("c", ctypes.c_int),
        ("d", ctypes.c_int),
        ("e", ctypes.c_int),
        ("f", ctypes.c_int),
    ]

    def __getattr__(self, name):
        print("__getattr__(self, %r)" % (name,))
        raise AttributeError

x = X()
print(x.a)
print(x.b)
print(x.c)
print(x.d)
print(x.e)
print(x.f)

# Shouldn't call __getattr__
print(x.a)
print(x.b)
print(x.c)
print(x.d)
print(x.e)
print(x.f)
