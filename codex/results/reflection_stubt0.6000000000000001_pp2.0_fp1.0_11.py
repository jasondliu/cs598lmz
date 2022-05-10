fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# run the code
fn()
