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

f.__code__.co_filename = 'a'
f.__code__.co_firstlineno = 1

import sys

sys.settrace(f)

# f.__code__ = g.__code__
# f.__code__.co_filename = 'b'
# f.__code__.co_firstlineno = 2

# f.__code__ = g.__code__
# f.__code__.co_filename = 'c'
# f.__code__.co_firstlineno = 3

def h():
    pass

f.__code__ = h.__code__

# f.__code__ = h.__code__

# f.__code__ = g.__code__
