fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

# Test that the code object is accessible on the instance
assert fn.__code__ is fn.__func__.__code__

# Test that the code object is accessible on the class
assert fn.__class__.__code__ is fn.__func__.__code__

# Test that the code object is accessible on the metaclass
assert fn.__class__.__class__.__code__ is fn.__func__.__code__

# Test that the code object is accessible on the metaclass's metaclass
assert fn.__class__.__class__.__class__.__code__ is fn.__func__.__code__

# Test that the code object is accessible on the metaclass's metaclass's metaclass
assert fn.__class__.__class__.__class__.__class__.__code__ is fn.__func__.__code__
