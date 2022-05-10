fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# __code__ is not writable, but we can still set it to a callable
# that raises an exception on call.
fn = lambda: None
fn.__code__ = lambda: 1/0
fn()

# __code__ is not writable, but we can still set it to a callable
# that raises an exception on call.
fn = lambda: None
fn.__code__ = lambda: 1/0
fn()

# __code__ is not writable, but we can still set it to a callable
# that raises an exception on call.
fn = lambda: None
fn.__code__ = lambda: 1/0
fn()

# __code__ is not writable, but we can still set it to a callable
# that raises an exception on call.
fn = lambda: None
fn.__code__ = lambda: 1/0
fn()

# __code__ is not writable, but we can still set it to a callable
# that raises an exception on call.
fn = lambda: None
fn.__code__ = lambda: 1
