from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo'))

# Issue #16
def f(a, b):
    return a, b

list(f(1, 2))

# Issue #17
def f(a, b):
    return a, b

list(f(1, 2))

# Issue #18
def f(a, b):
    return a, b

list(f(1, 2))

# Issue #19
def f(a, b):
    return a, b

list(f(1, 2))

# Issue #20
def f(a, b):
    return a, b

list(f(1, 2))

# Issue #21
def f(a, b):
    return a, b

list(f(1, 2))

# Issue #22
def f(a, b):
    return a, b

list(f(1, 2))

# Issue #23
def f(a, b):
    return a, b

list(f(1, 2))

# Issue
