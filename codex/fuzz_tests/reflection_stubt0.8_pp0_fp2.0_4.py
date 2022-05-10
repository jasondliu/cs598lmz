fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# Crashes in xrange_new on OS X 10.7.
xrange(fn)
