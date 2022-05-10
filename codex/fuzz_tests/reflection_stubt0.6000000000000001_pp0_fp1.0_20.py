fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = type(gi.gi_code)()
fn()
# AttributeError: 'code' object has no attribute 'co_argcount'
</code>

