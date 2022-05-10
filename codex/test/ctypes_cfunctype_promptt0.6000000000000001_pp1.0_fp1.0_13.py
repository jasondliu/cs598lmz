import ctypes
# Test ctypes.CFUNCTYPE(None)
# <https://bugs.python.org/issue26761>

if __name__ == '__main__':
    import sys
    import os
    if sys.platform == 'win32':
        libc = ctypes.WinDLL(None)
    else:
        libc = ctypes.CDLL(None)
    #
    # XXX: on some systems, sigaction() is not available
    #
