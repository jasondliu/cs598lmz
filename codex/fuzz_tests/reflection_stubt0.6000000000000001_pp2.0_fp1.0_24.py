fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

def f():
    def g():
        return g
    return g

del f()()

def f():
    def g():
        return g
    return g

del f()()

def f(x):
    def g():
        return g
    return g

del f(1)()

def f(x):
    def g():
        return g
    return g

del f(1)()

def f(x, y):
    def g():
        return g
    return g

del f(1, 2)()

def f(x, y):
    def g():
        return g
    return g

del f(1, 2)()

def f(x, y, z):
    def g():
        return g
    return g

del f(1, 2, 3)()

def f(x, y, z):
    def g():
        return g
    return g

del f(1, 2, 3)()

def f(x, y, z, t):
