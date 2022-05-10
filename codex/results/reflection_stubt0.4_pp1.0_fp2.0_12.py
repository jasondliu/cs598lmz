fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# TypeError: 'code' object is not subscriptable
fn()
</code>

