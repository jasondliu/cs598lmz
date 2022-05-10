fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Code objects are not callable
try:
    compile('1', '<string>', 'exec').__call__()
except TypeError:
    pass
else:
    raise Exception("__call__ on code object should raise TypeError")

# Code objects are not iterable
try:
    iter(compile('1', '<string>', 'exec'))
except TypeError:
    pass
else:
    raise Exception("iter on code object should raise TypeError")

# Code objects are not subscriptable
try:
    compile('1', '<string>', 'exec')[0]
except TypeError:
    pass
else:
    raise Exception("__getitem__ on code object should raise TypeError")

# Code objects are not hashable
try:
    hash(compile('1', '<string>', 'exec'))
except TypeError:
    pass
else:
    raise Exception("hash on code object should raise TypeError")

# Code objects are not pickleable
try:
    import pickle
except ImportError:
    pass
