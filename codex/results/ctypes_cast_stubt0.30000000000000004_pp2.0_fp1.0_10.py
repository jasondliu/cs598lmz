import ctypes
ctypes.cast(0, ctypes.py_object)

# ____________________________________________________________

def test_py_object_as_parameter():
    class X(object):
        pass
    def f(x):
        return x
    x = X()
    assert f(x) is x

def test_py_object_as_return_value():
    class X(object):
        pass
    def f():
        return X()
    x = f()
    assert isinstance(x, X)

def test_py_object_as_field():
    class X(object):
        pass
    class Y(object):
        pass
    x = X()
    y = Y()
    y.x = x
    assert y.x is x

def test_py_object_as_list_item():
    class X(object):
        pass
    x = X()
    l = [x]
    assert l[0] is x

def test_py_object_as_dict_item():
    class X(object):
        pass
    x = X()
