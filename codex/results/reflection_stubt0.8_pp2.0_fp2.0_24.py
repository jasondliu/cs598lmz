fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.send(None).send(1).send
fn()
