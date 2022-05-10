import ctypes
# Test ctypes.CFUNCTYPE
#
def test_cfunctype():
    #
    # This test is mostly a copy of test_callbacks.py
    #
    import _ctypes_test
    dll = ctypes.CDLL(_ctypes_test.__file__)
    callback = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(_testfunc_10)
    res = dll.set_callback(callback)
    assert res == 0
    res = dll.call_callback(5)
    assert res == 50
    #
    # Test a CFUNCTYPE function as a function pointer
    #
    CallbackType = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
    fptr = ctypes.cast(callback, ctypes.POINTER(CallbackType))
    res = dll.call_callback(5)
    assert res == 50
    #
    # Test a CFUNCTYPE function as a function pointer,
    # passing the function pointer to another dll.
   
