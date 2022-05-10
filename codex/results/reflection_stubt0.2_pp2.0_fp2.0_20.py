fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that __code__ can be set to a tuple
fn = lambda: None
fn.__code__ = (1, 2, 3, 4, 5)
fn()

# Test that __code__ can be set to a list
fn = lambda: None
fn.__code__ = [1, 2, 3, 4, 5]
fn()

# Test that __code__ can be set to a set
fn = lambda: None
fn.__code__ = {1, 2, 3, 4, 5}
fn()

# Test that __code__ can be set to a frozenset
fn = lambda: None
fn.__code__ = frozenset([1, 2, 3, 4, 5])
fn()

# Test that __code__ can be set to a bytearray
fn = lambda: None
fn.__code__ = bytearray([1, 2, 3, 4, 5])
fn()

# Test that __code__ can be set to a memoryview
fn = lambda: None
fn.__code__ = memoryview(b"
