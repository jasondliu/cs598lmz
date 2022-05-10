fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__doc__ = 'doc'
fn.__annotations__ = {'a': 1}
fn.__dict__ = {'d': 2}
fn.__kwdefaults__ = {'e': 3}
