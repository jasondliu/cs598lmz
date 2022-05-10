fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
assert_raises(TypeError, eval, fn.__code__, "foo")


# Issue #3840
def f():
    x = 3
    def g():
        return x
    return g

assert f()() == 3
