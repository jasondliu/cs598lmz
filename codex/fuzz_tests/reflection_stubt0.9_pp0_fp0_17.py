fn = lambda: None
gi = (i for i in ())
fn.__code__ = 1
gi.__code__ = 1
print(callable(fn))
print(callable(gi))
