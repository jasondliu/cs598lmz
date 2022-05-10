import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

# Test the expr_context attribute.
def test_expr_context():
    assert S.x.expr_context is ctypes.c_int.expr_context

# Test the __get__ and __set__ methods.
def test_getset():
    s = S()

    # Default value is 0.
    assert s.x == 0

    s.x = 42
    assert s.x == 42

    # Assigning an invalid value raises an exception.
    py.test.raises(TypeError, "s.x = 'foo'")

    del s.x
    assert s.x == 0

    # Deleting an invalid value raises an exception.
    py.test.raises(TypeError, "delattr(s, 'foo')")

# Test the from_param method.
def test_from_param():
    def f(x):
        pass

    # Passing S.x as a parameter should work.
    f(S.x)

    # Passing a field by name should not work.
    py.test.raises(TypeError, "f('x
