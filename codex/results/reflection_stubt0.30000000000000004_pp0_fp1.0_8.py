fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# This should not raise a TypeError
fn.__code__ = None
fn()

# This should not raise a TypeError
fn.__code__ = gi
fn()

# This should not raise a TypeError
fn.__code__ = None
fn()

# This should not raise a TypeError
fn.__code__ = gi
fn()
