fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

def f(a, b, c):
    return a, b, c
f(*(i for i in range(3)))

def g():
    fn = lambda a, b, c: (a, b, c)
    return fn(*(i for i in range(3)))
g()

def f(a, b, *c):
    return a, b, c
f(*(i for i in range(3)))

def g():
    fn = lambda a, b, *c: (a, b, c)
    return fn(*(i for i in range(3)))
g()

def f(a, b, *c, **d):
    return a, b, c, d
f(*(i for i in range(3)), **{'a': 1, 'b': 2})

def g():
    fn = lambda a, b, *c, **d: (a, b, c, d)
    return fn(*(i for i in range(3)), **{'a': 1, 'b': 2})
g
