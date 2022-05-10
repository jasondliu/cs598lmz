import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def test_fun():
    fun()

def test_fun_with_arg():
    fun(1)

def test_fun_with_kwarg():
    fun(x=1)

def test_fun_with_arg_and_kwarg():
    fun(1, x=1)

def test_fun_with_kwarg_and_arg():
    fun(x=1, 1)

def test_fun_with_kwarg_and_arg_and_kwarg():
    fun(x=1, 1, x=1)

def test_fun_with_kwarg_and_arg_and_kwarg_and_arg():
    fun(x=1, 1, x=1, 1)

def test_fun_with_kwarg_and_arg_and_kwarg_and_arg_and_kwarg():
    fun(x=1, 1, x=1, 1, x=1)

def test_fun_with_kwarg_and_arg_and_kwarg_and_arg_and
