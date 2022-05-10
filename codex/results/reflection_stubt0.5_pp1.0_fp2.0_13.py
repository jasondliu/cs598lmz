fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# https://bugs.python.org/issue34167
def f():
    def g(): pass
    g.__code__ = None
    return g
f()

# https://bugs.python.org/issue34167
def f():
    def g(): pass
    g.__code__ = {}
    return g
f()
