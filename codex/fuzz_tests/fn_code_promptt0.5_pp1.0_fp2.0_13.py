fn = lambda: None
# Test fn.__code__.co_argcount
fn.__code__ = types.CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')

# Test obj.__class__
obj = lambda: None
obj.__class__ = lambda: None
obj.__class__.__name__ = 42

# Test obj.__class__.__mro__
obj.__class__.__mro__ = lambda: None

# Test type(obj).__mro__
# Test type(obj).__subclasses__()
# Test type(obj).mro()

# Test type(obj).__subclasses__
type(obj).__subclasses__ = lambda: None

# Test type(obj).mro
type(obj).mro = lambda: None

# Test type(obj).__bases__
type(obj).__bases__ = lambda: None

# Test type(obj).__base__
type(obj).__base__ = lambda: None

# Test type(obj).__name__
type(obj).__name__ = lambda
