fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
del fn
del gi

# `__code__` must be a code object.
gi = (i for i in ())
try:
    gi.__code__ = 1
except TypeError:
    pass
else:
    print("TypeError expected")

# `__code__` must be a code object.
gi = (i for i in ())
try:
    gi.__code__ = "a"
except TypeError:
    pass
else:
    print("TypeError expected")

# `__code__` must be a code object.
gi = (i for i in ())
try:
    gi.__code__ = object()
except TypeError:
    pass
else:
    print("TypeError expected")

# `__code__` must be a code object.
gi = (i for i in ())
try:
    gi.__code__ = lambda: None
except TypeError:
    pass
else:
    print("TypeError expected")

# `__code__` must be a code object.
gi = (i for i
