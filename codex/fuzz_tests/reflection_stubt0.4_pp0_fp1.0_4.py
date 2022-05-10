fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'

# Create a new function with the same code object
g = types.FunctionType(fn.__code__, globals(), fn.__name__)

# Verify that the code object really is the same
assert g.__code__ is fn.__code__

# Verify that the function can be called
assert g() is None

# Verify that the function can be called with arguments
assert g(1, 2, 3) is None
</code>

