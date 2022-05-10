fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# This should raise a TypeError, but instead it returns None.
# This is because the code object is not checked for being a code object.
# Instead, it is checked for being a sequence, which it is.
# The code object is then used as a sequence and the first element is used
# as the code object.
# This is a bug.

# The bug is fixed in Python 3.5.
