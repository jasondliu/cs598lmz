fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# This should raise a TypeError, but it doesn't
fn.__code__ = (i for i in ())
fn()

# This should raise a TypeError, but it doesn't
fn.__code__ = (i for i in ())
fn()

# This should raise a TypeError, but it doesn't
fn.__code__ = (i for i in ())
fn()

# This should raise a TypeError, but it doesn't
fn.__code__ = (i for i in ())
fn()

# This should raise a TypeError, but it doesn't
fn.__code__ = (i for i in ())
fn()

# This should raise a TypeError, but it doesn't
fn.__code__ = (i for i in ())
fn()

# This should raise a TypeError, but it doesn't
fn.__code__ = (i for i in ())
fn()

# This should raise a TypeError, but it doesn't
fn.__code__ = (i for i in ())
fn()

# This should raise a TypeError,
