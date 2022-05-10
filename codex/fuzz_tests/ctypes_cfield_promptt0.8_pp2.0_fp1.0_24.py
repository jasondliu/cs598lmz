import ctypes
# Test ctypes.CField.from_address
CField.from_address.argtypes = (object, ctypes.c_size_t)

# Test ctypes.CField.in_dll
class Test:
    _fields_ = [("x", ctypes.c_int)]
c_dll.LoadLibrary.restype = ctypes.POINTER(Test)
c_dll.LoadLibrary.argtypes = (ctypes.c_char_p,)

# Test ctypes.CArgObject.from_address
CArgObject.from_address.argtypes = (object, ctypes.c_size_t)

# Test ctypes.CArgObject.in_dll
class Test:
    _fields_ = [("x", ctypes.c_int)]
c_dll.LoadLibrary.restype = ctypes.POINTER(Test)
c_dll.LoadLibrary.argtypes = (ctypes.c_char_p,)

# Test ctypes.CArray.from_address
CArray.from_address.argtypes = (object, ctypes.c_size_t)

# Test ctypes
