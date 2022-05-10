fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# This should raise an exception, but currently does not.
# See https://bugs.python.org/issue33169
# fn.__code__ = None
# fn()
