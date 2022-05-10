fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# We check that f(0).f_code.co_firstlineno doesn't cause any error
fn.__code__ = gi(0)
fn()
