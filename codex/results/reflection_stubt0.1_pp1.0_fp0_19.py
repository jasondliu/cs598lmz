fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #24071: __code__ should not be writable on built-in functions
def f(): pass
try:
    f.__code__ = None
except TypeError:
    pass
else:
    print("f.__code__ = None should have raised TypeError")

# Issue #24071: __code__ should not be writable on built-in methods
def f(): pass
try:
    f.__call__.__code__ = None
except TypeError:
    pass
else:
    print("f.__call__.__code__ = None should have raised TypeError")

# Issue #24071: __code__ should not be writable on built-in methods
def f(): pass
try:
    f.__new__.__code__ = None
except TypeError:
    pass
else:
    print("f.__new__.__code__ = None should have raised TypeError")

# Issue #24071: __code__ should not be writable on built-in methods
def f(): pass
try:
    f
