fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
try:
    fn()
except TypeError:
    pass
else:
    raise RuntimeError("TypeError not raised")

print("All done")
