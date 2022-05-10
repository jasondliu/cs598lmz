import ctypes
# Test ctypes.CFUNCTYPE and _ctypes.PyCFuncPtr
# The test started to fail in 64 bit mode when the first parameter was passed
# in the wrong register (edx)
def func(a=0, b=1, c=2):
    for x in a, b, c:
        if not isinstance(x, int):
            print('TypeError')
            return
    print('%d %d %d' % (a, b, c))


if struct.calcsize('P') == 4:
    FUNC = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int, ctypes.c_int)
else:
    FUNC = ctypes.CFUNCTYPE(None, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong)
f = FUNC(func)
f(4, 5, 6)
f()
f(c=9)
f(1, c=9)
f(1, 2, c=9)

f = FUNC(None, None)
