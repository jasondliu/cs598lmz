fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

def f(x):
    if x:
        return f(x-1)
    return fn()

f(1e6)

# check that the stack size is not too large
def f(x):
    return f(x-1)

f(1e6)
