import ctypes
# Test ctypes.CFUNCTYPE(None)
def test_CFUNCTYPE_None():
    import ctypes
    # note: we need to keep the cbtype object around to keep the
    # callback type alive, otherwise the following callback
    # would fail
    cbtype = ctypes.CFUNCTYPE(None)
    cbtype(_callback_noargs)
    _callback_noargs()

@ctypes.CFUNCTYPE(ctypes.c_char_p)
def test_CFUNCTYPE_decorator():
    _callback_str()
def test_CFUNCTYPE_decorator_assign():
    _callback_str2 = ctypes.CFUNCTYPE(ctypes.c_char_p)(_callback_str)
    _callback_str2()

def test_CFUNCTYPE_decorator_assign_parameter():
    _callback_str2 = ctypes.CFUNCTYPE(ctypes.c_char_p, ctypes.c_int)(_callback_str)
    _callback_str2(
