fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__qualname__ = 'fn'
fn.__module__ = '__main__'
fn.__annotations__ = {}
fn.__kwdefaults__ = None
fn.__defaults__ = ()
fn.__dict__ = {}
