import ctypes
# Test ctypes.CField
class CFoo(ctypes.Structure):
    pass
CFoo._fields_ = [("_0", ctypes.c_int),
                 ("_1", ctypes.c_int)]
# Test nested ctypes.CField
class CFoo2(ctypes.Structure):
    pass
class CFoo3(ctypes.Structure):
    _fields_ = [("_0", ctypes.POINTER(CFoo2))]
CFoo2._fields_ = [("_0", ctypes.c_int),
                  ("_1", ctypes.POINTER(CFoo3)),
                  ("_2", ctypes.c_int)]


# Test ctypes.CFuncPtr
CFuncPtr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)


# Test ctypes.Py_UNICODE_SIZE
Py_UNICODE_SIZE = ctypes.sizeof(ctypes.c_wchar)

# Test ctypes.py_object
py_object = ctypes.py_object

# Test ctypes.
