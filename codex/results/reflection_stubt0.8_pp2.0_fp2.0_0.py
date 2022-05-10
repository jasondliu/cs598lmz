fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
foo = type(lambda: None)
fn = foo.__new__(foo)
fn.__code__ = gi
fn()
</code>

