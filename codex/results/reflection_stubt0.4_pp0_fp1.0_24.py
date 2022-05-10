fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# This should raise a TypeError.
fn.__code__ = ()
fn()

# This should raise a TypeError.
fn.__code__ = 'abc'
fn()

# This should raise a TypeError.
fn.__code__ = object()
fn()

# This should raise a TypeError.
fn.__code__ = object()
fn()

# This should raise a TypeError.
fn.__code__ = object()
fn()

# This should raise a TypeError.
fn.__code__ = object()
fn()

# This should raise a TypeError.
fn.__code__ = object()
fn()

# This should raise a TypeError.
fn.__code__ = object()
fn()

# This should raise a TypeError.
fn.__code__ = object()
fn()

# This should raise a TypeError.
fn.__code__ = object()
fn()

# This should raise a TypeError.
fn.__code__ = object()
fn()

# This should raise a Type
