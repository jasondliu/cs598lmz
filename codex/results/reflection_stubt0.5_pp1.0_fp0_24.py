fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
try:
    fn()
except TypeError:
    pass
else:
    raise RuntimeError('TypeError not raised')

# Make sure that the iterator is not consumed
gi = (i for i in (1, 2, 3))
fn.__code__ = gi
try:
    fn()
except TypeError:
    pass
else:
    raise RuntimeError('TypeError not raised')

# Make sure that the iterator is not consumed
gi = (i for i in (1, 2, 3))
fn.__code__ = gi
try:
    fn()
except TypeError:
    pass
else:
    raise RuntimeError('TypeError not raised')

# Make sure that the iterator is not consumed
gi = (i for i in (1, 2, 3))
fn.__code__ = gi
try:
    fn()
except TypeError:
    pass
else:
    raise RuntimeError('TypeError not raised')

# Make sure that the iterator is not consumed
gi = (i for i in (1, 2, 3))
fn.__code__
