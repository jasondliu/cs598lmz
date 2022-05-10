fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Should raise a TypeError
fn.__code__ = None
fn()

# Should raise a TypeError
fn.__code__ = 42
fn()

# Should raise a TypeError
fn.__code__ = "foo"
fn()

# Should raise a TypeError
fn.__code__ = object()
fn()

# Should raise a TypeError
fn.__code__ = object
fn()

# Should raise a TypeError
fn.__code__ = type
fn()

# Should raise a TypeError
fn.__code__ = type(lambda: None)
fn()

# Should raise a TypeError
fn.__code__ = type(object())
fn()

# Should raise a TypeError
fn.__code__ = type(object)
fn()

# Should raise a TypeError
fn.__code__ = type(type)
fn()

# Should raise a TypeError
fn.__code__ = type(type(lambda: None))
fn()

# Should raise a TypeError
fn.__code__ = type(
