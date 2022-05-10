fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = type(gi.gi_code)()
fn.__code__.co_code = b'\x00'
fn()
</code>

