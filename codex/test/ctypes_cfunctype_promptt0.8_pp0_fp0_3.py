import ctypes
# Test ctypes.CFUNCTYPE with prototype
#  int (int, int)
#
# The actual function is the builtin function pow()

INT_INT_INT = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

if __name__=='__main__':
    import sys
    if len(sys.argv) > 1:
        libc = ctypes.CDLL(sys.argv[1])
    else:
        libc = ctypes.CDLL(None)
    pow = INT_INT_INT(libc.pow)

