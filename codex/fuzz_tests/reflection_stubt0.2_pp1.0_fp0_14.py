fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #16077: __code__ should be read-only
def f(): pass
try:
    f.__code__ = 42
except TypeError:
    pass
else:
    print("Assigning to __code__ didn't raise TypeError")

# Issue #16077: __code__ should be read-only
def f(): pass
try:
    del f.__code__
except TypeError:
    pass
else:
    print("Deleting __code__ didn't raise TypeError")

# Issue #16077: __code__ should be read-only
def f(): pass
try:
    f.__code__.co_filename = 42
except AttributeError:
    pass
else:
    print("Assigning to __code__.co_filename didn't raise AttributeError")

# Issue #16077: __code__ should be read-only
def f(): pass
try:
    del f.__code__.co_filename
except AttributeError:
    pass
else:
    print("Deleting __code
