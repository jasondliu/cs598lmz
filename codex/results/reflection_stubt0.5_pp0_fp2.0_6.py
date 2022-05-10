fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# In PyPy, this is a TypeError, but in CPython it's an AttributeError.
# https://bugs.python.org/issue30338
def fn():
    fn.__code__ = 2
fn()

# This is a TypeError in PyPy, but an AttributeError in CPython.
# https://bugs.python.org/issue30338
def fn():
    fn.__code__ = lambda: None
fn()

# This is a TypeError in PyPy, but an AttributeError in CPython.
# https://bugs.python.org/issue30338
def fn():
    fn.__code__ = object()
fn()

# This is a TypeError in PyPy, but an AttributeError in CPython.
# https://bugs.python.org/issue30338
def fn():
    fn.__code__ = [1, 2, 3]
fn()

# This is a TypeError in PyPy, but an AttributeError in CPython.
# https://bugs.python.org/issue30338
def fn():
