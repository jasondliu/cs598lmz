fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# This should raise a TypeError, but instead it raises a SystemError
# because the interpreter tries to dereference the code object's
# co_consts attribute.

# The problem is that the code object's co_consts attribute is
# initialized to NULL, but the interpreter doesn't check for that
# before dereferencing it.

# The fix is to initialize co_consts to an empty tuple.

# See also:
# http://bugs.python.org/issue1733
