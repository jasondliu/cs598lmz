fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# This should raise a TypeError, but currently doesn't.
# See https://bugs.python.org/issue28167
# fn.__code__ = (i for i in ())
# fn()
