import ctypes
# Test ctypes.CFUNCTYPE
def test_cfunctype():
    # Check that ctypes.CFUNCTYPE() accepts a tuple of types
    ctypes.CFUNCTYPE(ctypes.c_int, (ctypes.c_int, ctypes.c_int))
    # Check that ctypes.CFUNCTYPE() accepts a list of types
    ctypes.CFUNCTYPE(ctypes.c_int, [ctypes.c_int, ctypes.c_int])

# Test ctypes.c_char_p.in_dll()
def test_c_char_p_in_dll():
    # Issue #1728: ctypes.c_char_p.in_dll() must return None when
    # the address is NULL
    if sys.platform == 'win32':
        libc = ctypes.cdll.msvcrt
    else:
        libc = ctypes.cdll.LoadLibrary(None)
    # NULL pointer
    assert ctypes.c_char_p.in_dll(libc, "some_unexisting_symbol")
