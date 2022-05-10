fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# In Python 3.5, __code__ is read-only.
try:
    fn.__code__ = None
except TypeError:
    pass
else:
    raise RuntimeError("shouldn't be able to set __code__")

# In Python 3.5, __code__ is read-only.
try:
    del fn.__code__
except TypeError:
    pass
else:
    raise RuntimeError("shouldn't be able to delete __code__")

# In Python 3.5, __code__ is read-only.
try:
    fn.__code__ = None
except TypeError:
    pass
else:
    raise RuntimeError("shouldn't be able to set __code__")

# In Python 3.5, __code__ is read-only.
try:
    del fn.__code__
except TypeError:
    pass
else:
    raise RuntimeError("shouldn't be able to delete __code__")
