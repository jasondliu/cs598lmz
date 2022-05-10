fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
</code>
Is this a bug?

