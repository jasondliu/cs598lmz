fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

def g():
    raise RuntimeError

def f():
    g()

f.__code__ = fn
