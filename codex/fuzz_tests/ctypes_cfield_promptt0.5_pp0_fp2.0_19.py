import ctypes
# Test ctypes.CField

class CFoo(ctypes.Structure):
    _fields_ = [("bar", ctypes.CField(ctypes.c_int))]

class CFoo2(ctypes.Structure):
    _fields_ = [("_bar", ctypes.c_int)]
    bar = ctypes.CField(_bar)

class CFoo3(ctypes.Structure):
    _fields_ = [("_bar", ctypes.c_int)]
    bar = ctypes.CField(_bar, ctypes.c_int, 0x123)

class CFoo4(ctypes.Structure):
    _fields_ = [("_bar", ctypes.c_int)]
    bar = ctypes.CField(_bar, ctypes.c_int, 0x123, "bar")

class CFoo5(ctypes.Structure):
    _fields_ = [("_bar", ctypes.c_int)]
    bar = ctypes.CField(_bar, ctypes.c_int, 0x123, "bar", "doc")

class CFoo6
