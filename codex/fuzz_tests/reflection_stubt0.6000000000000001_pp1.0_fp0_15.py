fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
f = fn
print('done')
