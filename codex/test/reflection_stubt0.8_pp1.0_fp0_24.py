fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = '<lambda>'
fn.__qualname__ = '<lambda>'
