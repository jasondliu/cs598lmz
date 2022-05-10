import ctypes
# Test ctypes.CField
class CTest(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]
ctypes.CField("b", ctypes.c_char)

# Test ctypes.PyCFuncPtr
ctypes.PyCFuncPtr(lambda x: x)

# Test ctypes.ArgumentError
ctypes.ArgumentError("error message")
