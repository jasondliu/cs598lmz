import ctypes
# Test ctypes.CFUNCTYPE()
def func(a, b):
    print("func() called with %d and %d" % (a, b))

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

cmpptr = CMPFUNC(func)
assert cmpptr(2, 3) == 0

# Test ctypes.WINFUNCTYPE()
# TODO: This test fails on 64-bit Windows
if sys.platform == 'win32' and ctypes.sizeof(ctypes.c_void_p) == 4:
    from ctypes import wintypes
    def func(a, b):
        print("func() called with %d and %d" % (a, b))
        return a * b
    CMPFUNC = ctypes.WINFUNCTYPE(wintypes.UINT, wintypes.UINT, wintypes.UINT)
    cmpptr = CMPFUNC(func)
    assert cmpptr(2, 3) == 6


