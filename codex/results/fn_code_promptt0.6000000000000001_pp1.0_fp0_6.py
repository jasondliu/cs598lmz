fn = lambda: None
# Test fn.__code__.co_varnames and fn.__code__.co_argcount
def test_func_code():
    fn.__code__ = c1
    assert fn.__code__.co_varnames == ('x', 'y', 'z')
    assert fn.__code__.co_argcount == 3
    # Test co_cellvars and co_freevars
    def f1(x):
        y = x
        def g(z):
            return x + y + z
        return g
    assert f1.__code__.co_varnames == ('x', 'y', 'z', 'g')
    assert f1.__code__.co_argcount == 1
    assert f1.__code__.co_cellvars == ('x', 'y')
    assert f1.__code__.co_freevars == ()
    def f2(x):
        y = x
        def g(z):
            return x + y + z
        def h():
            return x + y
        return g, h
    assert f2.
