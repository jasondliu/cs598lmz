fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__module__ = '__main__'

import pdb; pdb.set_trace()
fn()
