import ctypes
# Test ctypes.CFUNCTYPE and ctypes.POINTER

# Functions accept None and python function objects, except that
# c_int(None) raises a TypeError, so all types will test for None
# explicitly.

# Test function types

def test_c_function(TYPE):
    if TYPE is None:
        return

    func = TYPE(lambda x: x)
    func.__name__ = 'test_function'
    func.__doc__ = 'docstring'
    assert func(2) == 2
    assert func.__doc__ == 'docstring'
    assert func.__name__ == 'test_function'
    func(1)

    func = TYPE(None)
    assert func is None

    func = TYPE(TYPE)
    assert func(2) == 2
    assert func(2.5) == 2
    # XXX: pass in NULL?

def test_c_function_int(TYPE):
    func = TYPE(lambda x: x)
    assert func(2.5) == 2
    func(1.5)
    raises(TypeError, "func('foo')")
