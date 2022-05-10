import ctypes
# Test ctypes.CField variables should not be stored in subclasses.

class X:
    def __new__(self):
        return (ctypes.c_int * 1).__new__(Y)

class Y(X):
    x = ctypes.c_int

y = Y()
print(y._fields_ == [])
