fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
del gi
fn()

# https://bugs.python.org/issue30932
def f():
    return
def g():
    return f().__code__.co_flags
g()

# https://bugs.python.org/issue30932
class A:
    pass
A.__new__.__code__.co_flags

# https://bugs.python.org/issue30932
def f():
    pass
f.__code__.co_flags

# https://bugs.python.org/issue30932
def f():
    pass
f.__code__.co_flags

# https://bugs.python.org/issue30932
def f():
    pass
f.__code__.co_flags

# https://bugs.python.org/issue30932
def f():
    pass
f.__code__.co_flags

# https://bugs.python.org/issue30932
def f():
    pass
f.__code__.co_flags

# https://bugs.python.org/issue
