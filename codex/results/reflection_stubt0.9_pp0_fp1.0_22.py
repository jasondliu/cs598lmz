fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = gc
fn.__globals__ = {'__builtins__': BUILTIN_MODULES,
                  '__name__': '__main__', '__file__': '', '__doc__': None}
fn.__module__ = None
sys.modules['__builtin__'] = fn
sys.modules['builtins'] = fn
fn.__dict__.update(BUILTIN_MODULES)
fn.__dict__.update(BUILTIN_FUNCTIONS)
fn.__dict__.update(BUILTIN_CLASSES)
