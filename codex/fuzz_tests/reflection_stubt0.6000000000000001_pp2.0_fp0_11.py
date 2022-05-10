fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.__code__
fn()

# The following may crash the interpreter
def f():
    fn()
f()
