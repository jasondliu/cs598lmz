import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello world"

def test_call():
    d = {}
    d["fun"] = fun
    assert "hello world" == d["fun"]()

def test_call_no_dict():
    # This is a regression test for a crash that occurred when calling
    # a function that was not in a dictionary.
    assert "hello world" == fun()

def test_call_no_dict_with_arg():
    # This is a regression test for a crash that occurred when calling
    # a function that was not in a dictionary.
    assert "hello world" == fun("foo")

def test_call_no_dict_with_kwargs():
    # This is a regression test for a crash that occurred when calling
    # a function that was not in a dictionary.
    assert "hello world" == fun(bar="foo")

def test_call_no_dict_with_arg_and_kwargs():
    # This is a regression test for a crash that occurred when calling
    # a function that was not in a dictionary.
    assert "hello world" == fun("
