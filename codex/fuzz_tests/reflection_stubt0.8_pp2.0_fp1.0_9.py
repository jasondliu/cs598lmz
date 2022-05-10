fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__closure__ = (lambda: None,)
fn()  # attr "gi_frame" not set

def f():
    x = 3
    f.__closure__[0] = lambda: x
    f.__closure__[1] = lambda: x
    return f.__closure__
def g():
    return f()[0]()
def h():
    return f()[1]()
g()
h()  # assert 0
def f():
    x = 3
    f.__closure__[0] = lambda: x
    f.__closure__[1] = lambda: x
    return f.__closure__
f = f()
f[0]()
f[1]()  # assert 0
def f():
    x = 3
    f.__closure__[0] = lambda: x
    f.__closure__[1] = lambda: x
    return f.__closure__
f = f()
f[0]()
f[1]()  # assert 0
def f():
    x = 3
    f.
