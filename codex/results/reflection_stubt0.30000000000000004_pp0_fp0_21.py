fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #34:  __code__ can be set to a tuple
fn = lambda: None
fn.__code__ = (1, 2, 3)
fn()

# Issue #35:  __code__ can be set to a list
fn = lambda: None
fn.__code__ = [1, 2, 3]
fn()

# Issue #36:  __code__ can be set to a set
fn = lambda: None
fn.__code__ = {1, 2, 3}
fn()

# Issue #37:  __code__ can be set to a frozenset
fn = lambda: None
fn.__code__ = frozenset([1, 2, 3])
fn()

# Issue #38:  __code__ can be set to a memoryview
fn = lambda: None
fn.__code__ = memoryview(b"abc")
fn()

# Issue #39:  __code__ can be set to a bytearray
fn = lambda: None
fn.__code__ = bytearray(b"abc")
fn
