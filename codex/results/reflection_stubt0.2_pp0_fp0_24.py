fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# This should raise a TypeError, but instead it raises a SystemError.
# The problem is that the code object is not a code object, but a
# generator object.
#
# The problem is that the code object is not a code object, but a
# generator object.
#
# The problem is that the code object is not a code object, but a
# generator object.
#
# The problem is that the code object is not a code object, but a
# generator object.
#
# The problem is that the code object is not a code object, but a
# generator object.
#
# The problem is that the code object is not a code object, but a
# generator object.
#
# The problem is that the code object is not a code object, but a
# generator object.
#
# The problem is that the code object is not a code object, but a
# generator object.
#
# The problem is that the code object is not a code object, but a
# generator object.
#
# The problem is that the code object is not a code object, but
