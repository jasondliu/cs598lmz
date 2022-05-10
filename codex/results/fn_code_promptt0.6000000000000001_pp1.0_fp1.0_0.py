fn = lambda: None
# Test fn.__code__ is None.
e = None
try:
    fn.__code__
except AttributeError:
    e = True
assert e is not None
assert fn.__code__ is None
# Test fn.__code__.co_argcount is None.
e = None
try:
    fn.__code__.co_argcount
except AttributeError:
    e = True
assert e is not None
assert fn.__code__.co_argcount is None
# Test fn.__code__.co_argcount is None.
e = None
try:
    fn.__code__.co_argcount
except AttributeError:
    e = True
assert e is not None
assert fn.__code__.co_argcount is None
# Test fn.__code__.co_argcount is None.
e = None
try:
    fn.__code__.co_argcount
except AttributeError:
    e = True
assert e is not None
assert fn.__code__.co_argcount is None
# Test fn.__code__.co_argcount is
