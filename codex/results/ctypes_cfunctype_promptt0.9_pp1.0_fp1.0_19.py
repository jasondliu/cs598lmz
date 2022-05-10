import ctypes
# Test ctypes.CFUNCTYPE
c_int_type = ctypes.c_int

def py_callback_test(a, b, c):
    print('py_callback_test,', a, b, c)
    return py_callback_test.counter
py_callback_test.counter = 0

c_callback_test = ctypes.CFUNCTYPE(c_int_type, c_int_type, c_int_type,
                                   c_int_type)(py_callback_test)

def test_c_callback():
    # Python Function -> C Function Callbacks
    assert call_callback(c_callback_test, 3, 5, 8) == 0
    assert py_callback_test.counter == 1

@ctypes.CFUNCTYPE(None, c_int_type, c_int_type, c_int_type)
def py_callback_test(a, b, c):
    print('py_callback_test,', a, b, c)
    py_callback_test.counter += 1
py_callback_test.counter = 0


# Test
