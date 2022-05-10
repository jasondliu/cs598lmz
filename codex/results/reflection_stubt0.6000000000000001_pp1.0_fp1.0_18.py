fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = '__code__'
fn.__module__ = '__code__'

# Check if the code object itself is a generator.
assert isinstance(fn.__code__, types.GeneratorType)

# Check if the code object's attributes are all generators.
for attr in dir(fn.__code__):
    if attr.startswith('co_'):
        assert isinstance(getattr(fn.__code__, attr), types.GeneratorType)
