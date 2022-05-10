fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__module__ = '__main__'
fn.__dict__ = {}
fn.__defaults__ = ()
fn.__kwdefaults__ = None
