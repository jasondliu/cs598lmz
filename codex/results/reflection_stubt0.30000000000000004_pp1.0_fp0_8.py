fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #27072: test that the code object is not modified by the call.
assert gi.gi_code is fn.__code__

# Issue #27072: test that the code object is not modified by the call.
assert gi.gi_code is fn.__code__

# Issue #27072: test that the code object is not modified by the call.
assert gi.gi_code is fn.__code__

# Issue #27072: test that the code object is not modified by the call.
assert gi.gi_code is fn.__code__

# Issue #27072: test that the code object is not modified by the call.
assert gi.gi_code is fn.__code__

# Issue #27072: test that the code object is not modified by the call.
assert gi.gi_code is fn.__code__

# Issue #27072: test that the code object is not modified by the call.
assert gi.gi_code is fn.__code__

# Issue #
