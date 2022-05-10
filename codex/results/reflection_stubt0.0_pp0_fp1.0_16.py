fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #23897: __code__ should be read-only
def f(): pass
try:
    f.__code__ = None
except TypeError:
    pass
else:
    print("Assigning to __code__ should raise TypeError")

# Issue #23897: __code__ should be read-only
def f(): pass
try:
    del f.__code__
except TypeError:
    pass
else:
    print("Deleting __code__ should raise TypeError")

# Issue #23897: __code__ should be read-only
def f(): pass
try:
    f.__code__.co_filename = "foo"
except AttributeError:
    pass
else:
    print("Assigning to __code__.co_filename should raise AttributeError")

# Issue #23897: __code__ should be read-only
def f(): pass
try:
    del f.__code__.co_filename
except AttributeError:
    pass
else:
    print("Deleting __code__
