import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'hello'

def f():
    return 'hello'

def test_function_type():
    assert fun() == 'hello'
    assert type(fun) is FUNTYPE
    assert fun.__name__ == 'fun'
    assert fun.__module__ == 'test_ctypes'
    assert fun.__doc__ == ''
    assert fun.__dict__ == {}
    assert fun.__defaults__ == ()
    assert fun.__code__.co_argcount == 0
    assert fun.__code__.co_kwonlyargcount == 0
    assert fun.__code__.co_nlocals == 1
    assert fun.__code__.co_stacksize == 2
    assert fun.__code__.co_flags == 67
    assert fun.__code__.co_code == b'|\x00|\x01\x17\x00S\x00'
    assert fun.__code__.co_consts == ('hello',)
    assert fun.__code__.co_names == ()
    assert fun.__code__.
