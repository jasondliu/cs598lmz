import ctypes
# Test ctypes.CFUNCTYPE
#
def call_func(f):
    f()

callit = ctypes.CFUNCTYPE(None)(call_func)
callit(None)
