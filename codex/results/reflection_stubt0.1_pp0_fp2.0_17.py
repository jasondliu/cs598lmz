fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #23984: __code__ is not writable on built-in functions
import builtins
try:
    builtins.__import__.__code__ = None
except TypeError:
    pass
else:
    raise Exception("__code__ should not be writable on built-in functions")

# Issue #23984: __code__ is not writable on built-in methods
try:
    list.append.__code__ = None
except TypeError:
    pass
else:
    raise Exception("__code__ should not be writable on built-in methods")

# Issue #23984: __code__ is not writable on built-in methods
try:
    list.__add__.__code__ = None
except TypeError:
    pass
else:
    raise Exception("__code__ should not be writable on built-in methods")

# Issue #23984: __code__ is not writable on built-in methods
try:
    list.__getitem__.__code__ = None
except TypeError:
    pass
