fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__dict__ = {}
fn.__doc__ = ''
fn.__module__ = '__main__'
fn.__defaults__ = None
fn.__kwdefaults__ = None
