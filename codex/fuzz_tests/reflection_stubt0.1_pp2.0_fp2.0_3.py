fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #24071: __code__ attribute of built-in functions should be read-only
def f(): pass
try:
    f.__code__ = None
except TypeError:
    pass
else:
    print("Assigning to __code__ of built-in function should raise TypeError")

# Issue #24071: __code__ attribute of built-in methods should be read-only
def f(): pass
try:
    f.__call__.__code__ = None
except TypeError:
    pass
else:
    print("Assigning to __code__ of built-in method should raise TypeError")

# Issue #24071: __code__ attribute of built-in methods should be read-only
def f(): pass
try:
    f.__new__.__code__ = None
except TypeError:
    pass
else:
    print("Assigning to __code__ of built-in method should raise TypeError")

# Issue #24071: __code__ attribute of built-in methods should be read-only
def f(): pass

