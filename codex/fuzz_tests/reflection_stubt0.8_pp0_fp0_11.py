fn = lambda: None
gi = (i for i in ())
fn.__code__ = False
fn.__code__ = gi
