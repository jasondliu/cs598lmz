fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__qualname__ = 'fn'

# Make sure the code object is not owned by the function.
fn.__code__ = fn.__code__

# Make sure the function is not owned by the code object.
gi.gi_code = gi.gi_code

# Make sure the code object is not owned by the generator.
gi.gi_code = gi.gi_code

# Make sure the generator is not owned by the code object.
gi.gi_code.co_freevars = gi.gi_code.co_freevars

# Make sure the function is not owned by the generator.
gi.gi_frame.f_locals['fn'] = gi.gi_frame.f_locals['fn']

# Make sure the generator is not owned by the function.
fn.__code__.co_freevars = fn.__code__.co_freevars
