import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_function_call():
    fun()

def test_function_call_with_args():
    fun(1, 2, 3)

def test_function_call_with_kwargs():
    fun(a=1, b=2, c=3)

def test_function_call_with_args_and_kwargs():
    fun(1, 2, 3, a=1, b=2, c=3)

def test_function_call_with_exception():
    try:
        fun(1, 2, 3, a=1, b=2, c=3, error=True)
    except Exception as e:
        pass

def test_function_call_with_exception_and_catch():
    try:
        fun(1, 2, 3, a=1, b=2, c=3, error=True)
    except Exception as e:
        pass
    else:
        pass

def test_function_call_with_exception_and_catch_and_finally():
   
