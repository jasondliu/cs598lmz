fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the iterator is closed.
gi = (i for i in (1, 2))
fn.__code__ = gi
fn()

# Test that the iterator is closed if an exception occurs.
gi = (i for i in ())
gi.throw(Exception)
fn.__code__ = gi
fn()

# Test that the iterator is closed if an exception occurs.
gi = (i for i in (1, 2))
gi.throw(Exception)
fn.__code__ = gi
fn()
