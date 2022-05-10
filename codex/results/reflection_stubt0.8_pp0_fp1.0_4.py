fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
fn.__code__ = (i for i in ())
fn()
