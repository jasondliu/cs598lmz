fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'

def f():
    pass

def g():
    pass

f.__code__ = g.__code__

# f.__code__.co_filename = 'a'
# f.__code__.co_firstlineno = 1

