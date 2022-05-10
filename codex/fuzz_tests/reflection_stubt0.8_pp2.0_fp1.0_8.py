fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that setting/deleting __code__ works as expected
fn.__code__ = None
del fn.__code__
a = 1
fn.__code__ = a
del fn.__code__
