import ctypes
# Test ctypes.CFUNCTYPE
@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)
def cb(s):
    return len(s)

class C(ctypes.Structure):
    _fields_ = [('cb', ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p))]

assert C.cb(b'abc') == 3
assert C(cb).cb(b'def') == 3

# Test ctypes.PYFUNCTYPE
@ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_char_p)
def python_cb(s):
    return len(s)

class C(ctypes.Structure):
    _fields_ = [('cb', ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_char_p))]

assert C.cb(b'abc') == 3
assert C(python_cb).cb(b'def') == 3

# Test ctypes.
