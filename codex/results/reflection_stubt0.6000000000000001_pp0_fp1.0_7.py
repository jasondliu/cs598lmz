fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
</code>
which is basically the same thing.

