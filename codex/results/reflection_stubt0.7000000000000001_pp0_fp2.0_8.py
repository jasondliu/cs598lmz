fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__code__()
# ValueError: generator already executing
</code>

