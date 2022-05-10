fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = '<lambda>'
fn.__module__ = '__main__'
fn.__dict__ = {}
fn.__defaults__ = ()
