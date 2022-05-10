fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__code__()

# TypeError: 'generator' object is not callable
fn.__code__ = None
fn.__code__()

# TypeError: 'NoneType' object is not callable
fn.__code__ = 0
fn.__code__()

# TypeError: 'int' object is not callable
fn.__code__ = ''
fn.__code__()

# TypeError: 'str' object is not callable
fn.__code__ = []
fn.__code__()

# TypeError: 'list' object is not callable
fn.__code__ = {}
fn.__code__()

# TypeError: 'dict' object is not callable
fn.__code__ = ()
fn.__code__()

# TypeError: 'tuple' object is not callable
fn.__code__ = set()
fn.__code__()

# TypeError: 'set' object is not callable
fn.__code__ = frozenset()
fn.__code__()

# TypeError: '
