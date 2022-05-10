import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("fun called")
    return 42

def test_simple():
    fun2 = fun.__call__
    assert fun2() == 42

def test_py_object():
    fun3 = ctypes.py_object(fun)
    assert fun3() == 42

def test_call_noncallable():
    raises(TypeError, "fun.__call__(42)")

def test_call_wrong_arg():
    raises(TypeError, "fun.__call__(42, 42)")

def test_call_kwargs():
    raises(TypeError, "fun.__call__(x=42)")

def test_call_noncallable_2():
    raises(TypeError, "ctypes.py_object(42)")

def test_call_wrong_arg_2():
    raises(TypeError, "ctypes.py_object(42, 42)")

def test_call_kwargs_2():
    raises(TypeError, "ctypes.py_object(x=42)")

def test_call
