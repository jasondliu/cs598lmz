fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'test'
fn.__doc__ = 'test'
fn.__dict__ = {}
fn.__defaults__ = ()
