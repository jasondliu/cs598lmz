fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# This should raise a TypeError
fn()

# This should raise a TypeError
fn.__code__ = None

# This should raise a TypeError
fn()

# This should raise a TypeError
fn.__code__ = "abc"

# This should raise a TypeError
fn()

# This should raise a TypeError
fn.__code__ = 1

# This should raise a TypeError
fn()

# This should raise a TypeError
fn.__code__ = lambda: None

# This should raise a TypeError
fn()

# This should raise a TypeError
fn.__code__ = fn

# This should raise a TypeError
fn()

# This should raise a TypeError
fn.__code__ = fn.__code__

# This should raise a TypeError
fn()

# This should raise a TypeError
fn.__code__ = fn.__code__.__code__

# This should raise a TypeError
fn()

# This should raise a TypeError
fn.__code__ = fn.__code__.
