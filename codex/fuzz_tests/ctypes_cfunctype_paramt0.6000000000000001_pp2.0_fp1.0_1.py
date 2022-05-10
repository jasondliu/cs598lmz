import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def cfunc(func):
    return FUNTYPE(func)

@cfunc
def c_foo(x):
    return x*x

def foo(x):
    return x*x

def test_cfunc():
    assert c_foo(2) == 4
    assert c_foo(foo(2)) == 16
    assert foo(c_foo(2)) == 16

def test_cfunc_docstring():
    assert c_foo.__doc__ == '<built-in function foo>'

def test_cfunc_name():
    assert c_foo.__name__ == 'foo'

def test_cfunc_module():
    assert c_foo.__module__ == 'foo'

def test_cfunc_qualname():
    assert c_foo.__qualname__ == 'foo'

def test_cfunc_get_dict():
    assert c_foo.__dict__ is None

def test_cfunc_set_dict():
    with pytest.ra
