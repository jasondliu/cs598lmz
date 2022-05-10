fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__qualname__ = 'fn'
fn.__annotations__ = {}
fn.__kwdefaults__ = None
fn.__globals__ = {}
fn.__closure__ = None
fn.__dict__ = {}
fn.__doc__ = None
fn.__text_signature__ = None

# Test that the function is not considered a builtin
assert not isbuiltin(fn)

# Test that the function is considered a builtin
fn.__module__ = 'builtins'
assert isbuiltin(fn)

# Test that the function is not considered a builtin
fn.__module__ = '__builtin__'
assert not isbuiltin(fn)

# Test that the function is considered a builtin
fn.__module__ = '__builtins__'
assert isbuiltin(fn)

# Test that the function is not considered a builtin
fn.__module__ = '__builtins__.__builtin__'
assert not isbuiltin(fn)

#
