import ctypes
ctypes.cast(0, ctypes.py_object)

# ____________________________________________________________

def test_py_object_as_parameter():
    class X(object):
        pass
    x = X()
    def f(x):
        return x
    assert f(x) is x

def test_py_object_as_return_value():
    class X(object):
        pass
    x = X()
    def f():
        return x
    assert f() is x

def test_py_object_as_field():
    class X(object):
        pass
    x = X()
    class Y(object):
        pass
    y = Y()
    y.x = x
    assert y.x is x

def test_py_object_as_list_item():
    class X(object):
        pass
    x = X()
    l = [x]
    assert l[0] is x

def test_py_object_as_dict_value():
    class X(object):
        pass
    x = X()
    d =
