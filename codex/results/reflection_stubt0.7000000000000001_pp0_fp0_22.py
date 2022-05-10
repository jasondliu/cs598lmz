fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# returns generator, which is not callable
fn.__code__()
</code>

