fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# This should not crash
fn()

# This should not crash
fn.__code__()

# This should not crash
fn.__code__.__code__()

# This should not crash
fn.__code__.__code__.__code__()

# This should not crash
fn.__code__.__code__.__code__.__code__()

# This should not crash
fn.__code__.__code__.__code__.__code__.__code__()

# This should not crash
fn.__code__.__code__.__code__.__code__.__code__.__code__()

# This should not crash
fn.__code__.__code__.__code__.__code__.__code__.__code__.__code__()

# This should not crash
fn.__code__.__code__.__code__.__code__.__code__.__code__.__code__.__code__()

# This should not crash
fn.__code__.__code__.__
