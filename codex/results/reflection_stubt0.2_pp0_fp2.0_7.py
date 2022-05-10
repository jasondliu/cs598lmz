fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# This should raise a TypeError, but instead it raises a SystemError
# because the code object is not a code object.

# The problem is that the code object is not a code object, but
# instead a generator object.  The code object is the first element
# of the generator object, but the code object is not a code object
# itself.

# This is a bug in the Python interpreter.  The code object is
# supposed to be a code object, but it is not.

# This bug was fixed in Python 3.2.
