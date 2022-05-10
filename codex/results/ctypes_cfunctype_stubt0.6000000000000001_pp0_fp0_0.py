import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

assert fun() == 42

# Issue #3075
c_int_p = ctypes.POINTER(ctypes.c_int)
c_int_p_p = ctypes.POINTER(c_int_p)
assert repr(c_int_p_p) == "<ctypes type 'int * *'>"
assert repr(c_int_p_p.from_address(0)) == "<ctypes type 'int * *' NULL>"

# Issue #3237
def test_find_library():
    try:
        import ctypes.util
    except ImportError:
        skip("ctypes.util is not available on this platform")
    try:
        ctypes.util.find_library('c')
    except OSError:
        skip("ctypes.util.find_library('c') failed")
    if ctypes.util.find_library('c') != ctypes.util.find_library('c'):
        skip("ctypes.util.find_library('c') returns different values")

# Issue #3421
try
