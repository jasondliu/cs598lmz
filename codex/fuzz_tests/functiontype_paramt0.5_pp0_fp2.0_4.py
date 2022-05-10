from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo'))

# Issue #1390
def f():
    return 1
f.__class__ = type(lambda: None)
list(f)

# Issue #1390, but with a different twist
def f():
    return 1
f.__class__ = type(lambda: None)
list(f())

# Issue #1390, but with a different twist
def f():
    return 1
f.__class__ = type(lambda: None)
list(f())

# Issue #1390, but with a different twist
def f():
    return 1
f.__class__ = type(lambda: None)
list(f())

# Issue #1390, but with a different twist
def f():
    return 1
f.__class__ = type(lambda: None)
list(f())

# Issue #1390, but with a different twist
def f():
    return 1
f.__class__ = type(lambda: None)
list(f())

# Issue #1390, but with a different twist
def f
