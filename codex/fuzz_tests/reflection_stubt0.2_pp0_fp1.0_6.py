fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# This should raise a TypeError, but it doesn't
# because the code object is not checked for
# being a code object.

# This is a bug in the implementation of the
# builtin function()

# The bug is fixed in Python 3.7.0
