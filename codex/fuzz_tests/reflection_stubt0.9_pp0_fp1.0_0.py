fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

class A:
    """..."""
    pass

def f(x):
    """..."""
    x.__doc__
    fn.__code__

"""
def f():
    'foo'
    (1 for i in ())
    def g(): 'foo'
    class B: 'foo'
    [('foo', 'foo'), ('foo', 'f
