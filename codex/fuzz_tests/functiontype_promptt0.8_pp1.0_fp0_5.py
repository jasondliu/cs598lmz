import types
# Test types.FunctionType (which, incidentally, is *not* the same as
# types.BuiltinFunctionType, which is what is returned by evaluating a
# Python builtin like 'abs' or 'min'):
def func(): pass
def test_is1():
    assert isinstance(func, types.FunctionType)
def test_is2():
    assert not isinstance(1, types.FunctionType)
def test_is3():
    class C:
        def f(self): pass
    assert isinstance(C().f, types.FunctionType)
def test_is4():
    def g(): pass
    def h(): pass
    assert g != h
    assert g.__name__ == h.__name__
    assert g.__name__ == 'g'
    assert g.__doc__ == h.__doc__
    assert g.__doc__ == None
    assert g.__defaults__ == h.__defaults__
    assert g.__defaults__ == None
    assert g.__closure__ == h.__closure__
    assert g.__closure__ == None
    assert g.
