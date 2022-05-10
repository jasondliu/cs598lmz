fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'test_name'
fn.__doc__ = 'test_doc'
fn.__dict__ = {}
fn.__defaults__ = (1, 2)
fn.__kwdefaults__ = {'a': 1, 'b': 2}
