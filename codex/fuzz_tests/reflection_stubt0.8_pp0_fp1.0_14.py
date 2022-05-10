fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

try:
    exec(fn)
except TypeError:
    pass
else:
    raise Excep
