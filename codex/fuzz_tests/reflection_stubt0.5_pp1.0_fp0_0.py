fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# https://bugs.python.org/issue33296
def f():
    def g():
        yield
    g().__del__()
f()

# https://bugs.python.org/issue33296
def f():
    def g():
        yield from ()
    g().__del__()
f()

# https://bugs.python.org/issue33296
def f():
    def g():
        yield
    g().send(None)
f()

# https://bugs.python.org/issue33296
def f():
    def g():
        yield from ()
    g().send(None)
f()

# https://bugs.python.org/issue33296
def f():
    def g():
        yield
    g().throw(Exception)
f()

# https://bugs.python.org/issue33296
def f():
    def g():
        yield from ()
    g().throw(Exception)
f()

# https://bugs.python.org/issue33296
def f():
