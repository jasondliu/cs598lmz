fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# issue #2
# https://github.com/pybee/thonny/issues/2

def f(x):
    return x

print(f(g()))

def g():
    return f()

# issue #3
# https://github.com/pybee/thonny/issues/3

def f1(x):
    return x

f2 = lambda: None
f2.__code__ = f1.__code__

f2()

# issue #4
# https://github.com/pybee/thonny/issues/4

def g1():
    return x

g2 = lambda: None
g2.__code__ = g1.__code__

def f1(x):
    return g2()

f2 = lambda: None
f2.__code__ = f1.__code__

f2(1)

# issue #5
# https://github.com/pybee/thonny/issues/5

def f(x):
    return
