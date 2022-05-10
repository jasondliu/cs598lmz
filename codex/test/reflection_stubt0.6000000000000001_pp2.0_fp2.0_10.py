fn = lambda: None
gi = (i for i in ())
fn.__code__ = compile("foo", "bar", "exec")
