fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #22897: a generator should not be able to set __code__ to
# something that is not a code object.
gi = (i for i in ())
try:
    gi.__code__ = None
except TypeError:
    pass
else:
    print("Failed to raise TypeError")

# Issue #22897: a generator should not be able to set __code__ to
# something that is not a code object.
gi = (i for i in ())
try:
    gi.__code__ = 'foo'
except TypeError:
    pass
else:
    print("Failed to raise TypeError")

# Issue #22897: a generator should not be able to set __code__ to
# something that is not a code object.
gi = (i for i in ())
try:
    gi.__code__ = 123
except TypeError:
    pass
else:
    print("Failed to raise TypeError")

# Issue #22897: a generator should not be able to set __code__ to
#
