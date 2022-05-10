fn = lambda: None
# Test fn.__code__.co_varnames
f = _fn
f.__code__.co_varnames = 1
try:
    f.__code__.co_varnames = {}
    raise RuntimeError
except TypeError:
    pass
# Test fn.__dict__
f = _fn
f.__dict__ = 1
try:
    f.__dict__ = {}
    raise RuntimeError
except TypeError:
    pass
# Test fn.__name__
f = _fn
f.__name__ = 1
try:
    f.__name__ = {}
    raise RuntimeError
except TypeError:
    pass
# Test fn.__qualname__
f = _fn
f.__qualname__ = 1
try:
    f.__qualname__ = {}
    raise RuntimeError
except TypeError:
    pass
# Test that fn is not callable after it has been deleted
del _fn
try:
    _fn()
    raise RuntimeError
except NameError:
    pass


# Class tests
def test_class_attr():
    # Test class att
