fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

def f():
    return fn()

# The issue was an assertion failure in the code that checks that the
# code object has the right size.
