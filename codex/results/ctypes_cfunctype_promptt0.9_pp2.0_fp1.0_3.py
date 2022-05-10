import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_longlong, ctypes.c_char, ctypes.c_char)
@ctypes.CFUNCTYPE(ctypes.c_longlong, ctypes.c_char, ctypes.c_char)
# Declaration                                                                                   
class fptr(object):
    def __call__(self, *args, **kwds): pass
    def _as_parameter_
