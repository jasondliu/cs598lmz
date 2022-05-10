fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_call_with_kwargs_and_starargs
def f(a, b, c):
    return a, b, c

def g(a, b, c, d):
    return a, b, c, d

def h(a, b, c, d, e):
    return a, b, c, d, e

def i(a, b, c, d, e, f):
    return a, b, c, d, e, f

def j(a, b, c, d, e, f, g):
    return a, b, c, d, e, f, g

def k(a, b, c, d, e, f, g, h):
    return a, b, c, d, e, f, g, h

def l(a, b, c, d, e, f, g, h, i):
    return a, b, c, d, e, f, g, h, i

def m(a, b, c, d, e, f, g
