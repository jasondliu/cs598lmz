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
if sys.platform == "win32":
    from ctypes import windll
    # The scandll() function is not implemented on S60
    scandll = windll.Sc_cw32
    scandll.scandll.argtypes = (ctypes.c_int,)
    scandll.scandll.restype = ctypes.c_int
    scandll.scandll(1)
    hash(sc
