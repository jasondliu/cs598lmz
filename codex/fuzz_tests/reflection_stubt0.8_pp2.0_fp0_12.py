fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
# Crash interpreted as RuntimeError, see issue #22798
try:
    type(fn)
except RuntimeError:
    print('RuntimeError')
