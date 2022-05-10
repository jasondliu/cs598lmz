fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__qualname__ = 'fn'
fn.__annotations__ = {}
fn.__doc__ = None
