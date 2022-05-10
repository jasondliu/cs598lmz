import ctypes
# Test ctypes.CFUNCTYPE

class Struct(ctypes.Structure):
    _fields_ = [("left", ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)),
                ("right", ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int))]

@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def add(a, b):
    return a + b

@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def sub(a, b):
    return a - b

obj = Struct()
obj.left = add
obj.right = sub

print obj.left(2, 3)
print obj.right(2, 3)
