fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# This is a regression test for http://bugs.python.org/issue17375
# and http://bugs.python.org/issue17376.
#
# The bug is that the code object is not properly initialized, so
# the following code should raise a TypeError.

try:
    fn()
except TypeError:
    pass
else:
    raise RuntimeError("TypeError not raised")
