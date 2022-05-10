import ctypes
# Test ctypes.CField
class CFoo(ctypes.Structure):
    _fields_ = [('bar', ctypes.c_int)]
class CFoo2(ctypes.Structure):
    _fields_ = [('bar', ctypes.c_int),
                ('baz', ctypes.c_int)]

# Test ctypes.CField.from_address
class CFoo3(ctypes.Structure):
    _fields_ = [('bar', ctypes.c_int),
                ('baz', ctypes.c_int)]

# Test ctypes.CField.from_buffer
class CFoo4(ctypes.Structure):
    _fields_ = [('bar', ctypes.c_int),
                ('baz', ctypes.c_int)]

# Test ctypes.CField.from_buffer_copy
class CFoo5(ctypes.Structure):
    _fields_ = [('bar', ctypes.c_int),
                ('baz', ctypes.c_int)]

# Test ctypes.CField.in_dll
class CFoo6(
