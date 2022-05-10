fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue 1785, stack overflow in function that returns itself
def f():
    f()
f()

def g():
    return g()
g()

# Issue 2129, segfault with deeply nested yield expressions
def h():
    return (yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((yield from ((
