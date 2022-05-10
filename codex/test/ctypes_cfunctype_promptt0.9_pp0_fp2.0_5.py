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


