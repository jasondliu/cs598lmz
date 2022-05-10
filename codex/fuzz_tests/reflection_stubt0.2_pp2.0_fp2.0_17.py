fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# This should raise a TypeError
fn()

# This should raise a TypeError
fn.__code__ = None

# This should raise a TypeError
fn.__code__ = 1

# This should raise a TypeError
fn.__code__ = "string"

# This should raise a TypeError
fn.__code__ = b"bytes"

# This should raise a TypeError
fn.__code__ = 1.0

# This should raise a TypeError
fn.__code__ = 1j

# This should raise a TypeError
fn.__code__ = object()

# This should raise a TypeError
fn.__code__ = []

# This should raise a TypeError
fn.__code__ = {}

# This should raise a TypeError
fn.__code__ = ()

# This should raise a TypeError
fn.__code__ = set()

# This should raise a TypeError
fn.__code__ = frozenset()

# This should raise a TypeError
fn.__code__ = range(0)

# This
