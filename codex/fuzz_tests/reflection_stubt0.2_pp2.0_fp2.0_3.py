fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #17093: segfault when __code__ is set to a non-code object
def f():
    pass

try:
    f.__code__ = f
except TypeError:
    pass
else:
    print("Assigning a function to __code__ should raise a TypeError")

# Issue #17093: segfault when __code__ is set to a non-code object
def f():
    pass

try:
    f.__code__ = 1
except TypeError:
    pass
else:
    print("Assigning an int to __code__ should raise a TypeError")

# Issue #17093: segfault when __code__ is set to a non-code object
def f():
    pass

try:
    f.__code__ = "abc"
except TypeError:
    pass
else:
    print("Assigning a str to __code__ should raise a TypeError")

# Issue #17093: segfault when __code__ is set to a non-code object

