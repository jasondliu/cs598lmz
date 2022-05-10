fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
del gi
</code>
This will blow up in Python 2.7 and below, which didn't support modifying the <code>__code__</code> attribute of function objects.

