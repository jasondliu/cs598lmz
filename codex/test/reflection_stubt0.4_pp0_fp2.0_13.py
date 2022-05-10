fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'foo'
fn.__module__ = 'bar'
fn.__doc__ = 'baz'
fn.__dict__ = {'a': 1, 'b': 2}
fn.__defaults__ = (1, 2, 3)
