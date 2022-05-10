fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Regression test for issue #15516
def f(x):
    def g(y):
        return x+y
    return g

assert f(1)(2) == 3

# Regression test for issue #16224
def f():
    def g():
        return g
    return g

assert f()() is f()()

# Regression test for issue #16224
def f():
    def g():
        return g
    return g

assert f()() is f()()

# Regression test for issue #16224
def f():
    def g():
        return g
    return g

assert f()() is f()()

# Regression test for issue #16224
def f():
    def g():
        return g
    return g

assert f()() is f()()

# Regression test for issue #16224
def f():
    def g():
        return g
    return g

assert f()() is f()()

# Regression test for issue #16224
def f():
