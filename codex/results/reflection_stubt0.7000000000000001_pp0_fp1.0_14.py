fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__qualname__ = 'fn'

def assertRaises(exc, fun, *args, **kwds):
    try:
        fun(*args, **kwds)
    except exc:
        pass
    else:
        raise AssertionError("%s not raised" % exc)

assertRaises(TypeError, fn)

# Issue #24917: Fix a recursion error.
def g():
    pass
g.__code__ = g.__code__
g()
