import ctypes
# Test ctypes.CFUNCTYPE() and ctypes.POINTER() 
#
# As of ctypes 1.0, it seems that the only allowed call to these is
# as function calls.  This seems like a flaw, and something that will
# eventually be fixed.  For now, let's work around it.
#

def main():
    import ctypes

    # a function pointer.
    assert ctypes.cast(0, ctypes.POINTER(ctypes.CFUNCTYPE(ctypes.c_int))).value is None

    # a void pointer.
    assert ctypes.cast(0, ctypes.POINTER(ctypes.c_void_p)).value == 0

    # a pointer to a function pointer
    assert ctypes.cast(1, ctypes.POINTER(ctypes.POINTER(ctypes.CFUNCTYPE(ctypes.c_int)))).contents.value == 1

    # A structure.  It should not be allowed at this level.
    try:
        ctypes.cast(0, ctypes.POINTER(ctypes.Structure))
    except TypeError:
