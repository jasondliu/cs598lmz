fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'foo'
fn.__doc__ = 'bar'
fn.__dict__ = {}
fn.__defaults__ = ()
