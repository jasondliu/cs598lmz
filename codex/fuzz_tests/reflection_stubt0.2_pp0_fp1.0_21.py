fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# This should not raise an exception
fn.__code__ = None
fn()

# This should raise an exception
fn.__code__ = gi
fn()

# This should not raise an exception
fn.__code__ = None
fn()

# This should raise an exception
fn.__code__ = gi
fn()

# This should not raise an exception
fn.__code__ = None
fn()

# This should raise an exception
fn.__code__ = gi
fn()

# This should not raise an exception
fn.__code__ = None
fn()

# This should raise an exception
fn.__code__ = gi
fn()

# This should not raise an exception
fn.__code__ = None
fn()

# This should raise an exception
fn.__code__ = gi
fn()

# This should not raise an exception
fn.__code__ = None
fn()

# This should raise an exception
fn.__code__ = gi
fn()

# This should not raise an exception

