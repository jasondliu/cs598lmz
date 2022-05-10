fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
# raises TypeError: 'generator' object is not callable
</code>

