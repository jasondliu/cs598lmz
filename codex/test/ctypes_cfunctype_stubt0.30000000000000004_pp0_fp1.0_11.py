import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

fun.__name__ = 'fun'

def test_call_with_py_object_return_value():
    assert fun() == 42
    assert fun.__name__ == 'fun'

def test_call_with_py_object_return_value_and_exception():
    def f():
        raise ValueError
    f.__name__ = 'f'
    raises(ValueError, f)
    assert f.__name__ == 'f'

def test_call_with_py_object_return_value_and_exception_and_finally():
    def f():
        try:
            raise ValueError
        finally:
            pass
    f.__name__ = 'f'
    raises(ValueError, f)
    assert f.__name__ == 'f'

def test_call_with_py_object_return_value_and_exception_and_finally_2():
    def f():
        try:
            raise ValueError
        finally:
            return 42
