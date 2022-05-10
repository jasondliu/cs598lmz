fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# https://bugs.python.org/issue33861
def f():
    def g():
        yield
    return g

f()()

# https://bugs.python.org/issue34118
def f():
    def g():
        yield
    return g

f()()

# https://bugs.python.org/issue34119
def f():
    def g():
        yield
    return g

f()()

# https://bugs.python.org/issue34120
def f():
    def g():
        yield
    return g

f()()

# https://bugs.python.org/issue34121
def f():
    def g():
        yield
    return g

f()()

# https://bugs.python.org/issue34122
def f():
    def g():
        yield
    return g

f()()

# https://bugs.python.org/issue34123
def f():
    def g():
        yield
    return g

f()()

# https
