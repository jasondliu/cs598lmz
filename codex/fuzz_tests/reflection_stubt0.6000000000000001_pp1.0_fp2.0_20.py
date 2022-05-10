fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# `__qualname__` is the qualified name of a class or function
fn = lambda: None
fn.__qualname__ = 'str'
fn()

# `__sizeof__` returns the size of an object in bytes
fn = lambda: None
fn.__sizeof__ = lambda: 'str'
fn()

# `__str__` returns the informal string representation of an object
fn = lambda: None
fn.__str__ = lambda: 1
str(fn)

# `__subclasshook__` is a static method called to implement `issubclass(cls, classinfo)`
fn = lambda: None
fn.__subclasshook__ = lambda: 'str'
issubclass(fn, int)

# `__text_signature__` is the signature of the callable object
fn = lambda: None
fn.__text_signature__ = 'str'
fn()

# `__weakref__` is list of weak references to the object
fn = lambda: None
fn.__weakref__ = ['str']
fn()
