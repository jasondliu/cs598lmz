fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #12072: crash when __code__ is set to a non-code object.
fn = lambda: None
fn.__code__ = fn
fn()

# Issue #12072: crash when __code__ is set to a non-code object.
fn = lambda: None
fn.__code__ = object()
fn()

# Issue #12072: crash when __code__ is set to a non-code object.
fn = lambda: None
fn.__code__ = type
fn()

# Issue #12072: crash when __code__ is set to a non-code object.
fn = lambda: None
fn.__code__ = type(fn)
fn()

# Issue #12072: crash when __code__ is set to a non-code object.
fn = lambda: None
fn.__code__ = type(lambda: None)
fn()

# Issue #12072: crash when __code__ is set to a non-code object.
fn = lambda: None
fn.__code__ = type(lambda: None
