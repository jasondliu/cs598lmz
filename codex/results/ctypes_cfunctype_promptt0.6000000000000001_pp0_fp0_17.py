import ctypes
# Test ctypes.CFUNCTYPE.
def PYFUNC(*args):
    return ctypes.c_int(42)

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, *args)

f = PYFUNC
assert f(1,2,3) == 42

f = CMPFUNC(PYFUNC)
assert f(1,2,3) == 42

f = CMPFUNC(lambda *args: ctypes.c_int(43))
assert f(1,2,3) == 43

f = lambda *args: ctypes.c_int(44)
assert f(1,2,3) == 44

f = CMPFUNC(lambda *args: ctypes.c_int(45))
assert f(1,2,3) == 45

f = CMPFUNC(f)
assert f(1,2,3) == 44

f = CMPFUNC(CMPFUNC(f))
assert f(1,2,3) == 44

f = CMPFUNC(CMPFUNC
