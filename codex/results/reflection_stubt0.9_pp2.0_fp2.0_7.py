fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
try:
    globals()[m](fn, globals()[m])
except TypeError:
    print(False)
