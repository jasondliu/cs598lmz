fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
code = fn.__code__
try:
    str(code)
except TypeError as e:
    print('TypeError: %s' % e)
