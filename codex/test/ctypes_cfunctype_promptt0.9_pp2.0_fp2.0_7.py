import ctypes
# Test ctypes.CFUNCTYPE
import ctypes
import ctypes.util # for find_library

#
# The 32-bit and 64-bit Windows API differs only slightly: c_char_p is
# used for 32-bit API strings, and c_wchar_p for 64-bit API strings.
#
def get_ctypes_argtypes(functype):
    if functype == ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p):
        return (ctypes.c_char_p,)
    if functype == ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_wchar_p):
        return (ctypes.c_wchar_p,)
    if functype == ctypes.CFUNCTYPE(None):
        return ()
    raise NotImplementedError("function type %s not yet implemented" %
                              (functype.__name__,))

