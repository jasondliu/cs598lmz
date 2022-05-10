import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class T(ctypes.Structure):
    pass

ctypes.CStructure = type(T)

# ctype instances
ctypes.CFuncPtr = type(ctypes.cdll[b'puts'])
ctypes.CArray = type(ctypes.c_int * 2)
ctypes.CPointer = type(ctypes.cast(ctypes.c_int(0), ctypes.c_void_p))
ctypes.CString = type(ctypes.cast(ctypes.c_int(0), ctypes.c_char_p))

# callbacks can use a CFuncPtr, or any C callable type
ctypes.CFuncPtrOrCFunction = Callable

# XXX implement ctypes.COpaque
# ctypes.COpaque = ...
