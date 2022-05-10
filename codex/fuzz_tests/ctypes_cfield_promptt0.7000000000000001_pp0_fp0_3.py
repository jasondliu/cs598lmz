import ctypes
# Test ctypes.CField
class Point(Structure):
    _fields_ = [('x', c_int),
                ('y', c_int)]

class Device(Structure):
    _fields_ = [('version', c_int),
                ('name', c_char * 4),
                ('point', Point)]

test_dev = Device(1, 'dev', Point(1, 2))
assert test_dev.version == 1
assert test_dev.name == b'dev'
assert test_dev.point.x == 1
assert test_dev.point.y == 2

# Test ctypes.CDLL
libm = CDLL(ctypes.util.find_library('m'))

# If a function has already been called, ctypes caches the argument types
# and calling the function with different types will cause segfault.
# Uncomment the following code to see the error.

# libm.sin(1.0)
# libm.sin(c_double(1.0))
# libm.sin(c_int(1))

# Test ctypes.c_char_
