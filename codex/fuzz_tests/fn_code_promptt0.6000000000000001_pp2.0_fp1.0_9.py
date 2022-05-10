fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = ('a', 'b', 'c')
# Test fn.__code__.co_argcount
fn.__code__.co_argcount = 3
# Test fn.__code__.co_flags
fn.__code__.co_flags = 0

def test_bind_args():
    def fn(a, b, c):
        pass

    fn2 = bind_args(fn, 1, 2)
    assert fn2.__code__.co_varnames == ('c',)
    assert fn2.__code__.co_argcount == 1
    assert fn2.__code__.co_flags == 0

def test_bind_args_with_default():
    def fn(a, b=1):
        pass

    fn2 = bind_args(fn, 1)
    assert fn2.__code__.co_varnames == ()
    assert fn2.__code__.co_argcount == 0
    assert fn2.__code__.co_flags == 0
