import ctypes
# Test ctypes.CFUNCTYPE(None)
def cb():
    print("callback")
    return
cb = ctypes.CFUNCTYPE(None)(cb)
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def cb1(arg):
    return arg * 2
cb1 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(cb1)
# Test ctypes.CFUNCTYPE(ctypes.c_wchar_p, ctypes.c_int)
def cb2(arg):
    return "callback invoked with {}".format(str(arg))
cb2 = ctypes.CFUNCTYPE(ctypes.c_wchar_p, ctypes.c_int)(cb2)
############################################################################
# END OF FUNCTIONS
############################################################################
# Example with no init
