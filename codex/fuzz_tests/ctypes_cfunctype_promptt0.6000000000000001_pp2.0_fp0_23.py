import ctypes
# Test ctypes.CFUNCTYPE()

def func(): pass

try:
    ctypes.CFUNCTYPE(func)
except TypeError:
    print("SKIP")
    raise SystemExit

class Bar(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]

FuncType = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(Bar))

def func(arg):
    return arg.x

FuncPtr = FuncType(func)

print(FuncPtr(ctypes.pointer(Bar(42))))
