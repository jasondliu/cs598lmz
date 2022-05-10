fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
f = fn
del gi, fn


def run_iter(f):
    return list(f())


