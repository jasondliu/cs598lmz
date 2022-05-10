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
    if hasattr(libc, 'sigaction'):
        # Allocate a signal handler
        #
        # XXX:  on some systems, signal.SIGALRM is not available
        #
        if hasattr(signal, 'SIGALRM'):
            sig_num = signal.SIGALRM
        else:
            sig_num = signal.SIGINT
        #
        # XXX:  on some systems, signal.SIG_DFL is not available
        #
        if hasattr(signal, 'SIG_DFL'):
            def_act = signal.SIG_DFL
        else:
           
