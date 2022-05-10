fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #27071: __code__ should be read-only
def f(): pass
try:
    f.__code__ = 42
except TypeError:
    pass
else:
    print("Assigning to __code__ didn't raise TypeError")

# Issue #27071: __code__ should be read-only
def f(): pass
try:
    del f.__code__
except TypeError:
    pass
else:
    print("Deleting __code__ didn't raise TypeError")

# Issue #27071: __code__ should be read-only
def f(): pass
try:
    f.__code__ += 42
except TypeError:
    pass
else:
    print("In-place adding to __code__ didn't raise TypeError")

# Issue #27071: __code__ should be read-only
def f(): pass
try:
    f.__code__ -= 42
except TypeError:
    pass
else:
    print("In-place subtracting from __code__ didn't raise TypeError")


