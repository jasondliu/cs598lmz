fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.__code__
fn()
</code>
This is a bit less satisfying as it doesn't work for other types that don't have a <code>__code__</code> attribute - but it's a starting point for you.

