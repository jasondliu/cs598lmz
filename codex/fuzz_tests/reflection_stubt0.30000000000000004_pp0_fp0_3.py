fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# issue #5
def f():
    yield
    yield
    yield
    yield

def g():
    yield
    yield
    yield
    yield

def h():
    yield
    yield
    yield
    yield

f.__code__ = g
g.__code__ = h
h.__code__ = f
f()

# issue #6
def f():
    yield
    yield
    yield
    yield

def g():
    yield
    yield
    yield
    yield

def h():
    yield
    yield
    yield
    yield

f.__code__ = g
g.__code__ = h
h.__code__ = f
g()

# issue #7
def f():
    yield
    yield
    yield
    yield

def g():
    yield
    yield
    yield
    yield

def h():
    yield
    yield
    yield
    yield

f.__code__ = g
g.__code__ = h
h.__code__ = f

