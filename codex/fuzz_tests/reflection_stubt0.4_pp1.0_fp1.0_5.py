fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# This should raise a RuntimeError
fn.__code__ = None
fn()

# This should raise a RuntimeError
fn.__code__ = lambda: None
fn()

# This should raise a RuntimeError
fn.__code__ = (i for i in ())
fn()
