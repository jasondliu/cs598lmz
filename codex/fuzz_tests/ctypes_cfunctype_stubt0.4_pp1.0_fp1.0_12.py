import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_ctypes_callback():
    assert fun() == "hello"

def test_ctypes_callback_with_args():
    @FUNTYPE
    def fun(x):
        return x
    assert fun(42) == 42

def test_ctypes_callback_with_kwargs():
    @FUNTYPE
    def fun(x=None):
        return x
    assert fun(x=42) == 42

def test_ctypes_callback_with_args_and_kwargs():
    @FUNTYPE
    def fun(x, y=None):
        return x, y
    assert fun(42, y=43) == (42, 43)

def test_ctypes_callback_with_args_and_kwargs_with_default():
    @FUNTYPE
    def fun(x, y=43):
        return x, y
    assert fun(42) == (42, 43)

def test_ctypes_callback_with_args_and_kwargs_with_default_and_args():
    @FUNTYPE
