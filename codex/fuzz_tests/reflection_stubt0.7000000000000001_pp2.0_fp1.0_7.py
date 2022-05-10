fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = "<lambda>\n"

# The presence of the __closure__ attribute indicates a closure.
fn.__closure__ = (lambda: None,)

# Add attributes to shut up the pickle machinery.
fn.__dict__ = { '__dict__': None, '__weakref__': None }

# Add attributes to shut up the unpickler.
fn.func_closure = None
fn.func_code = None
fn.func_defaults = None
fn.func_globals = None
fn.func_name = "<lambda>\n"

# Add attributes to shut up the pickler.
fn.__name__ = "<lambda>\n"
fn.__qualname__ = "<lambda>\n"
fn.__module__ = "<lambda>\n"
fn.__getstate__ = lambda self: None
fn.__setstate__ = lambda self, state: None
fn.__reduce_ex__ = lambda self, proto: (lambda: None)
fn.__reduce__ = lambda self: (lambda:
