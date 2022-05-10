fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# https://bugs.python.org/issue34156
def f():
    yield
    return
f().__code__ = None

# https://bugs.python.org/issue34157
def f():
    yield
    return
f().__code__ = 1

# https://bugs.python.org/issue34158
def f():
    yield
    return
f().__code__ = 'a'

# https://bugs.python.org/issue34159
def f():
    yield
    return
f().__code__ = object()

# https://bugs.python.org/issue34160
def f():
    yield
    return
f().__code__ = type

# https://bugs.python.org/issue34161
def f():
    yield
    return
f().__code__ = f

# https://bugs.python.org/issue34162
def f():
    yield
    return
f().__code__ = f()

# https://bugs.python.org/issue34163
def f():
