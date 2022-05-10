import types
# Test types.FunctionType
#
# Test that a function can be created with types.FunctionType and
# that the function can be called.
#

from types import FunctionType

def f(x):
    return x

def g(x):
    return x

def h(x):
    return x

def test_function_type():
    F = FunctionType(f.__code__, f.__globals__)
    assert F(1) == 1
    assert F(1.0) == 1.0
    assert F(1+1j) == 1+1j
    assert F('a') == 'a'
    assert F(None) is None
    assert F(True) is True
    assert F(False) is False
    raises(TypeError, F)
    raises(TypeError, F, 1, 2)
    raises(TypeError, F, x=1)
    raises(TypeError, F, 1, x=1)
    raises(TypeError, F, x=1, y=1)

    F = FunctionType(g.__code__, g.
