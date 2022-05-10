fn = lambda: None
gi = (i for i in ())
fn.__code__ = fn.__self__
self.assertIs(sys.exc_info()[2], None)
fn = gi.__code__
fn.__code__ = ()
