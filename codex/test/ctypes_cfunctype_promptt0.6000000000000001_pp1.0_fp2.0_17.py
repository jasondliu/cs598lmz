import ctypes
# Test ctypes.CFUNCTYPE

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

Xp = ctypes.POINTER(X)

@ctypes.CFUNCTYPE(None, ctypes.c_int)
def func(n):
    print(n)

@ctypes.CFUNCTYPE(None, Xp)
def func2(p):
    print(p.contents.a)

@ctypes.CFUNCTYPE(None, ctypes.POINTER(X))
def func3(p):
    print(p.contents.a)

@ctypes.CFUNCTYPE(None, ctypes.POINTER(X), ctypes.c_int)
def func4(p, n):
    print(p.contents.a, n)

@ctypes.CFUNCTYPE(None, ctypes.c_int, Xp)
def func5(n, p):
    print(n, p.contents.a)

