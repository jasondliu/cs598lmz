import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

if hasattr(ctypes.CField([(1,2)], 3), "name"):
    print("SKIP")
    import sys
    sys.exit()

print(ctypes.CField([(1,2)], 3).offset)
