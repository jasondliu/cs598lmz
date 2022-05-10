import ctypes
# Test ctypes.CFUNCTYPE
def prototype(arg):
    return arg

ctypes.CFUNCTYPE(None, ctypes.c_int)(prototype)

# Test ctypes.CFUNCTYPE with structs
class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

def prototype(arg):
    return arg

ctypes.CFUNCTYPE(None, ctypes.POINTER(S))(prototype)

# Test ctypes.PYFUNCTYPE
def prototype(arg):
    return arg

ctypes.PYFUNCTYPE(None, ctypes.c_int)(prototype)

# Test ctypes.PYFUNCTYPE with structs
class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

def prototype(arg):
    return arg

ctypes.PYFUNCTYPE(None, ctypes.POINTER(S))(prototype)

# Test ctypes.WINFUNCTYPE
def prototype(arg):
    return
