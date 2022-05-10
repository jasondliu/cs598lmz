fn = lambda: None
gi = (i for i in ())
fn.__code__ = type(lambda: None)().__code__
gi.gi_frame.f_code = fn.__code__
gi.gi_frame.f_locals = {'__builtins__': {'__import__': __import__}}

# The following is a hack to make this work on Python 3.x
gi.gi_frame.f_globals = {'__name__': '__main__', '__package__': None}
# End of hack

import sys
sys.modules['__main__'] = gi
sys.modules['__builtin__'] = gi.gi_frame.f_locals['__builtins__']

del sys, gi, fn, __import__

# The following is a hack to make this work on Python 3.x
try:
    import __builtin__
except ImportError:
    import builtins as __builtin__
# End of hack

import os

# The following is a hack to make this work on Python 3.x
try:
    import __builtin__
except ImportError:
    import builtins as __
