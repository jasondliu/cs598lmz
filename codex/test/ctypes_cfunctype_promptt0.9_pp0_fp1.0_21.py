import ctypes
# Test ctypes.CFUNCTYPE (Issue #2605)

ctypes.CFUNCTYPE(ctypes.c_int)(lambda: 0)
ctypes.CFUNCTYPE(ctypes.c_int)()

# a simple test that doesn't fail on 2.6 through 2.7
try:
    ctypes.CFUNCTYPE(ctypes.c_int)(lambda: None, lambda errno: 0)
except TypeError:
    pass

# Check whether top-level structure do not cause segfaults
# XXX later!
#ctypes.Structure
#ctypes.Structure()._fields_

# Test the hash() of pointers
