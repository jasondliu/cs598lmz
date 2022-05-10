fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'test_fn'
fn.__dict__ = {}
fn.__defaults__ = ()
