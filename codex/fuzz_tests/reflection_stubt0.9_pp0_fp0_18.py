fn = lambda: None
gi = (i for i in ())
fn.__code__ = None
fn()
gc.collect()
