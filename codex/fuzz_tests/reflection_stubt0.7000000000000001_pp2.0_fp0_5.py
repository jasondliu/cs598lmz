fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
print(fn.__code__)
