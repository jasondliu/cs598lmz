fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that we can call a function that has a generator as a closure
def f(x):
    yield x
    yield x+10
    yield x+20
g = f(1)
g.__closure__ = (g,)
g()

# Test that we can call a function that has a generator as a closure,
# and that the generator can be used as a closure.
def f(x):
    yield x
    yield x+10
    yield x+20
g = f(1)
g.__closure__ = (g,)
g()
next(g)
next(g)

# Test that we can call a function that has a generator as a closure,
# and that the generator can be used as a closure.
def f(x):
    yield x
    yield x+10
    yield x+20
g = f(1)
g.__closure__ = (g,)
g()
next(g)
next(g)

# Test that we can call a function that has a generator as a closure,
# and that the generator can
