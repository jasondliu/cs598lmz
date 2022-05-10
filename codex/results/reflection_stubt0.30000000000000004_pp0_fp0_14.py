fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# This should raise a TypeError
fn.__code__ = 1
fn()

# This should raise a TypeError
fn.__code__ = 'a'
fn()

# This should raise a TypeError
fn.__code__ = object()
fn()

# This should raise a TypeError
fn.__code__ = {'a': 1}
fn()

# This should raise a TypeError
fn.__code__ = []
fn()

# This should raise a TypeError
fn.__code__ = ()
fn()

# This should raise a TypeError
fn.__code__ = None
fn()

# This should raise a TypeError
fn.__code__ = True
fn()

# This should raise a TypeError
fn.__code__ = False
fn()

# This should raise a TypeError
fn.__code__ = 1.0
fn()

# This should raise a TypeError
fn.__code__ = 1j
fn()

# This should raise a TypeError
fn.__code__ = b'a
