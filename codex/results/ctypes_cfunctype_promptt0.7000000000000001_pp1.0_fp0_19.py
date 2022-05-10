import ctypes
# Test ctypes.CFUNCTYPE.
def func(a, b):
    return a + b

CFunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
cfunc = CFunc(func)
cfunc(1, 2)


# Test ctypes.CFUNCTYPE.
def func(a, b):
    return a + b

CFunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
cfunc = CFunc(func)
cfunc(1, 2)


# Test ctypes.WinDLL.
dll = ctypes.WinDLL("kernel32.dll")
dll.GetCurrentProcessId()


# Test ctypes.PyDLL.
dll = ctypes.PyDLL("_ctypes")
dll.PyCArrayType.restype = ctypes.c_void_p

# Can't call it with an argument, because it will try to use
# PyUnicode_FromEncodedObject() which we
