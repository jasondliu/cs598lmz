fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the code object is not modified
assert gi.gi_code is fn.__code__

# Test that the code object is not modified
assert gi.gi_code is fn.__code__

# Test that the code object is not modified
assert gi.gi_code is fn.__code__

# Test that the code object is not modified
assert gi.gi_code is fn.__code__

# Test that the code object is not modified
assert gi.gi_code is fn.__code__

# Test that the code object is not modified
assert gi.gi_code is fn.__code__

# Test that the code object is not modified
assert gi.gi_code is fn.__code__

# Test that the code object is not modified
assert gi.gi_code is fn.__code__

# Test that the code object is not modified
assert gi.gi_code is fn.__code__

# Test that the code object is not modified
assert gi.gi_code is fn.__code__
