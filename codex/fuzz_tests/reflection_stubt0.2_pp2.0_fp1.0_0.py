fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# This should not crash
fn()
