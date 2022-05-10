import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_call_c_function():
    res = interp.eval("(call-c-function %d)" % (int(fun)))
    assert res == "hello"

def test_call_c_function_with_args():
    res = interp.eval("(call-c-function %d 1 2 3)" % (int(fun)))
    assert res == "hello"

def test_call_c_function_with_args_and_kwargs():
    res = interp.eval("(call-c-function %d 1 2 3 :foo 'bar)" % (int(fun)))
    assert res == "hello"

def test_call_c_function_with_args_and_kwargs_and_return_value():
    res = interp.eval("(call-c-function %d 1 2 3 :foo 'bar :return-value 'baz)" % (int(fun)))
    assert res == "baz"

def test_call_c_function_with_args_and_kwargs_and_return_value
