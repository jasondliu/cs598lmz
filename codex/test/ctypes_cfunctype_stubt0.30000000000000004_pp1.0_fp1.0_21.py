import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_fun():
    assert fun() == "hello"

def test_fun_call():
    assert fun.__call__() == "hello"

def test_fun_call_with_args():
    with pytest.raises(TypeError):
        fun.__call__(1)

def test_fun_call_with_kwargs():
    with pytest.raises(TypeError):
        fun.__call__(a=1)

def test_fun_call_with_args_and_kwargs():
    with pytest.raises(TypeError):
        fun.__call__(1, a=1)

def test_fun_call_with_args_and_kwargs_and_starargs():
    with pytest.raises(TypeError):
        fun.__call__(1, a=1, *(2,))

