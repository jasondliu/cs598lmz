import ctypes
# Test ctypes.CField
class CField(ctypes.Structure):
    _fields_ = [('x','c'), ('y','c')]

class CFloat(ctypes.Structure):
    _fields_ = [('x','f'), ('y','f')]

class CDouble(ctypes.Structure):
    _fields_ = [('x','d'), ('y','d')]

class CInt(ctypes.Structure):
    _fields_ = [('x','i'), ('y','i')]

class CLong(ctypes.Structure):
    _fields_ = [('x','l'), ('y','l')]

class CULong(ctypes.Structure):
    _fields_ = [('x','L'), ('y','L')]

# Test ctypes.CField
CField(1j)
CFloat(1j)
CDouble(1j)
CInt(1j)
CLong(1j)
CULong(1j)
