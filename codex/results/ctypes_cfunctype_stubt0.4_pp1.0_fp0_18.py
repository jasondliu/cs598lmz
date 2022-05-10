import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def test_function_type():
    fn = fun()
    assert fn() == 1

def test_function_type_with_arg():
    @FUNTYPE
    def fun(x):
        return x + 1
    fn = fun(1)
    assert fn() == 2

def test_function_type_with_args():
    @FUNTYPE
    def fun(x, y):
        return x + y
    fn = fun(1, 2)
    assert fn() == 3

def test_function_type_with_kwds():
    @FUNTYPE
    def fun(x, y):
        return x + y
    fn = fun(x=1, y=2)
    assert fn() == 3

def test_function_type_with_args_and_kwds():
    @FUNTYPE
    def fun(x, y):
        return x + y
    fn = fun(1, y=2)
    assert fn() == 3

def test_function_type_with_kwds_and_args():
    @FUN
