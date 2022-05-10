fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = '__code__'
fn.__module__ = '__code__'

# Check if the code object itself is a generator.
