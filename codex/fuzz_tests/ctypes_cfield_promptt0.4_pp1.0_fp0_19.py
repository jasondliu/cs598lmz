import ctypes
# Test ctypes.CField
class POINT(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]
p = POINT(1, 2)
print(p.x, p.y)

class POINT(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]
p = POINT(1, 2)
print(p.x, p.y)

# Test ctypes.CField.from_param
class POINT(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]
p = POINT(1, 2)
print(p.x, p.y)

# Test ctypes.CField.from_address
class POINT(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]
p = POINT(
