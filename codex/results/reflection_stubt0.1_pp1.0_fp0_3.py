fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #24071: __code__ should be read-only
def f(): pass
try:
    f.__code__ = None
except TypeError:
    pass
else:
    print("Assigning to __code__ didn't raise TypeError")

# Issue #24071: __code__ should be read-only
def f(): pass
try:
    del f.__code__
except TypeError:
    pass
else:
    print("Deleting __code__ didn't raise TypeError")

# Issue #24071: __code__ should be read-only
def f(): pass
try:
    f.__code__.co_filename = "foo"
except TypeError:
    pass
else:
    print("Assigning to __code__.co_filename didn't raise TypeError")

# Issue #24071: __code__ should be read-only
def f(): pass
try:
    del f.__code__.co_filename
except TypeError:
    pass
else:
    print("Deleting __code__
