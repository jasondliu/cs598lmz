import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def c_callback(arg1, arg2):
    return arg1 * arg2
CALLBACK = FUNTYPE(c_callback)
# test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def ctypes_callback():
    lib.call_with_callback(CALLBACK)

# test ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)
@CALLBACK
def py_callback(arg1, arg2):
    print('arg1=%d, arg2=%d' % (arg1, arg2))
def test_py_callback():
    lib.call_with_callback(py_callback)

def test_callback_no_args():
    lib.call_with_callback_no_args(CALLBACK)

def test_callback_return_float():
    lib.call_with_callback_return_float(CALL
