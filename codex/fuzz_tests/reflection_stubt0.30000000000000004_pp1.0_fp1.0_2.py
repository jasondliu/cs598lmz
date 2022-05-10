fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #30897: crash when __code__ is a coroutine function
def coro():
    yield

fn.__code__ = coro
fn()

# Issue #30901: crash when __code__ is a method
fn.__code__ = fn.__code__.__call__
fn()

# Issue #30904: crash when __code__ is a coroutine function
fn.__code__ = coro
fn()

# Issue #30905: crash when __code__ is a method
fn.__code__ = fn.__code__.__call__
fn()

# Issue #30908: crash when __code__ is a method
fn.__code__ = fn.__code__.__call__
fn()

# Issue #30909: crash when __code__ is a coroutine function
fn.__code__ = coro
fn()

# Issue #30910: crash when __code__ is a method
fn.__code__ = fn.__code__.__call__
fn()

# Issue #30911: crash when
