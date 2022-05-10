import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def test_fun():
    assert fun() is None

def test_fun_type():
    assert type(fun) is FUNTYPE

def test_fun_instance():
    assert isinstance(fun, FUNTYPE)

def test_fun_callable():
    assert callable(fun)

def test_fun_repr():
    assert repr(fun) == '<CFUNCTYPE(<object>)(0x%x)>' % (id(fun),)

def test_fun_str():
    assert str(fun) == '<CFUNCTYPE(<object>)(0x%x)>' % (id(fun),)

def test_fun_get_doc():
    assert fun.__doc__ is None

def test_fun_set_doc():
    fun.__doc__ = 'doc'
    assert fun.__doc__ == 'doc'

def test_fun_get_name():
    assert fun.__name__ == 'fun'

def test_fun_set_name():
    fun.__
