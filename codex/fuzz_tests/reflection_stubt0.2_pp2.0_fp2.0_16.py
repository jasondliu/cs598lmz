fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# This should not raise an exception
fn.__code__ = None
fn()

# This should not raise an exception
fn.__code__ = 42
fn()

# This should not raise an exception
fn.__code__ = "abc"
fn()

# This should not raise an exception
fn.__code__ = b"abc"
fn()

# This should not raise an exception
fn.__code__ = bytearray(b"abc")
fn()

# This should not raise an exception
fn.__code__ = memoryview(b"abc")
fn()

# This should not raise an exception
fn.__code__ = range(10)
fn()

# This should not raise an exception
fn.__code__ = set()
fn()

# This should not raise an exception
fn.__code__ = frozenset()
fn()

# This should not raise an exception
fn.__code__ = dict()
fn()

# This should not raise an exception
fn.__code__ = object()
fn()


