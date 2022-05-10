import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_call_c_function():
    assert fun() == "hello"

def test_call_c_function_in_loop():
    for i in range(100):
        assert fun() == "hello"

def test_call_c_function_in_loop_with_error():
    for i in range(100):
        try:
            fun()
        except:
            pass

def test_call_c_function_in_loop_with_error_and_except():
    for i in range(100):
        try:
            fun()
        except:
            pass
        else:
            assert fun() == "hello"
