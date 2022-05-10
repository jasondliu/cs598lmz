import ctypes
# Test ctypes.CFUNCTYPE.

# Uncomment to test the crash.
#ctypes.CFUNCTYPE = None

import _ctypes_test

@_ctypes_test.callit
def func(*args):
    return len(args)

if __name__ == '__main__':
    print(func())
    print(func(1))
    print(func(1, 2))
    print(func(1, 2, 3))
    print(func(1, 2, 3, 4))
    print(func(1, 2, 3, 4, 5))
